from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm, CustomUserChangeForm
# namespace의 중복사용을 피하기 위해 as로 모듈 이름 변경

# Create your views here.
def login(request):
    if request.method == 'POST':
        # 모델폼 아님! request, data 순으로 넣어주기
        form = AuthenticationForm(request, request.POST)
        # 검증하기
        if form.is_valid():
            # 로그인
            # login(request, 유저정보) <- 이름 중복 & 유저 정보 어디?
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    # 로그아웃
    auth_logout(request)
    return redirect('articles:index')


def signup(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # 회원 가입 후 바로 로그인
            # auth_login << 이거 한 줄 추가
            auth_login(request, user)
            return redirect('articles:index')
    else:
        # form = UserCreationForm()
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


def delete(request):
    # 탈퇴
    request.user.delete()
    # 로그아웃
    auth_logout(request)
    return redirect('articles:index')


def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)