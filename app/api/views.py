import json

from django.conf import settings
from django.http import HttpRequest, JsonResponse
from django.views import View

from .models import Parlance
from .utils.response import error, success


class IndexView(View):
    def get(self, request: HttpRequest):
        return JsonResponse(success())

    def post(self, request: HttpRequest):
        if request.META["REMOTE_ADDR"] in settings.ALLOWED_REMOTE_ADDRESSES:
            try:
                data: dict = json.loads(request.body)
            except json.JSONDecodeError:
                data: dict = {}
            return JsonResponse(success(result=dict(data)))
        return JsonResponse(error(1, result=dict(data)))


class ParlanceView(View):
    def get(self, request: HttpRequest):
        return JsonResponse(
            success(
                result=[
                    dict(
                        id=term.id,
                        abbr=term.abbr,
                        desc=term.desc,
                        zh=term.zh,
                        en=term.en,
                    )
                    for term in Parlance.objects.all()
                ]
            )
        )

    def post(self, request: HttpRequest):
        try:
            d = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse(error())

        term = Parlance.objects.create(**d)
        return JsonResponse(
            success(
                result={
                    "id": term.id,
                    "abbr": term.abbr,
                    "desc": term.desc,
                    "zh": term.zh,
                    "en": term.en,
                }
            )
        )

    def put(self, request: HttpRequest):
        d: dict = json.loads(request.body)
        if "id" in d:
            _id = d.pop("id")
            Parlance.objects.filter(id=_id).update(**d)
        else:
            Parlance.objects.update(**d)

        return JsonResponse(success())

    def delete(self, request: HttpRequest):
        d: dict = json.loads(request.body)
        if "id" in d:
            _id = d.pop("id")
            Parlance.objects.filter(id=_id).delete()
        else:
            Parlance.objects.filter(**d).delete()

        return JsonResponse(success())
