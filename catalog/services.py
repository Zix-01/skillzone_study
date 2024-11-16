from django.core.cache import cache

from catalog.models import Category
from config.settings import CACHES_ENABLED


def get_categories():
    if not CACHES_ENABLED:
        return Category.objects.all()
    key = 'categories'
    categories_cache = cache.get(key)
    if categories_cache is not None:
        return categories_cache

    categories_cache = Category.objects.all()
    cache.set(key, categories_cache)
    return categories_cache

