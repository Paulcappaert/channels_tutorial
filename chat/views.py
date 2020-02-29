from django.shortcuts import render

def home(request):
    return render(request, 'chat/home.html')

def room(request):
    name = request.GET['room']
    return render(request, 'chat/chat.html', {'room_name': name})
