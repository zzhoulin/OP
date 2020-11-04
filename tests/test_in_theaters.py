# @Author : Joy
import requests
import pytest
from utils.commlib import get_test_data

cases, list_params = get_test_data("/TestProject/OP/data/test_in_theaters")


class TestInTheaters(object):
    @pytest.mark.parametrize("case,http,expected", list(list_params), ids=cases)
    def test_in_theaters(self, case, http, expected):
        host = "http://pre.feiyuanenv.com:8830"
        r = requests.request(http["method"],
                             url=host + http["path"],
                             headers=http["headers"],
                             params=http["params"])
        response = r.json()
        assert response["body"]["totalNum"] == expected['response']["totalNum"], "实际总数是: {}".format(response["body"]["totalNum"])
