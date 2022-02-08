import json
import os
from io import open


from .exception import (
    WebpackError,
    WebpackLoaderBadStatsError,
    WebpackLoaderTimeoutError,
    WebpackBundleLookupError
)

import requests


class CreateReactLoader(object):
    asset_file = 'asset-manifest.json'

    def __init__(self, config, manifest_path=None):
        self.config = config
        self.manifest_file_path = manifest_path

    @property
    def is_dev(self):
        return self.config.get("IS_DEV", False)

    def get_dev_path(self):
        dev_asset_path = self.config['FRONT_END_SERVER']
        public_path_dev = self.config.get("PUBLIC_PATH_DEV")
        if public_path_dev != "/":
            dev_asset_path = public_path_dev

        return dev_asset_path.strip('/') + "/"

    @property
    def asset_path(self):
        public_path = self.config.get("PUBLIC_PATH")
        if self.is_dev:
            return self.get_dev_path()
        return public_path

    @property
    def manifest_path(self):
        dev_asset_path = self.config['FRONT_END_SERVER']
        return dev_asset_path.strip('/') + "/"

    def get_dev_assets(self):
        server = self.manifest_path
        url = "{frontend_server}{asset_file}".format(frontend_server=server, asset_file=self.asset_file)
        try:
            data = requests.get(url, timeout=3)
        except:
            raise IOError(
                'Error reading {0}. Are you sure webpack has been started please check yarn start')

        return data.json()

    def get_prod_assets(self):
        try:
            build_folder = self.config['BUNDLE_DIR_NAME']
            if self.manifest_file_path:
                manifest_file = self.manifest_file_path
            else:
                manifest_file = os.path.join(build_folder, self.asset_file)
            with open(manifest_file, encoding="utf-8") as f:
                return json.load(f)
        except IOError:
            raise IOError(
                'Are you sure webpack has generated '
                'the asset-manifest file in the build directory and the path is correct?')

    def get_assets(self):
        if self.is_dev and not self.manifest_file_path:
            return self.get_dev_assets()
        return self.get_prod_assets()

    def get_bundle(self):
        assets = self.get_assets()
        if assets:
            chunks = assets['entrypoints']
            return chunks

    def get_pages(self):
        pages = self.get_assets()
        if pages:
            chunks = pages.get('pages', {})
            return chunks
