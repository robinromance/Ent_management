import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Ent_management.settings")
django.setup()
from faker import Faker
from Ent_item.models import *
from random import *

myfake = Faker()

def popular(n):
    for i in range(n):
        S_name = myfake.name()
        S_class = randint(1,12)
        S_address = myfake.address()
        Student_record = Student.objects.get_or_create(s_name = S_name, s_class = S_class, s_address = S_address)
popular(30)