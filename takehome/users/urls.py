from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path("", views.IndexView.as_view(), name='index'),
    path("add/", views.UserAddView.as_view(), name='add_user'),
    path("<int:pk>/edit", views.UserEditView.as_view(), name='edit_user'),
    path("<int:pk>/delete", views.UserDeleteView.as_view(), name='delete_user'),
]