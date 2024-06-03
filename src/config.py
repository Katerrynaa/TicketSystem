from dataclasses import dataclass
from dotenv import load_dotenv
import os


@dataclass
class Config:
    DATABASE_URL: str


def read_config():
    load_dotenv()
    return Config(DATABASE_URL=os.environ.get("DATABASE_URL"))


@dataclass
class ConfigKey:
    SECRET_KEY: str 


def read_key_config():
    load_dotenv()
    return ConfigKey(SECRET_KEY=os.environ.get("SECRET_KEY"))




