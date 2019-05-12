from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return  HttpResponse("Hello world!!! \n You are at the polls view")
