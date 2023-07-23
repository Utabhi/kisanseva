from django.shortcuts import render
from .models import complaint

# Create your views here.
def complaint1(request):
        if request.method == 'POST':
            if request.POST.get('name') :
                post=complaint()
                post.name= request.POST.get('name')
                post.father_name= request.POST.get('father_name')
                post.mother_name= request.POST.get('mother_name')
                post.address= request.POST.get('address')
                post.gender= request.POST.get('gender')
                post.complain= request.POST.get('complain')
                post.email= request.POST.get('email')
                post.contact_no= request.POST.get('contact_no')
                post.problem_type=request.POST.get('problem_type')
                post.save()
                
                return render(request,'complaint.html')  

        else:
                return render(request,'complaint.html')

def prices(request):
    return render(request,'PRICES.html')
def gallary(request):
    return render(request,'slider.html')
def home(request):
    return render(request,'home.html')
def soiltypes(request):
    return render(request,'soiltypes.html')
def aboutus(request):
    return render(request,'aboutus.html')



