from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from conference.models import Teacher, Time
from django.core.urlresolvers import reverse


def index(request):  # Index page, asks for Parent and Child's name
    return render(request, 'conference/index.html')


def teacher_redirect(request):
    if request.POST['student'] and request.POST['parent']:  # Makes sure both fields are filled out then
        request.session['student'] = request.POST['student']  # saves them to the session for use later
        request.session['parent'] = request.POST['parent']
        return HttpResponseRedirect(reverse('conference:teacher'))
    else:
        return render(request, 'conference/index.html', {'error_message': "Please fill in both fields"})


class TeacherView(generic.ListView):  # Lists all teachers
    model = Teacher
    context_object_name = 'teacher_list'
    template_name = 'conference/teacher.html'


class TimeView(generic.DetailView):  # Lists all times for certain teacher
    model = Teacher
    template_name = 'conference/time.html'
    context_object_name = 'time_list'


def vote(request, pk):  # Sets chosen time to owned by the user via session
    selected_time = get_object_or_404(Time, pk=pk)
    selected_time.time_available = False
    selected_time.reserved_by = request.session['parent']
    selected_time.save()
    return HttpResponseRedirect(reverse('conference:teacher'))