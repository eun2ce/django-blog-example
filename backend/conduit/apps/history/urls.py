from django.conf.urls import include, url

from rest_framework.routers import DefaultRouter

from .views import HistoryViewSet, ArticleHistoryAPIView

router = DefaultRouter(trailing_slash=False)
router.register(r'history', HistoryViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),

    url(r'^history/(?P<article_slug>[-\w]+)/?$', ArticleHistoryAPIView.as_view()),
]
