from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins


# class QueryModelViewSet(mixins.RetrieveModelMixin, GenericViewSet):
#     pass

class QueryModelViewSet(mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        GenericViewSet
                        ):
    pass
