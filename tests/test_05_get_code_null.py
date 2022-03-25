import allure
# from test_data.user_api.news_api_data import *
from test_data.user_api.gorest_api_data import response_get_code_null


@allure.step('get_all_post')
def test_o5_gorest_null_code():
    response_body, status_code = response_get_code_null()
    print(response_body)
    print(status_code)
    assert status_code == 200

