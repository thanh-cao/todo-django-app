from django.shortcuts import render
# Create your views here.
def get_todo_list(req):
    return render(req, 'todo/todo_list.html')
