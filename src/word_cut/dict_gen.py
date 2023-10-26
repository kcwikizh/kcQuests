import json
import os.path

_local = os.path.dirname(__file__)


def equip_dict_gen(path):
    item_list = []
    with open(path) as f:
        items = json.loads(f.read())
        for item in items:
            item_list.append(f'{item["chinese_name"] if item["chinese_name"] is not None else item["name"]} n \n')
    with open(os.path.join(_local, 'dict.txt'), 'w') as f:
        f.writelines(item_list)
