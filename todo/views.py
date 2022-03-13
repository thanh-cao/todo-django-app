from django.shortcuts import render
from .models import Item
# Create your views here.


def get_todo_list(req):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(req, 'todo/todo_list.html', context)
