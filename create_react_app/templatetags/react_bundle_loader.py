from django import template
from django.utils.safestring import mark_safe

from .. import utils

register = template.Library()


@register.simple_tag
def render_bundle_css():
    tags = utils.get_as_tags(extension='css')
    return mark_safe('\n'.join(tags))


@register.simple_tag
def render_bundle_js():
    tags = utils.get_as_tags(extension='js')
    return mark_safe('\n'.join(tags))
