from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('new/', views.create_page, name='new_page'),
    path('random/', views.random_page, name='random_page'),
    path('wiki/<str:query>/', views.search, name='search'),
    path('edit_page/<str:name>', views.edit_page, name='edit_page'),
    path('save/<str:name>/', views.save_edit, name='save_edit'),
    path('search/', views.search_form, name='search_form')
]
