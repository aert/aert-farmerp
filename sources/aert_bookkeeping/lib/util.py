from django.utils.html import mark_safe, format_html, force_text
from django.utils.html import smart_urlquote
from django.forms.util import flatatt
from django.utils.translation import ugettext as _


def link_to(title, url, attrs):
    final_attrs = {'href': mark_safe(smart_urlquote(url))}
    if attrs:
        final_attrs.update(attrs)
    return format_html('<a {1}>{0}</a>', force_text(title),
                       flatatt(final_attrs))


def l_or_humanize(s, options={}):
    return _(s)
