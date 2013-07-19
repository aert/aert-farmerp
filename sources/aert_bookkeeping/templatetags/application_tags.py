from django import template
from django.utils.html import format_html
from ..lib.info import Info


register = template.Library()


@register.simple_tag
def link_to_user(user, fmt=None):
    if fmt is None:
        fmt = "username"

    #TODO
    if fmt == "username":
        title = "{} {}".format(user.username, user.last_name)
    elif fmt == "lastname":
        title = user.last_name
    else:  # username
        title = user.username

    href = "user/{}".format(user.username)
    return format_html("<a href='{0}'>{1}</a>", href, title)


@register.simple_tag
def link_to_appinfo():
    return format_html("<a href='{0}'>{1}</a>", Info.URL, Info.VERSIONED_NAME)


@register.simple_tag(takes_context=True)
def render_project_jump_box(context):
    user = context["user"]
    if not user.is_authenticated:
        return ""

    #TODO:
    return "render_project_jump_box"
