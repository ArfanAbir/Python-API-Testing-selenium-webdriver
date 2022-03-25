import allure
# from test_data.user_api.news_api_data import *
from test_data.user_api.gorest_api_data import response_get_all_users


@allure.step('get_all_users')
def test_o1_apple_all_users():
    response_body, status_code = response_get_all_users()
    print(response_body)
    print(status_code)
    assert status_code == 200
    assert type(response_body[0]["id"]) == int
    assert type(response_body[0]["name"]) == str
    print(response_body[0]["name"])
    assert type(response_body[0]["email"]) == str
    print(response_body[0]["email"])
    assert type(response_body[0]["gender"]) == str
    print(response_body[0]["gender"])
    assert type(response_body[0]["status"]) == str
    print(response_body[0]["status"])

