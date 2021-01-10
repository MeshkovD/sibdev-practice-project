from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from apps.test.models import Test
from apps.test.serializers import TestSerializer


class TestViewSet(
    CreateModelMixin,
    RetrieveModelMixin,
    ListModelMixin,
    GenericViewSet
):
    serializer_class = TestSerializer
    queryset = Test.objects.all()
