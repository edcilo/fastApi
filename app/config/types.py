from typing import List, TypedDict
from pydantic import BaseSettings, BaseModel


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


class TSqLiteConfig(TypedDict):
    location: str


class TSqlConfig(TypedDict):
    host: str
    port: int
    database: str
    username: str
    password: str


class TConnectionsConfig(TypedDict):
    sqlite: TSqLiteConfig
    psql: TSqlConfig


class TDbConfig(TypedDict):
    default: str
    connections: TConnectionsConfig


class TConfig(TypedDict):
    app: TAppConfig
    db: TDbConfig


class AppSettingsSchema(BaseModel):
    name: str
    version: str


class CorsSchema(BaseModel):
    origins: list[str]
    methods: list[str]
    headers: list[str]


class AppSchema(BaseModel):
    app: AppSettingsSchema
    cors: CorsSchema


class SqliteSchema(BaseModel):
    location: str


class SQLSchema(BaseModel):
    host: str
    port: int
    database: str
    username: str
    password: str


class MySQLSchema(BaseModel):
    host: str
    port: int
    database: str
    username: str
    password: str


class EnginesSchema(BaseModel):
    sqlite: SqliteSchema
    psql: SQLSchema
    mysql: MySQLSchema


class DBSchema(BaseModel):
    default: str
    connections: EnginesSchema
