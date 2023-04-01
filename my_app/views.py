from django.shortcuts import render,redirect
from .models import Post,Category,Tag,Comment,Author
from django.contrib import messages
from .forms import AuthForm,TagForm,PostForm,CommentForm
# Create your views here.

def home_view(request):
    posts = Post.objects.all()
    Cat= Category.objects.all()
    tag = Tag.objects.all()
    context = {
        "post_objects":posts,
        "categories" :Cat,
        "tags" : tag
    }
    return render(request , "mainapp/index.html" , context)

def detail_view(request, post_id):
    post=Post.objects.get(id=post_id)
    form=CommentForm(request.POST or None)
    comment_objects = Comment.objects.filter(post__id=post_id)
    num_visits=request.session.get('visit_count', 0)
    request.session['visit_count']= num_visits + 1
    if request.method == 'POST':
        if form.is_valid():
            comment=form.save(commit=False)
            comment_name=form.cleaned_data['name']
            comment_email=form.cleaned_data['email']
            comment_cont=form.cleaned_data['comment']
            Comment.objects.create(comment=comment_cont, email=comment_email, name=comment_name)
            comment.save()
            return redirect ('detail' , post_id=post.id)
        else:
            return messages.error(request, "Enter the correct Fields")
    context= {
        'comment_objects': comment_objects,
        'post': post,
        'comment_form': form,
        'num_visitors': num_visits,
    }  
    # if request.method == 'POST':
    #     name=request.POST.get('cName')
    #     email=request.POST.get('cEmail')
    #     website=request.POST.get('cWebsite')
    #     message=request.POST.get('cMessage')

    #     Comment.objects.create(name=name, email=email,website=website,message=message)
    #     context["name"]=name
    #     context["email"]=email
    #     context["website"]=website
    #     context["message"]=message
        
    return render(request , "mainapp/single.html" , context)

def comment_view(request):
    comment_form = CommentForm(request.POST)
    
    # context["comment_form"] = comment_form
    if request.method == 'POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment_name=form.cleaned_data['name']
            comment_email=form.cleaned_data['email']
            comment_cont=form.cleaned_data['comment']
            comment = Comment.objects.create(comment=comment_cont)
            email = Comment.objects.create(email=comment_email)
            name = Comment.objects.create(name=comment_name)
            comment.name=name
            comment.email=email
            comment.comment=comment
            comment.save()
            return redirect('home')
    context = {"comment_form": comment_form}

    return render(request, "mainapp/single.html", context)

def form_create_view(request):
    if request.method == 'POST':
        category=request.POST.get('category')
        print(category)
        Category.objects.create(name=category)
        messages.success(request, "category created successfully")

    return render(request, "mainapp/formtest.html" )

def tag_create_view(request):
    if request.method == 'POST':
        tag=request.POST.get('tag')
        print(tag)
        Tag.objects.create(name=tag)
        messages.success(request, "tag created successfully")

    return render(request, "mainapp/formtest.html")
def handle_tag_form(request):
    if request.method == 'POST':
        form=TagForm(request.POST)
        if form.is_valid():
            tagname=form.cleaned_data['name']
            Tag.objects.create(name=tagname)

def handle_author_form(request):
    if request.method == 'POST':
        form= AuthForm(request.POST)
        if form.is_valid():
            author_name=form.cleaned_data['name']
            form.save()
            messages.success(request, f"{author_name} created successfully")
            return redirect(request, "mainapp/single.html")
        
def handle_post(request):
    context={}
    post_form =PostForm(request.POST)
    context['post_form']=post_form
    if request.method == 'POST':
        form=PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            author_name=form.cleaned_data['author']
            author = Author.objects.create(name=author_name)
            post.author=author
            post.save()
            return redirect('home')
    return render(request, "mainapp/post.html", context)




