from django.shortcuts import get_object_or_404, render,HttpResponse,redirect
from django.urls import reverse
from django.views import generic
import json

from .models import *

#객체 반환
def get_object(model,**args):
    query_set = model.objects.filter(**args)
    return query_set[0] if query_set else None
def check_login(request,url):
    user_id = request.session.get('id')
    return user_id if user_id else redirect(url)
    
# Create your views here.
class IndexView(generic.ListView):
    template_name = 'main.html'

    def get_queryset(self):
        Recipe.objects.order_by('upload_date')
# 로그인
def login(request):
    context = {}
    if request.method == "POST":
        user_id = request.POST.get('user_id')  
        user_pw = request.POST.get('user_pw')
        account = Account.objects.filter(user_id=user_id,password=user_pw)
        if account:
            request.session['id']=user_id
            return redirect('/')
        else:
            context['lgmsg'] = "아이디와 비밀번호가 일치하지 않습니다." 
    return render(request,'login.html',context)

#로그아웃 
def logout(request):
    del request.session['id']   
    return redirect('/')
# 회원가입 
def register(request):
    if request.method == "POST":
        Account.objects.create(
            user_id  = request.POST.get('user_id'),
            password = request.POST.get('user_pwd'),
            username = request.POST.get('user_name'),
            email    = request.POST.get('user_email'),
            phonenumber = request.POST.get('user_phone'),
        )
        return redirect('/login/')
    return render(request,'register.html')
#아이디 체크
def id_check(request):
    user_id = request.POST.get('id_check')
    account = Account.objects.filter(user_id=user_id)
    response = {}
    if account:
        response ={ 'msg' : True}
    else:
        response = {'msg' : False}
    print(response)
    return HttpResponse(json.dumps(response), content_type="application/json")

def manage_register(request):
    user_id = check_login(request,'/')
    account = get_object(Account,user_id=user_id)
    if account.level != 2: return render(request,'main.html',{'msg':'권한이 없습니다.'})  
    if request.method == "POST":
        Account.objects.create(
            user_id  = request.POST.get('user_id'),
            password = request.POST.get('user_pwd'),
            username = request.POST.get('user_name'),
            email    = request.POST.get('user_email'),
            phonenumber = request.POST.get('user_phone'),
            level      = 1
        )
        return redirect('/')

    return render(request,'manage_register.html')  
        
class ManagerRecipeView(generic.ListView):
    model = Recipe
    template_name = 'manage_recipe.html'


# class ManagerWriteRecipeView(generic.ListView):
#     model = Recipe
#     template_name = 'write_recipe.html'


def ManagerWriteRecipeView(request):
    if not request.session.get('id'):
        # redirect 하기!
        print('None Session!!')
    
    return render(request, 'write_recipe.html')


class ManagerStorageView(generic.ListView):
    model = Recipe
    template_name = 'manage_storage.html'


class ManagerWriteStorageView(generic.ListView):
    model = Recipe
    template_name = 'write_storage.html'