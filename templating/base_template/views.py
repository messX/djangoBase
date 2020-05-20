from rest_framework import viewsets
from rest_framework.mixins import DestroyModelMixin

from templating.generics.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin
from templating.generics.viewsets import GenericAPIView


class GenericViewSet(GenericAPIView,
                     viewsets.GenericViewSet):
    pass


class ModelViewSet(CreateModelMixin,
                   RetrieveModelMixin,
                   UpdateModelMixin,
                   DestroyModelMixin,
                   ListModelMixin,
                   GenericViewSet):
    pass


class ReadOnlyModelViewSet(RetrieveModelMixin,
                           ListModelMixin,
                           GenericViewSet):
    pass