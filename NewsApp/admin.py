from django.contrib import admin
from .models import Student

# Register your models here.




class AdminStudent(admin.ModelAdmin):
    model = Student
    list_display=('name','age','email','website')
    search_fields = ('name','age','email','website')

admin.site.register(Student, AdminStudent)

#admin.site.register(Student)
