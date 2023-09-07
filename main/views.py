from django.shortcuts import render, redirect, get_object_or_404 
# View에 Model(Post 게시글) 가져오기
from .models import Post
from .forms import PostForm
from django.http import HttpResponseRedirect
from django.urls import reverse


# index.html 페이지를 부르는 index 함수
def index(request):
    return render(request, 'main/index.html')


# index.html 페이지를 부르는 index 함수
def info(request):
    return render(request, 'main/info.html')

# contact.html 페이지를 부르는 blog 함수
def contact(request):
    # 모든 Post를 가져와 postlist에 저장합니다
    postlist = Post.objects.all()
    # contact.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져옵니다 
    return render(request, 'main/contact.html', {'postlist':postlist})

# contact의 게시글(posting)을 부르는 posting 함수
def posting(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    post = Post.objects.get(pk=pk)
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'main/posting.html', {'post':post})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # 폼을 저장하기 전에 모델 인스턴스를 가져와서 추가 데이터를 설정할 수 있습니다.
            post = form.save(commit=False)  # 커밋하지 않은 상태로 모델 인스턴스 생성
            post.password = request.POST.get('password')  # 비밀번호 설정
            post.save()  # 이제 모델 인스턴스를 저장
            return redirect('contact')  # URL 패턴 이름 사용 (reverse 대신)
    else:
        form = PostForm()
    return render(request, 'main/post_create.html', {'form': form})

def remove_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        # 게시물을 삭제합니다.
        post.delete()
        return HttpResponseRedirect(reverse('contact'))
    return render(request, 'main/remove_post.html', {'Post': post})

def posting(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        entered_password = request.POST.get('password')
        if entered_password == post.password:
            # 비밀번호가 일치하는 경우 게시물 내용을 보여줌
            return render(request, 'main/posting.html', {'post': post})
        else:
            # 비밀번호가 일치하지 않는 경우 에러 메시지 표시
            error_message = "비밀번호가 일치하지 않습니다."
            return render(request, 'main/post_password.html', {'post': post, 'error_message': error_message})

    return render(request, 'main/post_password.html', {'post': post})