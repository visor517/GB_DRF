from django.core.management.base import BaseCommand
from todos.models import Project
from users.models import User


class Command(BaseCommand):
    help = 'Create Projects with ToDos'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **options):
        Project.objects.all().delete()
        count = options['count']
        for i in range(count):
            project = Project.objects.create(name=f'Project-{i}', description=f'Description of project {i}')
            project.authors.set(User.objects.filter(username='admin'))
            print(f'project {project} created')
        print('done')
