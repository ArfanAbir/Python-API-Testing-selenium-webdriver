import allure
# from test_data.user_api.news_api_data import *
from test_data.user_api.gorest_api_data import response_get_all_todos


@allure.step('get_all_post')
def test_o4_gorest_all_todos():
    response_body, status_code = response_get_all_todos()
    print(response_body)
    print(status_code)
    assert status_code == 200
    assert type(response_body[0]["id"]) == int
    print(response_body[0]["id"])
    assert type(response_body[0]["user_id"]) == int
    print(response_body[0]["user_id"])
    assert type(response_body[0]["title"]) == str
    print(response_body[0]["title"])
    assert type(response_body[0]["due_on"]) == str
    print(response_body[0]["due_on"])
    assert type(response_body[0]["status"]) == str
    print(response_body[0]["status"])

