from django.http import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.


def test_views(request):
    return render(request,'01-tmp.html')

def tmp_views(request):
    return render(request,'02-tmp.html')


def change_score(request):
    if request.method =="POST":
        uname = request.POST['uname']
        uscore = request.POST['uscore']
        users = Score.objects.filter(name = uname)
        if len(users) >0:
            obj = Score.objects.get(name =uname)
            obj.get_score=uscore
            obj.save()
        else:
            Score.objects.create(name=uname,get_score=uscore)

        Rank.objects.all().delete()
        n = 1
        score_li = Score.objects.all().order_by('-get_score')
        for i in score_li:
            Rank.objects.create(score_id=i.id,ranking=n)
            n+=1
            print(i.id)
        return HttpResponse('<h1>上传成功<h1/>')

def select_views(request):
    return render(request,'04-tmp.html')

def show_views(request):
    if request.method=='POST':
        uname = request.POST['uname']
        start = int(request.POST['start'])-1
        end = int(request.POST['end'])
        #拿出排行榜的数据
        obj = Rank.objects.order_by('ranking')[start:end]
        # 反向查询排名
        score = Score.objects.get(name=uname)
        score_rank = score.rank
        return render(request,'05-tmp.html',locals())
