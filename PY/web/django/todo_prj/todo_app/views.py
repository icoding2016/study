from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import ToDo


def home(request):
    todos = ToDo.objects.all()

    # rsp = HttpResponse('<p>Home view</p>')
    return render(request, 'home.html', {'todos':todos, })


def todo_detail(request, id):
    #return rsp = HttpResponse(f"<p>ToDo_{id} details</p>")
    try:
        todo = ToDo.objects.get(id=id)
    except ToDo.DoesNotExist:
        raise Http404('Record not found')
    return render(request, 'todo_detail.html', {'todo':todo, })
