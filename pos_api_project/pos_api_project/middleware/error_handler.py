from django.http import HttpResponse
from django.conf import settings
import traceback
import pos_api_project.common.api_common as api_common

class ErrorHandlerMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        message = ""
        if exception:
                # Format your message here
                message = "**{url}**\n\n{error}\n\n````{tb}````".format(
                    url=request.build_absolute_uri(),
                    error=repr(exception),
                    tb=traceback.format_exc()
                )

        print("ErrorHandlerMiddleware " + "message " + message)

        if isinstance(exception, api_common.AuthException):
            return HttpResponse(api_common.toJson(api_common.WrapResponse(data=None, header=api_common.HeaderWrapResponse(isSuccessful=False, resultCode=403, resultMessage="Token fail!"))), content_type="application/json")

        return HttpResponse(api_common.toJson(api_common.WrapResponse(data=None, header=api_common.HeaderWrapResponse(isSuccessful=False, resultCode=500, resultMessage="Something wrong happened!"))), content_type="application/json")