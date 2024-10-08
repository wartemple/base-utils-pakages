from dataclasses import dataclass
from io import BytesIO
from .yaml_utils import YamlUtils


@dataclass
class FileTypes:
    TXT = 'txt'
    YAML = 'yaml'
    EXCEL = 'excel'


def save_data(data, type):
    if type == FileTypes.YAML:
        return YamlUtils.write(data)


def bytes_to_file(bytes: BytesIO, file_path) -> str:
    with open(file_path, mode='wb') as f_out:
        f_out.write(bytes.getbuffer())
    return file_path


