from django.db import models


class Teacher(models.Model):
    teacher_name = models.CharField(max_length=64)  # 64 seemed big enough

    def __str__(self):
        return self.teacher_name


class Time(models.Model):
    teacher_name = models.ForeignKey(Teacher)  # Each time is owned by a teacher
    time = models.DateTimeField()
    time_available = models.BooleanField(default=True)  # By default all times are available
    reserved_by = models.CharField(max_length=64, default="None")  # By default no times are owned

    def __str__(self):
        return str(self.time)