from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Topic, TopicDetail

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
        'topics': topic_list,
    }

    return HttpResponse(template.render(context, request))

def about(request):
    """ about.html view """
    template = loader.get_template('PyBoard/about/about.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def contact(request):
    """ contact.html view """
    template = loader.get_template('PyBoard/contact/contact.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def detail(request, topic_id):
    """ detail.html view """
    template = loader.get_template('PyBoard/detail/detail.html')
    topic_title = Topic.objects.get(pk=topic_id).title
    topic_detail_list = TopicDetail.objects.filter(title=topic_id).order_by('register_datetime')
    context = {
        'topic_title': topic_title,
        'topic_details': topic_detail_list,
    }
    return HttpResponse(template.render(context, request))

def create(request):
    """ create.html view """
    template = loader.get_template('PyBoard/create/create.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def reply(request, topic_id):
    """ reply.html view """
    template = loader.get_template('PyBoard/reply/reply.html')
    context = {
    }
    return HttpResponse(template.render(context, request))
