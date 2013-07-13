from django.utils.html import escape as h
from django.utils.html import format_html
from django.utils.html import force_text
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe
from .util import link_to
from .util import l_or_humanize
from inflexion import dasherize, humanize


class MenuError(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class MenuManager(object):
    _instance = None

    def __init__(self):
        self.items = {}

    def __new__(cls, *args, **kwargs):
        ''' Singleton '''
        if not cls._instance:
            cls._instance = super(MenuManager, cls) \
                .__new__(cls, *args, **kwargs)
        return cls._instance

    def map(self, menu_name):
        if self.items is None:
            self.items = {}
        return Mapper(menu_name, self.items)

    def items(self, menu_name):
        if menu_name in self.items:
            return self.items[menu_name]
        else:
            return MenuNode('root', {})


class MenuHelper(object):

    def __init__(self):
        pass

    @property
    def current_menu_item(self):
        '''Returns the current menu item name'''
        return self.controller.current_menu_item

    def render_main_menu(self, project):
        '''Renders the application main menu'''
        if (project and not project.is_new_record):
            self.render_menu('project_menu')
        else:
            self.render_menu('application_menu')

    def check_display_main_menu(self, project):
        if project and not project.is_new_record:
            menu_name = 'project_menu'
        else:
            menu_name = 'application_menu'
        return MenuManager().items(menu_name).has_children

    def render_menu(self, menu, project=None):
        links = []
        menu_items = self.menu_items_for(menu, project)
        for node in menu_items:
            links.append(self.render_menu_node(node, project))
        if len(links) > 0:
            return format_html('<ul>\n{0}\n</ul>', '\n'.join(links))
        else:
            return None

    def render_menu_node(self, node, project=None):
        if node.has_children or node.child_menus is not None:
            return self.render_menu_node_with_children(node, project)
        else:
            caption, url, selected = self.extract_node_details(node, project)
            return format_html('<li>{0}</li>',
                               self.render_single_menu_node(node, caption, url,
                                                            selected))

    def render_menu_node_with_children(self, node, project=None):
        caption, url, selected = self.extract_node_details(node, project)

        html = []
        html.append('<li>')
        #Parent
        html.append(self.render_single_menu_node(node, caption, url, selected))

        # Standard children
        standard_children_list = (self.render_menu_node(child, project)
                                  for child in node.children)

        if not standard_children_list:
            html.append(format_html('<ul class="menu-children">{0}</ul>',
                                    ''.join(standard_children_list)))

        # Unattached children
        unattached_children_list = \
            self.render_unattached_children_menu(node, project)
        if not unattached_children_list:
            html.append(
                format_html('<ul class="menu-children unattached">{0}</ul>',
                            unattached_children_list))

        html.append('</li>')
        return mark_safe('\n'.join(html))

    def render_unattached_children_menu(self, node, project):
        '''Returns a list of unattached children menu items'''
        if not node.child_menus:
            return None

        unattached_children = node.child_menus.call(project)
        # Tree nodes support #each so we need to do opbject detection
        if not isinstance(unattached_children, (tuple, list)):
            raise MenuError("child_menus must be an array of MenuItems")

        return format_html_join(
            '\n', '<li>{0}</li>',
            [self.render_unattached_menu_item(child, project)
                for child in unattached_children]
        )

    def render_single_menu_node(self, item, caption, url, selected):
        return link_to(h(caption), url,
                       item.html_options({'selected': selected}))

    def render_unattached_menu_item(self, menu_item, project):
        if not isinstance(menu_item, MenuItem):
            raise MenuError(":child_menus must be an array of MenuItems")

        if User.current.check_allowed_to(menu_item_url, project):
            return link_to(h(menu_item.caption),
                           menu_item.url,
                           menu_item.html_options)
        else:
            return None

    @staticmethod
    def menu_items_for(menu, project=None):
        items = []
        for node in MenuManager().items(menu).root.children:
            if check_allowed_node(node, User.current, project):
                items.append(node)

        return items

    @staticmethod
    def extract_node_details(node, project=None):
        item = node
        if isinstance(item.url, dict):
            if project is None:
                url = item.url
            else:
                url = {item.param: project}.update(item.url)
        else:
            url = item.url
        caption = item.caption(project)
        return [caption, url, (current_menu_item == item.name)]

    @staticmethod
    def check_allowed_node(node, user, project):
        '''
        Checks if a user is allowed to access the menu item by:
            * Checking the url target (project only)
            * Checking the conditions of the item
        '''
        if project and user and not user.check_allowed_to(node.url, project):
            return False
        if node.condition and not node.condition(project):
          # Condition that doesn't pass
            return False
        return True


class Mapper(object):

    def __init__(self, menu, items):
        if not menu in items:
            items[menu] = MenuNode('root', {})
        self.menu = menu
        self.menu_items = items[menu]

    def push(self, name, url, options={}):
        '''
        Adds an item at the end of the menu. Available options:
         * param: the parameter name that is used for the project id
                  (default is :id)
         * if: a Proc that is called before rendering the item,
               the item is displayed only if it returns true
         * caption that can be:
           * a localized string Symbol
           * a String
           * a Proc that can take the project as argument
         * before, after: specify where the menu item should be inserted
                          (eg. :after => :activity)
         * parent: menu item will be added as a child of another named menu
                   (eg. 'parent' => :issues)
         * children: a Proc that is called before rendering the item.
                     The Proc should return an array of MenuItems,
                     which will be added as children to this item.
           eg. 'children' => Proc.new {|project| [MenuManager::MenuItem(...)] }
         * last: menu item will stay at the end (eg. :last => true)
         * html_options: a hash of html options that are passed to link_to
        '''
        options = options.copy()

        if options['parent']:
            subtree = self.find(options['parent'])
            if subtree:
                target_root = subtree
            else:
                target_root = self.menu_items.root
        else:
            target_root = self.menu_items.root

        # menu item position
        first = options.pop('first', False)
        before = options.pop('before', False)
        after = options.pop('after', False)
        last = options.pop('last', False)
        if first:
            target_root.prepend(MenuItem(name, url, options))
        elif before:
            if self.exists(before):
                target_root.add_at(MenuItem(name, url, options),
                                   position_of(before))
            else:
                target_root.add(MenuItem(name, url, options))
        elif after:
            if self.exists(after):
                target_root.add_at(MenuItem(name, url, options),
                                   position_of(after) + 1)
            else:
                target_root.add(MenuItem(name, url, options))
        elif last:  # don't delete, needs to be stored
            target_root.add_last(MenuItem(name, url, options))
        else:
            target_root.add(MenuItem(name, url, options))

        # Removes a menu item
        def delete(name):
            found = self.find(name)
            if found:
                self.menu_items.remove(found)

        # Checks if a menu item exists
        def exists(name):
            return any(x for x in self.menu_items if x.name == name)

        def find(name):
            next((x for x in self.menu_items if x.name == name), None)

        @staticmethod
        def position_of(name):
            for node in self.menu_items:
                if node.name == name:
                    return node.position
            return None


class MenuNode(object):

    def __init__(self, name, content=None):
        self.parent = None

        self.name = name
        self._children = []
        self.last_item_count = 0

    @property
    def children(self):
        return self._children

    def has_children(self):
        return len(self.children) > 0

    def __iter__(self):
        return iter(self._children)

    def size(self):
        ''' Returns the number of descendants + 1'''
        return reduce(lambda total, node: total + node.size, self.children, 1)

    # Adds a child at first position
    def prepend(self, child):
        self.add_at(child, 0)

    # Adds a child at given position
    def add_at(self, child, position):
        if any(node for node in self.children if node.name == child.name):
            raise MenuError("Child already added")

        self.children.insert(position, child)
        child.parent = self
        return child

    # Adds a child as last child
    def add_last(self, child):
        self.add_at(child, -1)
        self.last_items_count += 1
        return child

    # Adds a child
    def add(self, child):
        position = self.children.size() - self.last_items_count
        return self.add_at(child, position)

    def __lshift__(self, other):
        return self.add(other)

    # Removes a child
    def remove(self, child):
        del self.children[child]
        if child and child.last:
            self.last_items_count -= +1
        child.parent = None
        return child

    # Returns the position for this node in it's parent
    @property
    def position(self):
        return self.parent.children.index(self)

    # Returns the root for this node
    @property
    def root(self):
        root = self
        while root.parent:
            root = root.parent
        return root


class MenuItem(MenuNode):
    #include Redmine::I18n

    def __init__(self, name, url, options):
        if options['if'] and not hasattr(options['if'], '__call__'):
            raise ValueError("Invalid option 'if' for menu item '#{name}'")
        if options['html'] and not isinstance(options['html'], dict):
            raise ValueError("Invalid option 'html' for menu item '#{name}'")
        if options['parent'] == name:
            raise ValueError("Cannot set the 'parent' to be the same"
                             " as this item")
        if options['children'] \
           and not hasattr(options['children'], '__call__'):
            raise ValueError("Invalid option 'children' for"
                             " menu item '#{name}'")
        self.name = name
        self.url = url
        self.condition = options['if']
        self.param = options['param'] or 'id'
        self.caption = options['caption']
        self.html_options = options['html'] or {}
        # Adds a unique class to each menu item based on its name
        self.html_options['class'] = ' '.join(
            set(filter(None,
                [self.html_options['class'], dasherize(force_text(self.name))]
            )))
        self.parent = options['parent']
        self.child_menus = options['children']
        self.last = options['last'] or False
        super(self, self.name)

    def caption(self, project=None):
        if hasattr(self.caption, '__call__'):
            c = force_text(self.caption(project))
            if not c:
                c = humanize(force_text(self.name))
            return c
        else:
            if self.caption is None:
                return l_or_humanize(self.name, prefix='label_')
            else:
                return self.caption

    def html_options(self, options={}):
        if options['selected']:
            o = self.html_options.copy()
            o['class'] += ' selected'
            return o
        else:
            return self.html_options
