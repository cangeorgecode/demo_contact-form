from django.shortcuts import render, redirect
from core.forms import ContactForm

def index(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('success')
    return render(request, 'core/index.html')

def success(request):
    return render(request, 'core/success.html')
