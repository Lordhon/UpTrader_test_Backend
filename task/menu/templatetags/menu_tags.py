from django import template
from menu.models import  MenuItem
from django.urls import reverse

register = template.Library()
@register.inclusion_tag('menu_item.html' , takes_context=True)
def draw_menu(context , menu_name):
    request = context['request']
    path = request.path
    menu_items = MenuItem.objects.select_related('parent').filter(menu__name=menu_name)
    id_item_dict = {item.id: item for item in menu_items}
    for item in menu_items:
        item.children = []

    main_title = []
    for item in menu_items:
        if item.parent_id:
            parent = id_item_dict.get(item.parent_id)
            parent.children.append(item)
        else:
            main_title.append(item)



    def route(item):
        if item.name_url:
            revers_url = reverse(item.name_url)
            return revers_url == path
        return item.url == path

    def active_path(item):
        item.active = route(item)
        item.open = False
        for child in item.children:
            if active_path(child):
                item.open = True
                item.active = False
                return True
        return item.active

    for item in main_title:
        active_path(item)

    return {'items': main_title}



