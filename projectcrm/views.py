from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Projectcrm Company Main Page</h1> <a href='index'><hr><br><h2>Sales Dept(app101) - Customer List</a></h2>")
