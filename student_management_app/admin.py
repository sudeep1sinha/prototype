from django.contrib import admin
from .models import Subjects , AdminHOD , Courses , Students 
# Register your models here.



admin.site.register(Subjects)
admin.site.register(AdminHOD)
admin.site.register(Courses)
admin.site.register(Students)