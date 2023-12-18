from django.shortcuts import render,redirect,get_object_or_404
from.models import post,comment
from django.contrib import messages
from django.urls import reverse
from.forms import renew,change
from django.http import HttpResponse
# Create your views here.
def create(request):
    if request.method == 'POST':
        title=request.POST.get('title')
        content=request.POST.get('content')
        user=request.user
        pic=request.FILES.get('pic')
        if pic is not None:
            store= post(author=user,title=title,content=content,image=pic)
            store.save()
            messages.success(request,'Created successfully')
            return redirect('/')
        else:
            store= post(author=user,title=title,content=content )
            store.save()
            messages.success(request,'Created successfully')
            return redirect('/')
    return render(request,'blog/create.html')
def home(request):
    posts=post.objects.all().order_by('-date_posted')
    return render(request,'blog/home.html',{'posts':posts})

def about(request):
    return HttpResponse('<h1>This app was created by Awomewe Oladeji</h1>')

def detail(request,id):
    grab=get_object_or_404(post,id=id)
    return render(request,'blog/detail.html',{'post':grab})

def delete(request,id):
        grab = get_object_or_404(post,id=id)
        if grab.author==request.user:
            grab.delete()
            messages.success(request,'Deleted successfully')
            return redirect('/')
        else:
            messages.error(request,'Access denied')
            return redirect('/')
def update(request,id):
   if request.method == 'POST':
       grab = get_object_or_404(post, id=id)
       form = renew(request.POST,instance=grab)
       if form.is_valid():
           form.save()
           messages.success(request,'Updated')
           return render(request,'blog/update.html',{'form':form})
   else:
       form = renew()
       return render(request, 'blog/update.html', {'form': form})


def comments(request,id):
    grab=get_object_or_404(post,id=id)
    new_comment=comment.objects.filter(posts=grab)
    return render(request,'blog/comment.html',{'comment':new_comment,'grab':grab})

def add_comment(request,id):
    if request.method=='POST':
        author=request.user
        grab = get_object_or_404(post,id=id)
        content=request.POST.get('content')
        store = comment(author=author,posts=grab,content=content)
        store.save()
        return redirect('/')
    else:
        return HttpResponse('Not a POST method')
    

def destroy(request,id):
    get_comment=comment.objects.get(id=id)
    get_comment_post=get_comment.posts.pk
    # get_post=post.objects.get(id=get_comment_post)
    if get_comment.author == request.user or request.user.is_staff:
        get_comment.delete()
        messages.success(request,'You just deleted this comment')
        # return redirect(reverse(comments,args=get_comment_post))
        # return redirect('comment',post_id=get_comment_post)
        return redirect('/')
    else:
        messages.error(request,'Permission denied')
        # return redirect(reverse(comments,args=get_post.pk))
        # return redirect('comment',post_id=get_comment_post)
        return redirect('/')


def new_update(request,id):
    grab = get_object_or_404(comment,id=id)
    if request.method == 'POST':
        if request.user == grab.author:
            form = change(request.POST,instance=grab)
            if form.is_valid():
                form.save()
                messages.success(request,'Updated')
                # return redirect('comment' + grab.id)
        else:
            messages.error(request, 'Access denied')
    else:
        form=change()
    return render(request,'blog/comment_update.html',{'form':form})


# def destroy(request,id):
#     grab = get_object_or_404(comment, id=id)
#     if request.user == grab.author:
#         grab.delete()
#         return redirect('/')
#     else:
#         messages.error(request, 'Access denied')
