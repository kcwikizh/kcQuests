import json

from src.kcwiki.constants import WT_FILTERS
from src.kcwiki.helper import filter_text


class Quest:

    def __init__(self, name=None, id=None, code=None, memo=None, memo2=None, desc=None, pre=None):
        if pre is None:
            pre = []
        self.name = name
        self.id = id
        self.code = code
        self.memo = memo
        self.memo2 = memo2
        self.desc = desc
        self.pre = pre

    def __repr__(self):
        return f"Quest(name={self.name}, id={self.id}, code={self.code}, memo={self.memo}, memo2={self.memo2}, desc={self.desc}, pre={self.pre})"

    def to_json(self):
        return json.dumps(self.__dict__, ensure_ascii=False)

    def to_dict(self):
        return {
            self.id: self.__dict__
        }

    def to_dict_without_id(self):
        return {
            self.id: {
                i: self.__dict__[i] if i != 'memo' else f'奖励:{self.__dict__[i]}' for i in self.__dict__.keys() if i != 'id'
            }
        }

    @classmethod
    def from_json(cls, json_data):
        data = json.loads(json_data)
        return cls(**data)

    @classmethod
    def from_wt_template(cls, template, items):
        quest = cls()
        quest.id = template.comments[0].contents.strip()
        for arg in template.arguments:
            name = arg.name.strip()
            value = arg.value.strip()
            if name == '编号':
                quest.code = value
            if name.startswith('前置') and value:
                quest.pre.append(value)
            if name == '中文任务名字':
                quest.name = filter_text(value, WT_FILTERS)
            if name == '中文任务说明':
                quest.desc = filter_text(value, WT_FILTERS)
            if name == '奖励':
                for i in arg.templates:
                    if i.name.strip().startswith('装备奖励'):
                        for _ in i.arguments:
                            if _.name.strip().startswith('编号'):
                                value = value.replace(i.string, items[int(_.value.strip())])
                for link in arg.wikilinks:
                    if '|' in link:
                        link_items = link.text.split('|')
                        for link_item in link_items:
                            if 'link=' in link_item:
                                link_name = link_item.replace('link=', '')
                                value = value.replace(link.string, f'「{link_name}」')
                quest.memo = filter_text(value, WT_FILTERS)
            if name == '备注':
                quest.memo2 = filter_text(value, WT_FILTERS)
        return quest
