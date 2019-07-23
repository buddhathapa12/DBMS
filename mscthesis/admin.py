from django.contrib import admin

from .models import Student
from .models import Thesis
from .models import Area
from .models import Supervisor
from .models import Status
from .models import Submission

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Student,StudentAdmin)

class ThesisAdmin(admin.ModelAdmin):
    pass
admin.site.register(Thesis,ThesisAdmin)

class AreaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Area,AreaAdmin)

class SubmissionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Submission,SubmissionAdmin)

class SupervisorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Supervisor,SupervisorAdmin)

class StatusAdmin(admin.ModelAdmin):
    pass
admin.site.register(Status,StatusAdmin)

