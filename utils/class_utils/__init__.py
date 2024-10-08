from importlib import import_module
from typing import Any


class ClassUtils:

    @classmethod
    def import_string(cls, dotted_path: str) -> Any:
        """通过字符串获取类

        :param dotted_path: 以“.”分隔的字符串类
        :type dotted_path: str
        :raises ImportError: 引入类失败
        :return: 类
        :rtype: Any
        """
        try:
            module_path, class_name = dotted_path.rsplit('.', 1)
        except ValueError as err:
            raise ImportError("%s doesn't look like a module path" % dotted_path) from err

        module = import_module(module_path)

        try:
            return getattr(module, class_name)
        except AttributeError as err:
            raise ImportError('Module "%s" does not define a "%s" attribute/class' % (module_path, class_name)) from err
