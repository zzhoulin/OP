# -*- coding: utf-8 -*-
# @Author : Joy
import pytest
import os
import yaml


# 接收命令行参数
def pytest_addoption(parser):
    parser.addoption("--env",
                     action="store",
                     dest="environment",
                     default="Pre",
                     help="environment: Pre or Pro")

# 读取host
@pytest.fixture(scope="session")
def env(request):
    config_path = os.path.join(request.config.rootdir,
                               "config",
                               request.config.getoption("environment"),
                               "config.yaml")
    with open(config_path) as f:
        env_config = yaml.load(f.read(), Loader=yaml.SafeLoader)
    return env_config
