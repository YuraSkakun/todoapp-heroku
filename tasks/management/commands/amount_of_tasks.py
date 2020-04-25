# coding: utf-8

from django.core.management import BaseCommand

from tasks.models import TodoItem
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = u"Displays all users\'tasks"

    def add_arguments(self, parser):
        parser.add_argument('--amount', dest='amount', type=int, default=3)

    def handle(self, *args, **options):   
        count = options['amount']     
        for u in User.objects.all():
        	for t in u.tasks.all()[:count]:
        		print('user:{} task:{}'.format(u, t))
        	print('********')

