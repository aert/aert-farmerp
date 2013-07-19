from django import template
#from ..lib.menu_manager import MenuManager

register = template.Library()


@register.inclusion_tag('aert_bookkeeping/tags/render_menu.html')
def render_menu(menu, project=None):
    #return MenuManager().render_menu(menu, project)
    return {"menu":  menu, "project": project}
