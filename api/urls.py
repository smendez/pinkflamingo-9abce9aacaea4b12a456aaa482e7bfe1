from django.conf.urls import url, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'books', views.BookViewSet)
router.register(r'authors', views.AuthorViewSet)
router.register(r'publishers', views.PublisherViewSet)
router.register(r'ratings', views.RatingViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^authors/(?P<pk>[0-9]+)/books/$', views.AuthorBooks.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
