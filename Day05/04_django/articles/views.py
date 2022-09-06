from django.shortcuts import render, redirect
from django.views.decorators.http import require_safe
from django.views.decorators.http import require_http_methods
from django.views.decorators.http import require_POST
from .models import Article
from .forms import ArticleForm


# Create your views here.
@require_safe
def index(request):
    # DB에 전체 데이터를 조회
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        # Create
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        # New
        form = ArticleForm()
    # POST일때 is_valid 통과 못한 경우 포함
    context = {
        'form':form,
    }
    return render(request, 'articles/create.html', context)


@require_safe
def detail(request, pk):
    # variable routing으로 받은 pk 값으로 데이터를 조회
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


@require_POST
def delete(request, pk):
    if request.method == 'POST':
        article = Article.objects.get(pk=pk)
        article.delete()
    return redirect('articles:index')
    

@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)
