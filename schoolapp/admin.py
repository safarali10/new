from django.contrib import admin
from .models import Department
from .models import Course
from .models import Material


admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Material)

# Register your models here.