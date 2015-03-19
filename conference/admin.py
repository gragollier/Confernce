from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from django.core import serializers
from conference.models import Teacher, Time


class TimeInLine(admin.TabularInline):
    model = Time
    extra = 5


class TeacherAdmin(admin.ModelAdmin):
    fields = ('teacher_name',)
    inlines = [TimeInLine]
    '''
    actions = ['time_range_add']
    def time_range_add(self, request, queryset):
        response = HttpResponseRedirect('/time_setup/')
        serializers.serialize('json', queryset, stream=response)
        return response

    def time_range_add(self, request, queryset):
        # selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)  # Serializer works better taking all the data
        serialized_data = serializers.serialize('json', queryset)  # Therefore the deserializer separates the data
        print(queryset)
        # print(serialized_data)
        return HttpResponseRedirect("/time_setup/?ids=%s" % serialized_data)
    '''





admin.site.register(Teacher, TeacherAdmin)