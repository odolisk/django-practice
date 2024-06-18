from tastypie.authorization import Authorization
from tastypie.resources import ModelResource

from shop.models import Category, Course

from .authentication import CustomAuthentication


class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'categories'
        allowed_methods = ('get',)


class CourseResource(ModelResource):
    class Meta:
        queryset = Course.objects.all()
        resource_name = 'courses'
        allowed_method = ('get', 'post', 'delete',)
        excludes = ('created_at', 'comments_qty',)
        authentication = CustomAuthentication()
        authorization = Authorization()

    def hydrate(self, bundle):
        bundle.obj.category_id = bundle.data['category_id']
        return super().hydrate(bundle)

    def dehydrate(self, bundle):
        bundle.data['category'] = bundle.obj.category
        return super().dehydrate(bundle)

    def dehydrate_title(self, bundle):
        return bundle.data['title'].lower()

    def dehydrate_price(self, bundle):
        return f'${bundle.data['price']}'
