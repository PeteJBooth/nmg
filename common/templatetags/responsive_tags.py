from django import template
from django.conf import settings

# ----------------------------------------------------------------------------

register = template.Library()


@register.inclusion_tag('common/responsive_image.html')
def responsive_image(image, thumbnail_category, small_alias, *args, **kwargs):
    """"Generates the boilerplate needed for responsive image creation.
    Args:
    - image: an image instance.
    - thumbnail_category: A dict of thumbnail aliases from  the THUMBNAIL_ALIASES setting.
        The default (typcially largest) alias is the last in the dict.
    - small_alias: the smallest thumbnail alias to be used.

    After that, we need an even number of extra args, which correspond to the
    different sizes:
    - breakpoint: the dimension at which a new size is activated.
    - alias: the name of the thumbnail alias to activate.
    ...etc...

    Kwargs:
    - alt: 'alt' tag to display on image.

    """
    assert len(args) % 2 == 0, 'Number of sizing args must be even'

    assert thumbnail_category in settings.THUMBNAIL_ALIASES, 'Thumbnail category not found'

    aliases = settings.THUMBNAIL_ALIASES[thumbnail_category]
    breakpoint_data = []
    args = [i for i in args]
    while len(args) > 0:
        breakpoint = args.pop(0)
        alias = args.pop(0)
        breakpoint_data.append((breakpoint, aliases[alias]))
    default_image_alias = aliases[alias] #default alias is the last (largest) thumbnail
    small_image_alias = aliases[small_alias]
    alt = kwargs['alt'] if 'alt' in kwargs else None

    return {'image': image,
            'small_image_alias':small_image_alias,
            'breakpoint_data': breakpoint_data,
            'default_image_alias': default_image_alias,
            'alt': alt}
