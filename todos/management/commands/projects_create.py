from django.core.management.base import BaseCommand
from todos.models import Project, ToDo
from users.models import User


class Command(BaseCommand):
    help = 'Create Projects with ToDos'

    def add_arguments(self, parser):
        parser.add_argument('projects_count', type=int)
        parser.add_argument('todos_count', type=int)

    def handle(self, *args, **options):
        Project.objects.all().delete()
        projects_count = options['projects_count']
        todos_count = options['todos_count']
        for i in range(projects_count):
            project = Project.objects.create(name=f'Project-{i}', description=f'Description of project {i}')
            project.authors.set(User.objects.filter(username='admin'))
            project.save()
            author = User.objects.get(username='admin')
            for j in range(todos_count):
                todo = ToDo.objects.create(name=f'ToDo-p{i}-{j}',
                                           description=f'Todo {j} for project {i}',
                                           project=project,
                                           author=author)
            print(f'project {project} created')
        print('done')
