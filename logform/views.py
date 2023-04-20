from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        return redirect('index', name=name, email=email)
    
    return render(request, 'form.html')

def index(request, name, email):
    messages.success(request, 'Your form submitted successfully')
    return render(request, 'index.html', {'name': name, 'email':email})