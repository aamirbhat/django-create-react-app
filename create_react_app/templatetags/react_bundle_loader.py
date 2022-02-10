from django import template
from django.utils.safestring import mark_safe
from ..asset import AssetManager, SrcAssetManager

register = template.Library()


@register.simple_tag
def render_bundle_css(config="DEFAULT", is_preload=False, attrib=''):
    tags = AssetManager(config).css_tags(is_preload=is_preload, attrib=attrib)
    return mark_safe('\n'.join(tags))


@register.simple_tag
def render_bundle_js(config="DEFAULT", is_preload=False, attrib=''):
    tags = AssetManager(config).js_tags(is_preload=is_preload, attrib=attrib)
    return mark_safe('\n'.join(tags))


@register.simple_tag
def render_bundle_src_css(config="DEFAULT"):
    tags = SrcAssetManager(config).css_tags()
    return tags


@register.simple_tag
def render_bundle_src_js(config="DEFAULT"):
    tags = SrcAssetManager(config).js_tags()
    return tags
