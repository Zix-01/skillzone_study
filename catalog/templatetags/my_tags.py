from django import template

register = template.Library()

@register.filter()
def media_path(path):
    if path and not path.startswith('media/'):
        return f'media/{path}' if not path.startswith('media/') else path
    return path or '#'


