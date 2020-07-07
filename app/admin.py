from django.contrib.admin import AdminSite
from django.contrib import admin
from .models import *
from django.db import models
from django.urls import reverse


'''custom admin page'''
class WebAdmin(AdminSite):
    site_header = 'WEBXPver2'
    site_title = 'WEBXPver2'


admin_site = WebAdmin(name='myadmin')


'''setting up tabulars'''
class UserListDetail_Tabular(admin.TabularInline):
    list_display = ('content',)
    readonly = ('content',)
    model = UserListDetail


class UserList_Tabular(admin.TabularInline):
    list_display = ('name',)
    readonly_fields = ('name',)
    model = UserList
    inlines = [UserListDetail_Tabular, ]


class History_Tabular(admin.TabularInline):
    list_display = ('content', 'time')
    readonly_fields = ('content', 'time')
    model = WatchHistory

class Content_Tabular(admin.TabularInline):
    list_display = ('poster', 'name')
    model = Content


class Crew_HR_Tabular(admin.TabularInline):
    list_display = ('content',)
    model = Crew
    inlines = [Content_Tabular, ]


class HR_Tabular(admin.TabularInline):
    list_display = ('image', 'name',)
    model = HR


class Crew_Content_Tabular(admin.TabularInline):
    list_display = ('hr',)
    model = Crew
    inlines = [HR_Tabular, ]


class Episode_Tabular(admin.TabularInline):
    model = Episode


class Season_Tabular(admin.TabularInline):
    model = Season
    inlines = Episode_Tabular


class Classification_Tabular(admin.TabularInline):
    model = Classification


'''setting admmin for each model'''
class User_Admin(admin.ModelAdmin):
    list_display = ('name', 'password', 'email', 'created',)
    readonly = ('created',)
    list_filter = ('created',)
    inlines = [
        UserList_Tabular,
        History_Tabular,
    ]

    class Meta:
        model = User


class Content_Admin(admin.ModelAdmin):
    list_display = ('name', 'type', 'status', 'studio', 'year', 'country', 'poster')
    inlines = [Classification_Tabular, Season_Tabular, Crew_Content_Tabular, ]
    list_filter = ('type', 'status', 'studio', 'year', 'country',)
    class Meta:
        model = Content


class Season_Admin(admin.ModelAdmin):

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

class Genre_Admin(admin.ModelAdmin):

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class Classification_Admin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class Episode_Admin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class HR_Admin(admin.ModelAdmin):
    list_display = ('name', 'birth', 'country', 'JobChoices', 'image')
    inlines = [Crew_HR_Tabular,]

    class Meta:
        model = HR


class Crew_Admin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class Report_Admin(admin.ModelAdmin):
    list_display = ('content', 'type', 'user', 'time')
    readonly_fields = ('content', 'type', 'user', 'time')
    list_filter = ('time', 'type')

    class Meta:
        model = Report


class UserList_Admin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class UserListDetail_Admin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class History_Admin(admin.ModelAdmin):
    readonly_fields = ('user', 'content', 'time')
    list_filter = ('time',)

    class Meta:
        model = WatchHistory


'''register models'''
admin_site.register(User, User_Admin)
admin_site.register(Content, Content_Admin)
admin_site.register(Season, Season_Admin)
admin_site.register(Genre, Genre_Admin)
admin_site.register(Classification, Classification_Admin)
admin_site.register(Episode, Episode_Admin)
admin_site.register(HR, HR_Admin)
admin_site.register(Crew, Crew_Admin)
admin_site.register(Report, Report_Admin)
admin_site.register(UserList, UserList_Admin)
admin_site.register(UserListDetail, UserListDetail_Admin)
admin_site.register(WatchHistory, History_Admin)
