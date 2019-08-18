from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import article, author, category, comment
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .forms import createform, register_user, createauthor,commentform, categoryform
from django.contrib import messages


# Create your views here.
def index(request):
    post= article.objects.all()
    search = request.GET.get('q')  # from base.html search name="q"
    if search:                   #Q lookup
        post= post.filter(
            Q(title__icontains=search)|
            Q(posted_on__icontains=search)

        )
    paginator = Paginator(post, 8)  # Show 25 contacts per page
    page = request.GET.get('p') #page=p
    total_article = paginator.get_page(page)


    context={
        "post":total_article
    }
    return render(request, "index.html", context)

def getauthor(request, name):
    post_author= get_object_or_404(User, username=name)
    auth=get_object_or_404(author, name=post_author.id)
    post= article.objects.filter(article_author=auth.id)

    context={

        "auth":auth,
        "post":post
    }
    return render(request, "profile.html", context)

def getsingle(request, id):
    first= article.objects.first()
    last= article.objects.last()
    getcomment=comment.objects.filter(post=id)
    post= get_object_or_404(article, pk=id)
    related= article.objects.filter(category=post.category).exclude(id=id)[:4]
    form=commentform(request.POST or None)
    if form.is_valid():
        instance=form.save(commit= False)
        instance.post=post
        instance.save()
    context={

        "post":post,
        "first":first,
        "last":last,
        "related": related,
        "form": form,
        "comment": getcomment

    }
    return render(request, "single.html", context)

def getTopic(request, name):
    cat = get_object_or_404(category, name=name)
    post = article.objects.filter(category=cat.id)
    paginator = Paginator(post, 8)  # Show 25 contacts per page

    page = request.GET.get('p')
    total_article = paginator.get_page(page)
    context={

        "post":total_article,
        "cat":cat
    }
    return render(request, "category.html", context)

def getLogin(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            user = request.POST.get('user')
            password = request.POST.get('pass')
            auth = authenticate(request, username=user, password=password)
            if auth is not None:
                login(request, auth)
                return redirect('index')
            else:
                messages.add_message(request, messages.ERROR, 'User Or Password Not Match!!')
                return render(request, 'login.html')
    return render(request, 'login.html')

def getlogout(request):
    logout(request)
    return redirect('index')

def getcreate(request):
    if request.user.is_authenticated:
        u = get_object_or_404(author, name=request.user.id)
        form = createform(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.article_author=u
            instance.save()
            return redirect('index')
        return render(request, 'create.html', {"form": form})
    else:
        return redirect('login')

def getupdate(request, pid):
    if request.user.is_authenticated:
        u = get_object_or_404(author, name=request.user.id)
        post = get_object_or_404(article, id=pid)
        form = createform(request.POST or None, request.FILES or None, instance=post)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.article_author=u
            instance.save()
            messages.success(request, 'Article is updated successfully')
            return redirect('profile')

        return render(request, 'create.html', {"form": form})
    else:
        return redirect('login')

def getdelete(request, pid):
    if request.user.is_authenticated:
        post = get_object_or_404(article, id=pid)
        post.delete()
        messages.warning(request, 'Article is successfully deleted')
        return redirect('profile')
    else:
        return redirect('login')




def getprofile(request):
    if request.user.is_authenticated:

        user= get_object_or_404(User, id=request.user.id)
        author_profile= author.objects.filter(name=user.id)
        if author_profile:
            author_user = get_object_or_404(author, name=request.user.id)
            post = article.objects.filter(article_author=author_user.id)
            return render(request, 'logedin_profile.html', {"post":post, "user":author_user})
        else:
            form=createauthor(request.POST or None, request.FILES or None)
            if form.is_valid():
                instance=form.save(commit=False)
                instance.name =user
                instance.save()
                messages.success(request, "Successfully create author")
                return redirect('profile')
            return render(request, 'createauthor.html', {"form":form})

    else:
        return redirect('login')

def getregister(request):
    form=register_user(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        messages.success(request, 'you are successfully registered')
        return redirect('login')
    return render(request, 'register.html', {"form":form})

def getcategory(request):
    query=category.objects.all()
    return render(request, 'topics.html', {"topic": query})

def createtopic(request):
    form=categoryform(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        messages.success(request, 'Topic created successfully')
        return redirect('category')
    return render(request, 'create_topic.html', { "form":form })

def topicdelete(request, pid):
    if request.user.is_authenticated:
        post = get_object_or_404(category, id=pid)
        post.delete()
        messages.warning(request, 'Topic is successfully deleted')
        return redirect('category')
    else:
        return redirect('login')