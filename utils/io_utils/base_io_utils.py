from abc import ABC, abstractclassmethod
from io import BytesIO
from typing import Any


class BaseIOUtils(ABC):

    @abstractclassmethod
    def write(cls, data) -> BytesIO:
        pass

    @abstractclassmethod
    def read(cls, file_path) -> Any:
        pass