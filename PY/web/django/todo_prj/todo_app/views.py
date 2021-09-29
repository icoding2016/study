from django.shortcuts import render
from rest_framework import response, serializers

from .models import ToDo


####################################################################
# Solution 1: use basic django http handler + template
# the handlers are mapped in urls.urlpatterns by name

from django.http import HttpResponse, Http404

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



####################################################################
# Solution 2: Use rest_framework viewsets
# ModelViewSet is a special view that Django Rest Framework provides.
# It will handle GET and POST for Heroes without us having to do any more work.

from rest_framework import viewsets
from .serializers import ToDoSerializer

class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all().order_by('handle_time')
    serializer_class = ToDoSerializer


####################################################################
# Solution 3: use standard restful API view from rest_framework
# https://www.django-rest-framework.org/api-guide/views/

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)


# use default serializer
class ToDoViewDefault(APIView):

    def get(self, request, task):
        try:
            todo = ToDo.objects.get(task=task)    # 
            serializer = ToDoSerializer(todo)
        except ToDo.DoesNotExist:
            raise Http404('Record not found')
        # return render(request, 'todo_list.html', {'todo':todo, })
        return Response(serializer.data)


class ToDoView(APIView):

    def get(self, request, task):
        try:
            todo = ToDo.objects.get(task=task)    # 
            # serializer = ToDoSerializer(todo)
            context = {'task':todo.task, 'time':todo.handle_time, 'created':todo.create_time}
        except ToDo.DoesNotExist:
            raise Http404('Record not found')
        # return render(request, 'todo_detail.html', {'todo':todo, })
        return render(request, 'todo_info.html', context)


class ToDoListViewDefault(APIView):

    def get(self, request):
        try:
            todo = ToDo.objects.all().order_by('handle_time')
            serializer = ToDoSerializer(todo, many=True)
            context = {list:todo}
        except ToDo.DoesNotExist:
            raise Http404('Record not found')
        return Response(serializer.data)
        return render(request, 'todo_list.html', context)

class ToDoListView(APIView):

    def get(self, request):
        try:
            todo = ToDo.objects.all().order_by('handle_time')
            # serializer = ToDoSerializer(todo, many=True)
            context = {list:todo}
        except ToDo.DoesNotExist:
            raise Http404('Record not found')
        # return Response(serializer.data)
        return render(request, 'todo_list.html', context)


