from .base_io_utils import BaseIOUtils
from typing import Any
from io import BytesIO
import re
import os
from contextlib import suppress

import yaml
from ruamel.yaml import YAML

from class_utils import ClassUtils


class Loader(yaml.SafeLoader):
    pattern = re.compile(r'.*?(\${(\w+)\|?(.*?)}).*?')
    loader = yaml.SafeLoader

    def __init__(self, stream: Any):
        self._root = os.path.split(stream.name)[0]
        super(Loader, self).__init__(stream)
        Loader.add_constructor('!include', Loader.include)
        Loader.add_constructor('!env', Loader.env)
        Loader.add_constructor('!class', Loader.class_constructor)
        Loader.add_constructor('!regex', Loader.regex)

    def include(self, node: Any) -> Any:
        filename = os.path.join(self._root, str(self.construct_scalar(node)))
        with open(filename, 'r', encoding='utf-8') as fin:
            return yaml.load(fin, self.__class__)

    def env(self, node: Any) -> Any:
        value = self.construct_scalar(node)
        match = self.pattern.findall(str(value))
        if match:
            full_value = str(value)
            for item in match:
                (raw, key, default) = item
                default = default if default else key
                full_value = full_value.replace(f'{raw}', os.environ.get(key, default))
            with suppress(Exception):
                return int(full_value)
            return full_value
        return value

    def class_constructor(self, node: Any) -> Any:
        value = self.construct_scalar(node)
        return ClassUtils.import_string(str(value))

    def regex(self, node: Any) -> Any:
        value = self.construct_scalar(node)
        return re.compile(str(value)[1:-1])



class YamlUtils(BaseIOUtils):
    
    @classmethod
    def read(cls, file_path):
        with open(file_path, 'r', encoding='utf-8') as fin:
            return yaml.load(fin, Loader)


    @classmethod
    def write(cls, data):
        dumper = YAML()
        dumper.width = 4096
        dumper.representer.add_representer(type(None), lambda self, _: self.represent_scalar("tag:yaml.org,2002:null", "null"))
        buffer = BytesIO()
        dumper.dump(data, buffer)
        return buffer
