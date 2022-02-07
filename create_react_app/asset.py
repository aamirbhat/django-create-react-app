from create_react_app.config import get_loader
from create_react_app.utils import _page_bundle, _filter_by_extension


class AssetTag:
    def __init__(self, public_path):
        self.public_path = public_path

    def css_tag(self, asset_path, attrib=""):
        return '<link type="text/css" href="{0}{1}" rel="stylesheet" {2}/>'.format(self.public_path, asset_path, attrib)

    def script_tag(self, asset_path, attrib=""):
        return '<script type="text/javascript" src="{0}{1}" {2}></script>'.format(self.public_path, asset_path, attrib)


class AssetManager:
    def __init__(self, config_name):
        self.loader = get_loader(config_name)
        self.asset = AssetTag(self.loader.asset_path)

    def get_bundle(self, extension):
        bundle = self.loader.get_bundle()
        if extension:
            bundle = _filter_by_extension(bundle, extension)
        if not bundle:
            return []
        return bundle

    def get_tag_bundle(self, extension, ends_with=[]):
        tags = []
        bundle = self.get_bundle(extension=extension)
        for chunk in bundle:
            if not self.loader.is_dev:
                chunk = chunk.replace("static/", "")

            if chunk.endswith(tuple(ends_with)):
                tags.append(self.asset.script_tag(chunk))
        return tags

    def css_bundle(self):
        return self.get_tag_bundle(extension="css", ends_with=['.css', '.css.gz'])

    def js_bundle(self):
        return self.get_tag_bundle(extension="js", ends_with=['.js', '.js.gz'])
