from django import template

register = template.Library()

@register.filter
def default_logo_url(provider_name):
    """Returns the default logo URL for a social provider."""
    logos = {
        'facebook': 'https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg',
        'instagram': 'https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png',
    }
    return logos.get(provider_name, 'https://via.placeholder.com/30')
