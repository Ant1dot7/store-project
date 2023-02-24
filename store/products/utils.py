from django.db.models import Count

from .models import *


class DataMixin:
    paginate_by = 5

    def get_user_context(self, **kwargs):
        context = kwargs
        context['categories'] = ProductCategory.objects.annotate(Count('product'))
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
