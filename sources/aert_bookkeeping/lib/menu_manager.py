
class MenuError(Exception):
    pass


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
        self.items = {}

    def render_menu(self, menu, project=None):
        links = []
        menu_items = self.menu_items_for(menu, project)
        for node in menu_items:
            links.append(self.render_menu_node(node, project))

        if links.count > 0:
            return content_tag('ul', links.join("\n").html_safe)
        else:
            return None

    def menu_items_for(self, menu, project=None):
        items = []
        for node in MenuManager().items(menu).root.children:
            if check_allowed_node(node, User.current, project):
                items.append(node)

        return items

    def check_allowed_node(node, user, project):
        '''
        Checks if a user is allowed to access the menu item by:

        * Checking the url target (project only)
        * Checking the conditions of the item
        '''
        if project and user and not user.check_allowed_to(node.url, project):
            return False

        if node.condition and not node.condition.call(project):
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
                   (eg. :parent => :issues)
         * children: a Proc that is called before rendering the item.
                     The Proc should return an array of MenuItems,
                     which will be added as children to this item.
           eg. :children => Proc.new {|project| [MenuManager::MenuItem(...)] }
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
            target_root.insert(0, MenuItem(name, url, options))
        elif before:
            if exists(before):
                target_root.insert(position_of(before),
                                   MenuItem(name, url, options))
            else:
                target_root.append(MenuItem(name, url, options))
        elif after:
            if exists(after):
                target_root.insert(position_of(after) + 1,
                                   MenuItem(name, url, options))
            else:
                target_root.add(MenuItem(name, url, options))
        elif last:  # don't delete, needs to be stored
            target_root.append(MenuItem(name, url, options))
        else:
            target_root.append(MenuItem(name, url, options))

        # Removes a menu item
        def delete(name):
            found = self.find(name)
            if found:
                del self.menu_items[found]

        # Checks if a menu item exists
        def exists(name):
            return any([x for x in self.menu_items if x.name == name])

        def find(name):
            next((x for x in self.menu_items if x.name == name), None)

        def position_of(name):
            for node in self.menu_items:
                if node.name == name:
                    return node.position


class MenuNode(list):

    def __init__(self, name, content=nil):
        self.parent = None

        self.name = name
        self.children = []
        self.last_item_count = 0

    # Adds a child at first position
    def prepend(child):
        self.children.insert(0, child)

    # Adds a child at given position
    def add_at(child, position):
        raise "Child already added" if find {|node| node.name == child.name}

        self.children.insert(position, child)
        child.parent = self
        return child

    # Adds a child as last child
    def add_last(child):
        add_at(child, -1)
        self.last_items_count += 1
        return child

    # Adds a child
    def add(child):
        self.children.in
    alias :<< :add

    # Removes a child
    def remove!(child)
      @children.delete(child)
      @last_items_count -= +1 if child && child.last
      child.parent = nil
      child
  
    # Returns the position for this node in it's parent
    def position
      self.parent.children.index(self)
  
    # Returns the root for this node
    def root
      root = self
      root = root.parent while root.parent
      root

class MenuItem(MenuNode):
    include Redmine::I18n
    attr_reader :name, :url, :param, :condition, :parent, :child_menus, :last
  
    def initialize(name, url, options)
      raise ArgumentError, "Invalid option :if for menu item '#{name}'" if options[:if] && !options[:if].respond_to?(:call)
      raise ArgumentError, "Invalid option :html for menu item '#{name}'" if options[:html] && !options[:html].is_a?(Hash)
      raise ArgumentError, "Cannot set the :parent to be the same as this item" if options[:parent] == name.to_sym
      raise ArgumentError, "Invalid option :children for menu item '#{name}'" if options[:children] && !options[:children].respond_to?(:call)
      @name = name
      @url = url
      @condition = options[:if]
      @param = options[:param] || :id
      @caption = options[:caption]
      @html_options = options[:html] || {}
      # Adds a unique class to each menu item based on its name
      @html_options[:class] = [@html_options[:class], @name.to_s.dasherize].compact.join(' ')
      @parent = options[:parent]
      @child_menus = options[:children]
      @last = options[:last] || false
      super @name.to_sym
  
    def caption(project=nil)
      if @caption.is_a?(Proc)
        c = @caption.call(project).to_s
        c = @name.to_s.humanize if c.blank?
        c
      else
        if @caption.nil?
          l_or_humanize(name, :prefix => 'label_')
        else
          @caption.is_a?(Symbol) ? l(@caption) : @caption
  
    def html_options(options={})
      if options[:selected]
        o = @html_options.dup
        o[:class] += ' selected'
        o
      else
        @html_options
