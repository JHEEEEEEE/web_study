from django.shortcuts import render, redirect, get_object_or_404 
# View에 Model(Post 게시글) 가져오기
from .models import Post
from .forms import PostForm


# index.html 페이지를 부르는 index 함수
def index(request):
    return render(request, 'main/index.html')

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
            form.save()
            return redirect('/contact')
      else:
          form = PostForm()
      return render(request, 'main/post_create.html', {'form': form})


def remove_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/contact/')
    return render(request, 'main/remove_post.html', {'Post': post})
