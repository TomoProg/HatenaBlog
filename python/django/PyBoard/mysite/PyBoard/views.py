from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.db.models import Max
from .models import Topic, TopicDetail
from .forms import AccountForm, TopicForm, ReplyForm
from django.utils import timezone

# Create your views here.

def index(request):
    """ index.html view """
    template = loader.get_template('PyBoard/index.html')

    topic_num_query = """
                      SELECT
                          COUNT(*)
                      FROM
                          PyBoard_topicdetail
                      WHERE
                          PyBoard_topic.id = PyBoard_topicdetail.title_id
                      """
    topic_list = Topic.objects.order_by('-update_datetime').extra(
        select={'topic_num': topic_num_query}
    )
    context = {
        'signin_username': request.user.username,
        'topics': topic_list,
    }

    return HttpResponse(template.render(context, request))

def about(request):
    """ about.html view """
    template = loader.get_template('PyBoard/about/about.html')
    context = {
        'signin_username': request.user.username,
    }
    return HttpResponse(template.render(context, request))

def contact(request):
    """ contact.html view """
    template = loader.get_template('PyBoard/contact/contact.html')
    context = {
        'signin_username': request.user.username,
    }
    return HttpResponse(template.render(context, request))

def detail(request, topic_id):
    """ detail.html view """
    template = loader.get_template('PyBoard/detail/detail.html')
    topic_title = Topic.objects.get(pk=topic_id).title
    topic_detail_list = TopicDetail.objects.filter(title=topic_id).order_by('register_datetime')
    context = {
        'signin_username': request.user.username,
        'topic_title': topic_title,
        'topic_details': topic_detail_list,
        'topic_id': topic_id,
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url='PyBoard:signin')
def create(request):
    """ create.html view """
    template = loader.get_template('PyBoard/create/create.html')
    f = TopicForm()

    if request.method == 'POST':
        f = TopicForm(request.POST)
        now_time = timezone.now()
        if f.is_valid():
            t = Topic(
                title=f.cleaned_data['title'],
                register_name=request.user.username,
                register_datetime=now_time,
                update_name=request.user.username,
                update_datetime=now_time
            )
            t.save()
            td = TopicDetail(
                title=t,
                text=f.cleaned_data['text'],
                register_name=request.user.username,
                register_datetime=now_time,
                update_name=request.user.username,
                update_datetime=now_time
            )
            td.save()
            return redirect('PyBoard:index')
    context = {
        'signin_username': request.user.username,
        'form': f,
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url='PyBoard:signin')
def reply(request, topic_id, text_no=0):
    """ reply.html view """
    template = loader.get_template('PyBoard/reply/reply.html')

    if request.method == 'POST':
        f = ReplyForm(request.POST)
        now_time = timezone.now()
        if f.is_valid():
            t = Topic.objects.get(pk=topic_id)
            max_no = TopicDetail.objects.filter(title=t).aggregate(Max('text_no'))['text_no__max']
            max_no = int(max_no) + 1
            td = TopicDetail(
                title=t,
                text=f.cleaned_data['text'],
                text_no = max_no,
                register_name=request.user.username,
                register_datetime=now_time,
                update_name=request.user.username,
                update_datetime=now_time
            )
            td.save()
            t.update_datetime = now_time
            t.save()
            return redirect('PyBoard:detail', topic_id)
    else:
        t = Topic.objects.get(pk=topic_id)
        topic_title = t.title
        rep_text = TopicDetail.objects.get(title=t, text_no=text_no).text
        rep_text = '> ' + rep_text
        rep_text = rep_text.replace('\n', '\n> ')
        f = ReplyForm(initial={'text':rep_text})

    context = {
        'signin_username': request.user.username,
        'form': f,
        'topic_title': topic_title,
        'topic_id': topic_id,
    }
    return HttpResponse(template.render(context, request))

def signin(request):
    """ signin.html view """
    template = loader.get_template('PyBoard/signin/signin.html')
    f = AccountForm()
    error_message = ''

    if request.method == 'POST':
        f = AccountForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user:
            if user.is_active:
                auth.login(request, user)
                return redirect('PyBoard:index')
            else:
                error_message = 'そのユーザーは現在使用できません。'
        else:
            error_message = 'ユーザー名またはパスワードが異なります。'
    context = {
        'signin_username': request.user.username,
        'form': f,
        'error_message' : error_message,
    }
    return HttpResponse(template.render(context, request))

def signout(request):
    """ signout.html view """
    auth.logout(request)
    return redirect('PyBoard:index')

def signup(request):
    """ signup.html view """
    template = loader.get_template('PyBoard/signup/signup.html')
    f = AccountForm()
    error_message = ''

    if request.method == 'POST':
        f = AccountForm(request.POST)
        if f.is_valid():
            try:
                user = User.objects.create_user(
                    username=f.cleaned_data['username'],
                    password=f.cleaned_data['password'],
                )
                user.save()
                return redirect('PyBoard:signin')
            except IntegrityError:
                # ユーザー重複チェック
                error_message = 'そのユーザー名は既に使われています。'

    context = {
        'signin_username': request.user.username,
        'form': f,
        'error_message' : error_message,
    }
    return HttpResponse(template.render(context, request))

