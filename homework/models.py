from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=99)

    def __str__(self):
        return 'департамент ' + str(self.name)


class Experimenter(models.Model):
    name = models.CharField(max_length=99)
    name_department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return 'эксперементатор ' + str(self.name)


class Laboratory(models.Model):
    name = models.CharField(max_length=99)
    description = models.CharField(max_length=99)

    def __str__(self):
        return 'лаборатория ' + str(self.name)


class Sample(models.Model):
    name = models.CharField(max_length=99)
    code = models.IntegerField(default=0)

    def __str__(self):
        return 'образец ' + str(self.name) + ' код: ' + str(self.code)


class Experiment(models.Model):
    name = models.CharField(max_length=99)
    laboratory = models.ForeignKey(Laboratory, on_delete=models.CASCADE)
    sample = models.ManyToManyField(Sample, blank=True)
    experimenter = models.ManyToManyField(Experimenter, blank=True)

    def __str__(self):
        return 'эксперимент ' + str(self.name)