import allure
# from test_data.user_api.news_api_data import *
from test_data.user_api.gorest_api_data import response_get_all_comments


@allure.step('get_all_post')
def test_o3_gorest_all_comments():
    response_body, status_code = response_get_all_comments()
    print(response_body)
    print(status_code)
    assert status_code == 200
    assert type(response_body[0]["id"]) == int
    print(response_body[0]["id"])
    assert type(response_body[0]["post_id"]) == int
    print(response_body[0]["post_id"])
    assert type(response_body[0]["name"]) == str
    print(response_body[0]["name"])
    assert type(response_body[0]["email"]) == str
    print(response_body[0]["email"])
    assert type(response_body[0]["body"]) == str
    print(response_body[0]["body"])

