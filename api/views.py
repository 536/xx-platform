import json

from django.conf import settings
from django.http import JsonResponse
from django.views import View

from .response import error, success


class Index(View):
    def get(self, request):
        return JsonResponse(success())

    def post(self, request):
        if request.META['REMOTE_ADDR'] in settings.ALLOWED_REMOTE_ADDRESSES:
            try:
                data: dict = json.loads(request.body)
            except json.JSONDecodeError:
                data: dict = {}
            return JsonResponse(success(result=dict(data)))
        return JsonResponse(error(1, result=dict(data)))
