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


@register.simple_tag
def render_bundle_page_css(page_name="main", config="DEFAULT"):
    tags = utils.get_tags_per_page(extension='css', page_name=page_name, config=config)
    return mark_safe('\n'.join(tags))


@register.simple_tag
def render_bundle_page_js(page_name="main", config="DEFAULT"):
    tags = utils.get_tags_per_page(extension='js', page_name=page_name, config=config)
    return mark_safe('\n'.join(tags))
