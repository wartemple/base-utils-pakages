from .base_io_utils import BaseIOUtils
from collections import OrderedDict
from pathlib import Path
from typing import Any, Dict, List, Union
from io import BytesIO
import json
from ruamel.yaml import YAML, RoundTripRepresenter, YAMLError, add_representer
from ruamel.yaml.constructor import DuplicateKeyError


class YamlUtils(BaseIOUtils):
    
    @classmethod
    def read(cls, file_path):
        pass

    @classmethod
    def write(cls, data):
        dumper = YAML()
        dumper.width = 4096
        # use `null` to represent `None`
        dumper.representer.add_representer(
            type(None),
            lambda self, _: self.represent_scalar("tag:yaml.org,2002:null", "null"))
        buffer = BytesIO()
        dumper.dump(data, buffer)
        return buffer
