from django import forms
from django.contrib.admin import AdminSite
from django.contrib import admin
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.models import Group, User as Au
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin
from django.db import models
from django.urls import reverse
# from django.views.decorators.cache import cache_page
from django.core.exceptions import PermissionDenied
from django.db.models.signals import pre_delete



# custom admin user


"""class UserCreateForm(UserCreationForm):

    class Meta:
        model = adminuser
        fields = ('username',)


class UserEditForm(UserChangeForm):

    class Meta:
        model = adminuser
        fields = ('username',)
"""


class ExtendUserAdmin(UserAdmin):

    # add_form = UserCreateForm
    # change_form = UserEditForm
    # prepopulated_fields = {'username': ('first_name', 'last_name', )}

    def has_delete_permission(self, request, obj=None):
        if obj is None:
            return True
        else:
            return not obj.is_superuser

    def has_change_permission(self, request, obj=None):
        if obj is None:
            return True
        else:
            return not obj.is_superuser

    list_display = ('username', 'is_active', 'is_staff', 'is_superuser', 'last_login', )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
        ('Permissions', {
             'fields': ('is_staff',),
         }),
        ('Groups', {
            'fields': ('groups',),
        }),
        ('Roles', {
            'fields': ('user_permissions',),
        })
    )

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
            ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser'),
        }),
        ('Groups', {
            'fields': ('groups',),
        }),
        ('Roles', {
            'fields': ('user_permissions',),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined'), }),
    )
    readonly_fields = ('last_login', 'date_joined', 'is_superuser')
    filter_horizontal = ['groups', 'user_permissions']

# custom admin group
Users = get_user_model()


class GroupAdminForm(forms.ModelForm):
    class Meta:
        model = Group
        exclude = []

    users = forms.ModelMultipleChoiceField(
        queryset=Users.objects.all(),
        required=False,
        widget=FilteredSelectMultiple('users', False)
    )

    def __init__(self, *args, **kwargs):

        super(GroupAdminForm, self).__init__(*args, **kwargs)

        if self.instance.pk:
            self.fields['users'].initial = self.instance.user_set.all()

    def save_m2m(self):

        self.instance.user_set.set(self.cleaned_data['users'])

    def save(self, *args, **kwargs):

        instance = super(GroupAdminForm, self).save()

        self.save_m2m()

        return instance




class GroupAdmin(admin.ModelAdmin):

    form = GroupAdminForm

    filter_horizontal = ['permissions']


'''custom admin page'''
class WebAdmin(AdminSite):
    site_header = 'WEBXP ver2'
    site_title = 'WEBXP ver2'


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
#@cache_page(None)
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


#@cache_page(None)
class Content_Admin(admin.ModelAdmin):
    list_display = ('name', 'type', 'status', 'studio', 'year', 'country', 'poster')
    inlines = [Classification_Tabular, Season_Tabular, Crew_Content_Tabular, ]
    list_filter = ('type', 'status', 'studio', 'year', 'country',)

    class Meta:
        model = Content


#@cache_page(None)
class Season_Admin(admin.ModelAdmin):

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


#@cache_page(None)
class Genre_Admin(admin.ModelAdmin):

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


#@cache_page(None)
class Classification_Admin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


#@cache_page(None)
class Episode_Admin(admin.ModelAdmin):

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


#@cache_page(None)
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
admin_site.register(Group, GroupAdmin)
admin_site.register(Au, ExtendUserAdmin)


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
