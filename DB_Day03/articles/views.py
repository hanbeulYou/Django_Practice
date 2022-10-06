from django.shortcuts import render, redirect, get_object_or_404

import random

from .models import Article, Comment
from .forms import ArticleForm, CommentForm


def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

    
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm()

    cnt_red = article.comment_set.filter(pick='RE').count()
    cnt_blue = article.comment_set.filter(pick='BL').count()
    cnt_total = cnt_red+cnt_blue
    per_red, per_blue = 0, 0
    if cnt_total > 0:
        per_red = round(cnt_red/cnt_total*100, 1)
        per_blue = round(cnt_blue/cnt_total*100, 1)

    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'cnt_red': cnt_red,
        'cnt_blue': cnt_red,
        'per_red': per_red,
        'per_blue': per_blue,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


def comments_create(request, pk):
    comment_form = CommentForm(request.POST)
    article = Article.objects.get(pk=pk)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()
    return redirect('articles:detail', article.pk)


def comments_delete(request, article_pk, comment_pk):
    pass


def random_detail(request):
    articles = Article.objects.all()
    rand_article = random.choice(articles)
    return redirect('articles:detail', rand_article.pk)