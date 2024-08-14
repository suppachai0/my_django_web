from django.shortcuts import render

# Create your views here.
def indexPage(request):
    return render(request, 'index.html')

def aboutUs(request):
    return render(request, 'about.html')

def contactUs(request):
    return render(request, 'contact.html')

def forPage(request):
    context = {}  
    lt = list(range(0, 100))
    context["list"] = lt
    return render(request, 'for_test.html', context)

def cardPage(request):
    context = {}  
    lt = list(range(0, 100))
    context["list"] = lt
    return render(request, 'card.html', context)

def cardcolorpage(request):
    context = {
        'color': 'all',
    }

    if request.method == "GET" and request.GET.get('color') is not None:
        context['color'] = request.GET.get('color')

    return render(request, 'card_color.html', context)

def form(request):
    email = ''
    password = ''
    context = {}

    if request.method == "POST":  # แก้ไขการพิมพ์ผิดจาก emthod เป็น method
        email = request.POST.get('email')
        password = request.POST.get('password')

    context['email'] = email
    context['password'] = password
    
    return render(request, 'form.html', context)  # เพิ่ม context ที่ส่งไปยัง template
