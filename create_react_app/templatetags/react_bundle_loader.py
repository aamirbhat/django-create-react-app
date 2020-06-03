from django import template
from django.utils.safestring import mark_safe

from .. import utils

register = template.Library()


@register.simple_tag
def render_bundle_css(config="DEFAULT"):
    tags = utils.get_as_tags(extension='css', config=config)
    return mark_safe('\n'.join(tags))


@register.simple_tag
def render_bundle_js(config="DEFAULT"):
    tags = utils.get_as_tags(extension='js', config=config)
    return mark_safe('\n'.join(tags))
