from django.shortcuts import render, redirect
from .models import Item
# Create your views here.


def get_todo_list(req):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(req, 'todo/todo_list.html', context)


def add_item(req):
    if req.method == 'POST':
        name = req.POST['item_name']
        done = 'item_done' in req.POST
        Item.objects.create(name=name, done=done)
        return redirect('get_todo_list')
    return render(req, 'todo/add_item.html')
