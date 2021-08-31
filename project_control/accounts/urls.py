from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('create_user/',views.createUser),
    path('update_user/',views.updateUser),
    path('remove_user/',views.removeUser),
    path('new_ticket/',views.createTicket),
    path('ticket/',views.viewTicket),
    path('update_ticket/',views.updateTicket),
    path('remove_ticket/',views.removeTicket),
    path('new_project/',views.createProject),
    path('project/',views.viewProject),
    path('update_project/',views.updateProject),
    path('remove_project/',views.removeProject),
    path('new_company/',views.createCompany),
    path('company/',views.viewCompany),
    path('update_company/',views.updateCompany)
]




