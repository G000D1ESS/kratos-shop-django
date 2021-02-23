from django import template

register = template.Library()


@register.filter(name='watermark')
def add_watermark(value):
    return f'[ Godless ] {value}'


@register.inclusion_tag('shop/menu.html')
def show_menu(menu):
    return {'menu': menu}


@register.inclusion_tag('shop/image_slider.html')
def image_slider(images):
    return {'images': images}
from django import template

register = template.Library()


@register.filter(name='watermark')
def add_watermark(value):
    return f'[ Godless ] {value}'


@register.inclusion_tag('shop/menu.html')
def show_menu(menu):
    return {'menu': menu}


@register.inclusion_tag('shop/image_slider.html')
def image_slider(images):
    return {'images': images}
