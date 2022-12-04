from django.shortcuts import render, HttpResponse, redirect

from .models import BlogPost
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    myposts = BlogPost.objects.all()
    print(myposts)
    return render(request, 'index.html', {'myposts': myposts} )
    # return HttpResponse("hello there")

def search(request):
    query = request.GET.get('search')
    print("Your search item is = "+ str(query.lower()))
    print(len(query))
    mypost_temp = BlogPost.objects.all()
    myposts = []
    for item in mypost_temp:
        print(item)
        if query.lower() in item.p_title.lower() or query.lower() in item.p_content0.lower():
            myposts.append(item)
    if len(query) > 30:
        return render(request, 'error.html',{'query':query})
    else:
        return render(request,'index.html',{'myposts': myposts, 'query':query} )

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def blogPost(request,id):
    post = BlogPost.objects.filter(p_id=id)[0]
    print(post)
    return render(request, 'blog.html', {'post':post})

def signup(request):
    if request.method == 'POST':
        #getting the parameters
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['pass1']
        confirmPassword = request.POST['pass2']
        phone = request.POST['phone']
        #form validation
        if len(username) > 20 or len(username) < 1:
            messages.error(request, "invalid username")
        
        if password != confirmPassword:
            messages.error(request, "Password does not match")

        #user creation
        createuser = User.objects.create_user(username,email,password)
        createuser.phone = phone
        createuser.save()
        if User.objects.filter(username = username).first():
            messages.error(request, "This username is already taken bro")
            return redirect('/')
        else:
            messages.success(request, 'User Created, Please remember email and the respective password')
            return redirect(request, '/')
    else:
        return render(request, 'error.html')


