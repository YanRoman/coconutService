from rest_framework.response import Response
from rest_framework.views import APIView
from .model.ml_model import MLModel


class BaseView(APIView):
    def get(self, request):
        ml_model = MLModel()
        return Response({"msg": ml_model.do()})
