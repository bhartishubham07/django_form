from django.shortcuts import render

# Create your views here.
from app.forms import *
from app.models import *

def insert_topic(request):
    TFO = TopicForm()
    d = {'TFO' : TFO}
    
    if request.method == 'POST':
        TFD = TopicForm(request.POST)
        if TFD.is_valid():
            topic_name=TFD.cleaned_data['topic_name']
            
            TO = Topic.objects.get_or_create(topic_name=topic_name)[0]
            TO.save()

            TQS = Topic.objects.all()
            d1 = {'TQS' : TQS}
            return render(request, 'display_topic.html', d1)
    
    return render(request, 'insert_topic.html', d)





def insert_webpage(request):
    WFO = WebpageForm()
    d = {'WFO' : WFO}
    
    if request.method == 'POST':
        WFD = WebpageForm(request.POST)
        if WFD.is_valid():
            topic_name = WFD.cleaned_data['topic_name']
            name = WFD.cleaned_data['name']
            url = WFD.cleaned_data['url']
            email = WFD.cleaned_data['email']
            
            TO = Topic.objects.get_or_create(topic_name=topic_name)[0]
            WO = Webpage.objects.get_or_create(topic_name=TO, name=name, url=url, email=email)[0]
            WO.save()
            
            WQS = Webpage.objects.all()
            d1 = {'WQS' : WQS}
            return render(request, 'display_webpage.html', d1)
        
    return render(request, 'insert_webpage.html', d)




def insert_record(request):
    ARFO = AccessRecordForm()
    d = {'ARFO' : ARFO}
    
    if request.method == 'POST':
        ARFD = AccessRecordForm(request.POST)
        if ARFD.is_valid():
            name = ARFD.cleaned_data['name']
            author = ARFD.cleaned_data['author']
            date = ARFD.cleaned_data['date']
            
            WO = Webpage.objects.get_or_create(name=name)[0]
            ARO = AccessRecord.objects.get_or_create(name=WO, author=author, date=date)[0]
            ARO.save()
            
            ARQS = AccessRecord.objects.all()
            d1 = {'ARQS' :ARQS}
            return render(request, 'display_record.html', d1)
    
    return render(request, 'insert_record.html', d)
    
    