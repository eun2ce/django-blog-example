from rest_framework import generics, mixins, status, viewsets
from rest_framework.exceptions import NotFound
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import (
    AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
)
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import History
from .renderers import HistoryJSONRenderer
from .serializers import HistorySerializer


class HistoryViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    lookup_field = 'slug'
    queryset = History.objects.select_related('slug', 'slug')
    permission_classes = (IsAuthenticatedOrReadOnly,)
    renderer_classes = (HistoryJSONRenderer,)
    serializer_class = HistorySerializer

    def get_queryset(self):
        queryset = self.queryset

        author = self.request.query_params.get('author', None)
        if author is not None:
            queryset = queryset.filter(author__user__username=author)

        slug = self.request.query_params.get('slug', None)
        if slug is not None:
            queryset = queryset.filter(slug=slug)

        return queryset

    def create(self, request):
        serializer_context = {
            'author': request.user.profile,
            'request': request
        }
        serializer_data = request.data.get('history', {})

        serializer = self.serializer_class(
            data=serializer_data, context=serializer_context
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        serializer_context = {'request': request}
        page = self.paginate_queryset(self.get_queryset())

        serializer = self.serializer_class(
            page,
            context=serializer_context,
            many=True
        )

        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, slug):
        serializer_context = {'request': request}

        try:
            serializer_instance = self.queryset.get(slug=slug)
        except History.DoesNotExist:
            raise NotFound('An article history with this slug does not exist.')

        serializer = self.serializer_class(
            serializer_instance,
            context=serializer_context
        )

        return Response(serializer.data, status=status.HTTP_200_OK)


class ArticleHistoryAPIView(RetrieveAPIView):
    lookup_field = 'slug'
    queryset = History.objects.select_related('slug', 'slug')
    permission_classes = (IsAuthenticatedOrReadOnly,)
    renderer_classes = (HistoryJSONRenderer,)
    serializer_class = HistorySerializer

    def retrieve(self, request, article_slug, *args, **kwargs):
        # Try to retrieve the requested profile and throw an exception if the
        # profile could not be found.
        print('article slug' + article_slug)
        try:
            history = self.queryset.get(slug=article_slug)
        except History.DoesNotExist:
            raise NotFound('A profile with this username does not exist.')

        serializer = self.serializer_class(history, context={
            'request': request
        })

        return Response(serializer.data, status=status.HTTP_200_OK)