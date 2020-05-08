import json
import os
import time
from io import open

from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage

from .exception import (
    WebpackError,
    WebpackLoaderBadStatsError,
    WebpackLoaderTimeoutError,
    WebpackBundleLookupError
)

import requests


class CreateReactLoader(object):
    asset_file = 'asset-manifest.json'

    def __init__(self, config):
        self.config = config
        self.is_dev = self.config.get("is_dev", False)

    @property
    def asset_path(self):
        if self.is_dev:
            return self.config['FRONT_END_SERVER'].strip('/') + "/"
        return ""

    def get_dev_assets(self):
        server = self.asset_path
        url = "{frontend_server}{asset_file}".format(frontend_server=server, asset_file=self.asset_file)
        data = requests.get(url)
        return data.json()

    def get_prod_assets(self):
        try:
            build_folder = self.config['BUNDLE_DIR_NAME']
            manifest_file = os.path.join(build_folder, self.asset_file)
            with open(manifest_file, encoding="utf-8") as f:
                return json.load(f)
        except IOError:
            raise IOError(
                'Error reading {0}. Are you sure webpack has generated '
                'the file and the path is correct?'.format(
                    self.config['STATS_FILE']))

    def get_assets(self):
        if self.is_dev:
            return self.get_dev_assets()
        return self.get_prod_assets()

    def get_bundle(self):
        assets = self.get_assets()
        if assets:
            chunks = assets['entrypoints']
            return chunks
