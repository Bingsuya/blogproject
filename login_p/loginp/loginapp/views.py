from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from loginapp.models import *
from userapp.models import *
# Create your views here.
def index(request):
    #post = Post.objects.filter(user = request.user)
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['re_password']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            #auth.login(request, user)
            return redirect('index')
    return render(request,'signup.html')

def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else :
            return render(request, 'login.html', {'error' : '아이디나 비밀번호가 틀렸습니다.'})
    else :
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

def mypost(request):
    post = reversed(Post.objects.filter(user = request.user) )
    return render(request, 'mypost.html',  {
        'post' :post })


def deletepost(request): 
    post_id = request.GET['post_id'] 
    post = Post.objects.get(id = post_id)
    post.delete() #타이틀이나 컨텐츠 저장할 필요없이 삭제만 해주면됨
    return redirect('mypost')


def addpost(request):
    a = Post.objects.filter(user = request.user)

    if request.method == 'POST' and 'picture' in request.FILES:
        
        post = Post()
        
        postcontents = request.POST['postcontents']
        posttitle = request.POST['posttitle']
        picture = request.FILES['picture']

        post.postcontents = postcontents
        post.posttitle = posttitle
        post.picture = picture
        post.user = request.user

        post.save()
        return render(request,'addpost.html', {'done' : '사진 추가 완료!'})

    elif request.method == 'POST':
        post = Post()
        
        postcontents = request.POST['postcontents']
        posttitle = request.POST['posttitle']

        post.postcontents = postcontents
        post.posttitle = posttitle
        post.user = request.user

        post.save()

        return render(request,'addpost.html' , {'done' : '사진 빼고 완료!'})
    return render(request,'addpost.html')

def editpost(request): #post로 받아오자
    if request.method == 'POST' and 'picture' in request.FILES:
        post_id = request.POST['post_id'] #히든인풋을 post_id로 저장
        aa = Post.objects.get(id = post_id)#그걸 id로 받아서 오브젝트로 받아옴
        postcontents = request.POST['postcontents']
        posttitle = request.POST['posttitle']
        picture = request.FILES['picture']
        aa.postcontents = postcontents
        aa.posttitle = posttitle
        aa.picture = picture
        aa.user = request.user
        aa.save()
        return redirect('mypost') 
        #editpost로 가면 기존 aa가 사라져버렸기때문에 에러가 뜬다. 그래서 사진첩 redirect해줌
        
    elif request.method == 'POST':
        post_id = request.POST['post_id']
        aa = Post.objects.get(id = post_id)
        postcontents = request.POST['postcontents']
        posttitle = request.POST['posttitle']
        aa.postcontents = postcontents
        aa.posttitle = posttitle
        aa.user = request.user
        aa.save()
        return redirect('mypost')

    else :
        post_id = request.GET['post_id']
        aa = Post.objects.get(id = post_id )
        return render(request,'editpost.html', {'aa' : aa})