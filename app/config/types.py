from typing import List, TypedDict


class TApp(TypedDict):
    name: str
    version: str


class TCors(TypedDict):
    origins: List[str]
    methods: List[str]
    headers: List[str]


class TAppConfig(TypedDict):
    app: TApp
    cors: TCors
