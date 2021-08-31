from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

## USER

def home(request):
    context = {}
    return render(request, 'accounts/user_dashboard.html')

def createUser(request):
    context = {}
    return render(request, 'new_user')

def updateUser(request):
    context = {}
    return render(request, 'update_user')

def removeUser(request):
    context = {}
    return render(request, 'remove_user')

## TICKET

def createTicket(request):
    context = {}
    return render(request, 'new_ticket')

def viewTicket(request):
    context = {}
    return render(request, 'ticket')

def updateTicket(request):
    context = {}
    return render(request, 'update_ticket')

def removeTicket(request):
    context = {}
    return render(request, 'remove_ticket')

## PROJECT

def createProject(request):
    context = {}
    return render(request, 'new_project')

def viewProject(request):
    context = {}
    return render(request, 'project')

def updateProject(request):
    context = {}
    return render(request, 'update_project')

def removeProject(request):
    context = {}
    return render(request, 'remove_project')

## COMPANY

def createCompany(request):
    context = {}
    return render(request, 'new_company')

def viewCompany(request):
    context = {}
    return render(request, 'company')

def updateCompany(request):
    context = {}
    return render(request, 'update_company')