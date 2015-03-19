from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.core import serializers
from conference.models import Teacher, Time


def time_setup(request):
    # teacher_list_json = request.GET['ids']
    teacher_list = serializers.deserialize('json', stream_or_string='stream')
    return HttpResponse(teacher_list)