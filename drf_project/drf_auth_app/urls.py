from django.conf.urls import url, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='API')


router = DefaultRouter()
router.register(r'categories', views.CategoryListView)
router.register(r'post', views.PostListView)
router.register(r'users', views.UserListView)

urlpatterns = [
    url(r'article/api/', include(router.urls)),
    url(r'docs/$', schema_view),
    url(r'get_auth_token/', obtain_auth_token, name='get_auth_token'),
]
