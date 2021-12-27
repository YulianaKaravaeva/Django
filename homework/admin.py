from django.contrib import admin
from homework.models import Department, Experiment, Laboratory, Sample, Experimenter


admin.site.register(Department)
admin.site.register(Experiment)
admin.site.register(Laboratory)
admin.site.register(Sample)
admin.site.register(Experimenter)