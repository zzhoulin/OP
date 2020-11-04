
# @Author : Joy
import requests
import yaml


def get_test_data(test_data_path):
    case = []  # 存储测试用例名称
    http = []  # 存储请求对象
    expected = []  # 存储预期结果
    with open(test_data_path, encoding='utf-8') as f:
        dat = yaml.load(f.read(), Loader=yaml.SafeLoader)
        test = dat['tests']
        for td in test:
            case.append(td.get('case', ''))
            http.append(td.get('http', {}))
            expected.append(td.get('expected', {}))
    parameters = zip(case, http, expected)
    return case, parameters


cases, parameters = get_test_data("/TestProject/OP/data/test_in_theaters")
list_params = list(parameters)


class TestInTheaters(object):
    def test_in_theaters(self):
        host = "http://pre.feiyuanenv.com:8830"
        r = requests.request(list_params[0][1]["method"],
                             url=host + list_params[0][1]["path"],
                             headers=list_params[0][1]["headers"],
                             params=list_params[0][1]["params"])
        response = r.json()
        assert response["body"]["totalNum"] == list_params[0][2]['response']["totalNum"]
