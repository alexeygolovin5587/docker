from django.conf.urls import url, include
from rest_framework import routers
from sample import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^command', 'sample.views.command_view'),

    url(r'^assets-csv', 'sample.views.assets_csv_view')
]
