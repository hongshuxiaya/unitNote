import yaml

from main import DIR, Env


def env_config():
    user_yaml = f"{DIR}/config/env/{Env}/config.yml"
    with open(user_yaml, 'r', encoding='utf-8')as f:
        return yaml.load(f, Loader=yaml.FullLoader)


def data_config():
    data_yaml = f"{DIR}/config/data/config.yml"
    with open(data_yaml, 'r', encoding='utf-8')as f:
        return yaml.load(f, Loader=yaml.FullLoader)