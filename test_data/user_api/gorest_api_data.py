from test_data.api_end_point import *
from test_data.common_data import data_from_server
from test_data.headers import headers_post


# from test_data.payloads import *


def response_get_all_users():
    res = data_from_server("GET", get_all_users)
    return res.json(), res.status_code


def response_get_all_posts():
    res = data_from_server("GET", get_all_post)
    return res.json(), res.status_code


def response_get_all_comments():
    res = data_from_server("GET", get_all_comments)
    return res.json(), res.status_code


def response_get_all_todos():
    res = data_from_server("GET", get_all_todos)
    return res.json(), res.status_code


def response_get_code_null():
    res = data_from_server("GET", get_code_null)
    return res.json(), res.status_code
