from django.views import generic
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


class IndexViews(generic.ListView):
    #template_name = ""
    context_object_name = "all_movies"
    queryset = Content.objects.all()

    def get_queryset(self):

        return self.queryset
