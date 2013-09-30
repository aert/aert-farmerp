from django import template
from django.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static

register = template.Library()


def current_theme():
    return settings.THEME_NAME


class ThemeAssetNode(template.Node):
    def __init__(self, static_url):
        self.static_url = static_url

    def render(self, context):
        path = "themes/" + current_theme() + "/" + self.static_url
        return static(path)


def get_theme_asset(parser, token, asset_type):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, param_static_url = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError(
            "%r tag requires a single argument" % token.contents.split()[0])
    if not (param_static_url[0] == param_static_url[-1]
            and param_static_url[0] in ('"', "'")):
        raise template.TemplateSyntaxError(
            "%r tag's argument should be in quotes" % tag_name)
    return ThemeAssetNode(asset_type + "/" + param_static_url[1:-1])


@register.tag('aert_theme_js')
def do_aert_theme_js(parser, token):
    return get_theme_asset(parser, token, 'javascripts')


@register.tag('aert_theme_css')
def do_aert_theme_css(parser, token):
    return get_theme_asset(parser, token, 'stylesheets')


@register.tag('aert_theme_img')
def do_aert_theme_img(parser, token):
    return get_theme_asset(parser, token, 'images')
