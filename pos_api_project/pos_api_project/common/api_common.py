from django.http import HttpResponse
import json
from datetime import date, datetime

class HeaderWrapResponse:
    def __init__(self, isSuccessful: bool, resultCode: int, resultMessage: str):
        self.isSuccessful = isSuccessful
        self.resultCode = resultCode
        self.resultMessage = resultMessage

class WrapResponse:
    def __init__(self, header: HeaderWrapResponse, data):
        self.header = header
        self.data = data


def obj_to_dict(obj):

    if isinstance(obj, (datetime)):
        return '{:%Y-%m-%d %H:%M:%S}'.format(obj)

    if isinstance(obj, (date)):
        return '{:%Y-%m-%d}'.format(obj)
    return obj.__dict__


def toJson(obj):
    return json.dumps(obj=obj, default=obj_to_dict, ensure_ascii=False).encode('utf8')

def toWrapResponse(data) -> HttpResponse:
    return HttpResponse(toJson(WrapResponse(data=data, header=HeaderWrapResponse(isSuccessful=True, resultCode=0, resultMessage=""))), content_type="application/json")

class AuthException(Exception):
    pass