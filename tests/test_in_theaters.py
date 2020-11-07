# @Author : Joy
import requests
import pytest
from utils.commlib import get_test_data

cases, list_params = get_test_data("/TestProject/OP/data/test_in_theaters")


class TestInTheaters(object):
    @pytest.mark.parametrize("case,http,expected", list(list_params), ids=cases)
    def test_in_theaters(self, env, case, http, expected):
        r = requests.request(http["method"],
                             url=env["host"]["pre"] + http["path"],
                             headers=http["headers"],
                             params=http["params"])
        response = r.json()
        assert response["body"]["totalNum"] == expected['response']["body"]["totalNum"]

    @pytest.fixture(scope="function")
    def preparation(self):
        print("在数据库中准备测试数据")
        test_data = "在数据库中准备测试数据"
        yield test_data
        print("清理测试数据")