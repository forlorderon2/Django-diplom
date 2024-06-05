from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import MenuItem

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            send_mail(
                f"Новое сообщение от {name}",
                message,
                email,
                ['your_email@gmail.com'],
                fail_silently=False,
            )
            return redirect('home')

    menu_items = MenuItem.objects.all()
    return render(request, 'main/home.html', {'menu_items': menu_items})
