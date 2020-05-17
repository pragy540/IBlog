from django.shortcuts import render, HttpResponse, redirect
from .models import Post
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import updatePost


# Create your views here.
def bloghome(request):
    posts=Post.objects.all()
    context={'posts': posts}
    return render(request, 'bloghome.html', context)

def blogpost(request, id):
    post=Post.objects.filter(post_id=id)[0]
    context={'post':post}
    return render(request, 'blogpost.html', context)

def handlesignup(request):
    if request.method == 'POST':
        # get the post parameters
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        #checks for errorneous inputs
        if len(username) > 20:
            messages.error(request, "Your username must be of less than 20 characters. ")
            return redirect('/')
        if pass1 != pass2:
            messages.error(request, "Your passwords do not match. ")
            return redirect('/')
        if not username.isalnum():
            messages.error(request, "Username should only contain letters and numbers. ")
            return redirect('/')


        #Create the user!
        myuser=User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, "Your ICoder account has been successfully created. ")
        return redirect('/')

    else:
        return HttpResponse("404 - Not found")



def handlelogin(request):
    if request.method== 'POST':
        loginusername= request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user= authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('/dashboard/')
        else:
            messages.error(request, "Invalid Credentials, Please try again")
            return redirect('/')

    return HttpResponse("404 - Not Found")


def handlelogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('/')



def dashboard(request):
    posts=Post.objects.filter(author=request.user.username)
    context={'posts':posts}
    return render(request, 'dashboard.html', context)


def personal(request,id):
    post = Post.objects.filter(post_id=id)[0]
    context = {'post': post}
    return render(request, 'personal.html', context)


def tiny(request):
    return render(request, 'tiny.html')

def update(request, id):
    post=Post.objects.get(post_id=id)
    form=updatePost(instance=post)
    context={'form': form}

    if request.method == 'POST':
        form=updatePost(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('/')


    return render(request, 'updatepost.html',context )


