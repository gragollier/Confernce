from django.core.management.base import BaseCommand, CommandError
from conference.models import Teacher, Time


class Command(BaseCommand):
    help = 'This command adds times in chosen interval to chosen teachers'

    def add_arguments(self, parser):
        parser.add_argument('teacher_id', nargs='+', type=int)

    def handle(self, *args, **options):
        for teacher_id in options['teacher_id']:
            try:
                teacher = Teacher.objects.get(pk=teacher_id)
            except Teacher.DoesNotExist:
                raise CommandError("Teacher %s doesn't exist" % teacher_id)
            else:
                self.stdout.write('%s exists' % teacher)