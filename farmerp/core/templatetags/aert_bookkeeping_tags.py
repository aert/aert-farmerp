from django import template
#from ..lib.menu_manager import MenuManager

register = template.Library()


@register.inclusion_tag('core/tags/render_menu.html')
def render_menu(menu, project=None):
    #return MenuManager().render_menu(menu, project)
    return {"menu":  menu, "project": project}


@register.inclusion_tag('core/tags/render_main_menu.html')
def render_main_menu(project=None):
    return {"project": project}


@register.simple_tag(takes_context=True)
def render_flash_messages(context):
    return "render_flash_messages"
