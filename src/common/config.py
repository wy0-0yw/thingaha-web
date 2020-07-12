import os

import yaml


def load_config() -> dict:
    """
    load conf based on environment
    :return:
    """
    env = "dev"
    if os.environ.get("SCRIPT_ENV") == "production":
        env = "prod"
    elif os.environ.get("SCRIPT_ENV") == "staging":
        env = "staging"
    with open("../conf/config_%s.yaml" % env, "r", encoding="utf-8") as conf_f:
        conf = yaml.safe_load(conf_f)
    return conf
