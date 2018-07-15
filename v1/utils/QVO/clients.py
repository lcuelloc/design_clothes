from v1.utils.QVO.base import get_params
from v1.utils.QVO.base import post_json

test_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjb21tZXJjZV9pZCI6ImNvbV9scGxzT3g3eHA4NFRzOUJ2R2NNeUxnIiwiYXBpX3Rva2VuIjp0cnVlfQ.Swf5ilRkhNS8YLGQ2La9b8E4LKB-JFUAcHq5nI4pHIw"


def new_client(email, username):
    json = {"email": email, "name": username}
    return post_json(dev=True, url="customers/", params=json, token=test_token)


def get_client(customer):
    return get_params(dev=True, url="customers/" + customer, token=test_token)
