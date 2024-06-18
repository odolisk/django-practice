from django.urls import include, path

from tastypie.api import Api

from api.models import CategoryResource, CourseResource


api = Api(api_name='vs4')
api.register(CategoryResource())
api.register(CourseResource())

urlpatterns = [
    path('', include(api.urls), name='index'),
]
