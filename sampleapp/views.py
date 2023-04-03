from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.


def home(request):
    if not request.user.is_authenticated:
        return redirect("login")
    blogs = Article.objects.all()
    keyword = request.GET.get('keyword')
    genre = request.GET.get('genre')
    if keyword:
         blogs = blogs.filter(tittle__icontains=keyword)
    if genre:
        blogs = blogs.filter(genre=genre)
    context = {"blog": blogs,
    'choices':Article.genre_choices
     }
    return render(request, "index.html", context)


@login_required(login_url="login")
def create(request):
    if request.method == "POST":
        tt = request.POST.get("t")
        cc = request.POST.get("c")
        image = request.FILES.get("cover_image")
        genre = request.POST.get('genre')
        Article.objects.create(
            tittle=tt, 
            content=cc,
            cover_image=image,
            genre=genre,
            author=request.user
        )
        return redirect("index")
    return render(request, "create.html",{'choices':Article.genre_choices})


@login_required(login_url="login")
def details(request, id):
    content = Article.objects.get(id=id)
    comments = Comment.objects.filter(article=content)
    context = {"blog": content, "comments": comments}
    return render(request, "details.html", context)


@login_required(login_url="login")
def edit(request, id):
    edits = Article.objects.get(id=id)
    context = {"blog": edits}
    if request.method == "POST":
        if edits.author != request.user:
            return HttpResponse("You are not Authorize to edit this page")
        tit = request.POST.get("t")
        con = request.POST.get("c")
        edits.tittle = tit
        edits.content = con
        edits.save()
        return redirect("details", id)
    return render(request, "edit.html", context)


@login_required(login_url="login")
def delete(request, id):
    article = Article.objects.get(id=id)
    if article.author != request.user:
        return HttpResponse("You are not Authorize to delete this page")
    if request.method == "POST":
        article.delete()
        return redirect("index")
    context = {"blog": article}
    return render(request, "delete.html", context)


def comment_post(requset, article_id):
    article = Article.objects.get(id=article_id)
    if requset.method == "POST":
        comments = requset.POST.get("comment")
        Comment.objects.create(
            text=comments, comment_author=requset.user, article=article
        )
    return redirect("details", article_id)


def comment_delete(request,id):
    comment = Comment.objects.get(id=id)
    article_id = comment.article.id
    comment.delete()
    return redirect('details',article_id)

 
def comment_edit(request,id):
    comment = Comment.objects.get(id=id)
    blog = comment.article
    if request.method == 'POST':
        text = request.POST.get('comment')
        comment.text = text
        comment.save()
        return redirect('details',blog.id)
    comments = Comment.objects.filter(article = blog)
    context = {
        'blog':blog,
        'comments':comments,
        'cmd':comment,
        'edit':True
    }
    return render(request,'details.html',context)