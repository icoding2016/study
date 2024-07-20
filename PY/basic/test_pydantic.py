from enum import Enum
from pydantic import BaseModel
from pydantic_settings import BaseSettings  #, SettingsConfigDict
from typing import Optional, List
import os


DOTENV = os.path.join(os.path.dirname(__file__), ".env")
DOTENV_PRD = os.path.join(os.path.dirname(__file__), "prd.env")
DOTENV_DEV = os.path.join(os.path.dirname(__file__), "dev.env")


class Environment(Enum):
    PRD = 'prd'
    DEV = 'dev'

ENV_FILES = {
    Environment.PRD: DOTENV_PRD,
    Environment.DEV: DOTENV_DEV,
}

class Team(BaseModel):
    member: List[str]
    lead: str

class Project(BaseModel):
    name: str
    id:  int
    owner: str
    team: Team
    repo: str


class EnvConfig(BaseSettings):
    # model_config = SettingsConfigDict(env_file='.env', env_nested_delimiter='_', extra='ignore')
    env: Environment
    class Config:
        env_file = DOTENV
        extra = 'ignore'
        env_nested_delimiter = '_'


class Configuration(BaseSettings):
    # model_config = SettingsConfigDict(env_nested_delimiter='_', extra='ignore')
    project: Project
    class Config:
        env_file = None  # Default value
        extra = 'ignore'
        env_nested_delimiter = '_'


def test_env(env:Optional[str]=None):
    cfg = None
    if not env:
        cfg = EnvConfig()
        env = cfg.env
    else:
        env = Environment(env)
    # cfg = Configuration(model_config=SettingsConfigDict(env_file=ENV_FILES[env], env_nested_delimiter='_', extra='ignore'))
    cfg = Configuration(_env_file=ENV_FILES[env])
    print(cfg.model_dump())
    print(env, cfg)
    return cfg


def test():
    cfg = test_env()    # default: prd
    assert cfg.project.repo == "https://repo-prd.fahuasi.co"
    cfg = test_env(Environment('dev'))
    assert cfg.project.repo == "https://repo-dev.fahuasi.co"


test()