from . import product_repo
import pos_api_project.common.api_common as api_common
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse, HttpRequest

@require_http_methods(["GET"])
def products(request: HttpRequest) -> HttpResponse:
    data = product_repo.getCategoryListWithProduct()
    return api_common.toWrapResponse(data=data)