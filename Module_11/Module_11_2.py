import inspect
import pprint
from Module_10 import Module_10_4

class TestClass:
    test_atr = 1
    pass

def introspection_info(obj):
    result = dict()
    name_list = (dir(obj)).copy()
    attributes_list = list()
    methods_list = list()

    for attr_name in dir(obj):
        if attr_name.startswith('__') and attr_name.endswith('__'):
            methods_list.append(attr_name)
            name_list.remove(attr_name)
    #print(name_list)

    for attr_name in name_list:
        attr = getattr(obj, attr_name)
        print(attr_name, type(attr))
        if type(attr) in [int, str, float, list, dict, bool, set, tuple]:
            attributes_list.append(attr_name)

    result['type'] = type(obj)
    result['attributes'] = attributes_list
    result['methods'] = methods_list
    result['module'] = inspect.getmodule(obj)

    return result

test_obj = TestClass
pprint.pp(introspection_info(test_obj))