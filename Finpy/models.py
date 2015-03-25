from django.db import models

# Create your models here.


class Income(models.Model):

    salary = models.DecimalField('Salary', max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.salary)
