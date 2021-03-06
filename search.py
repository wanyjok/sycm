# -*- coding: utf-8 -*-
# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = search_from_dict(json.loads(json_string))

from typing import Any, List, TypeVar, Type, cast, Callable


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


class Keyword:
    value: str

    def __init__(self, value: str) -> None:
        self.value = value

    @staticmethod
    def from_dict(obj: Any) -> 'Keyword':
        assert isinstance(obj, dict)
        value = from_str(obj.get("value"))
        return Keyword(value)

    def to_dict(self) -> dict:
        result: dict = {}
        result["value"] = from_str(self.value)
        return result


class Uv:
    value: int

    def __init__(self, value: int) -> None:
        self.value = value

    @staticmethod
    def from_dict(obj: Any) -> 'Uv':
        assert isinstance(obj, dict)
        value = from_int(obj.get("value"))
        return Uv(value)

    def to_dict(self) -> dict:
        result: dict = {}
        result["value"] = from_int(self.value)
        return result


class Rival:
    uv: Uv
    keyword: Keyword

    def __init__(self, uv: Uv, keyword: Keyword) -> None:
        self.uv = uv
        self.keyword = keyword

    @staticmethod
    def from_dict(obj: Any) -> 'Rival':
        assert isinstance(obj, dict)
        uv = Uv.from_dict(obj.get("uv"))
        keyword = Keyword.from_dict(obj.get("keyword"))
        return Rival(uv, keyword)

    def to_dict(self) -> dict:
        result: dict = {}
        result["uv"] = to_class(Uv, self.uv)
        result["keyword"] = to_class(Keyword, self.keyword)
        return result


class Data:
    rival1: List[Rival]
    rival2: List[Rival]

    def __init__(self, rival1: List[Rival], rival2: List[Rival]) -> None:
        self.rival1 = rival1
        self.rival2 = rival2

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        rival1 = from_list(Rival.from_dict, obj.get("rival1"))
        rival2 = from_list(Rival.from_dict, obj.get("rival2"))
        return Data(rival1, rival2)

    def to_dict(self) -> dict:
        result: dict = {}
        result["rival1"] = from_list(lambda x: to_class(Rival, x), self.rival1)
        result["rival2"] = from_list(lambda x: to_class(Rival, x), self.rival2)
        return result


class Search:
    trace_id: str
    code: int
    data: Data
    message: str

    def __init__(self, trace_id: str, code: int, data: Data, message: str) -> None:
        self.trace_id = trace_id
        self.code = code
        self.data = data
        self.message = message

    @staticmethod
    def from_dict(obj: Any) -> 'Search':
        assert isinstance(obj, dict)
        trace_id = from_str(obj.get("traceId"))
        code = from_int(obj.get("code"))
        data = Data.from_dict(obj.get("data"))
        message = from_str(obj.get("message"))
        return Search(trace_id, code, data, message)

    def to_dict(self) -> dict:
        result: dict = {}
        result["traceId"] = from_str(self.trace_id)
        result["code"] = from_int(self.code)
        result["data"] = to_class(Data, self.data)
        result["message"] = from_str(self.message)
        return result


def search_from_dict(s: Any) -> Search:
    return Search.from_dict(s)


def search_to_dict(x: Search) -> Any:
    return to_class(Search, x)

