from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.core.validators import RegexValidator

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

class Student(models.Model):
    DORM_NAME = (
        ('AA', 'AA'),
        ('BB', 'BB'),
        ('CC', 'CC'),
        ('DD', 'DD'),
        ('EE', 'EE'),
        ('FF', 'FF'),
        ('Gabriel V', 'Gabriel V'),
        ('Rosaria V', 'Rosaria V'),
        ('Aisha Kande', 'Aisha Kande'),
    )

    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    student_id = models.CharField(max_length=9, validators=[alphanumeric], null=True)
    email = models.EmailField(max_length=50, null=True, unique=True)
    dorm = models.CharField(max_length=50, null=True,  choices=DORM_NAME, blank=True)
    room = models.IntegerField(null=True)
    phone = models.CharField(max_length=11, null=True)
    profile_pic = models.ImageField(default='arab.png', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.name)

class OrderWorker(models.Model):
    staff = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=50, null=True)
    job = models.CharField(max_length=50, null=True)

    def __str__(self):
        return '{} - {}'.format(self.staff, self.job)

class WorkOrder(models.Model):
    CATEGORY = (
        ('AC', 'AC'),
        ('Electricity', 'Electicity'),
        ('Plumbing', 'Plumbing'),
        ('Wright Repair', 'Wright Repair'),
        ('Other', 'Other'),
    )

    order_name = models.CharField(max_length=50, null=True)
    category = models.CharField(max_length=50, null=True,  choices=CATEGORY, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    order_worker = models.ForeignKey(OrderWorker, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.order_name

class Order(models.Model):
    DORM_NAME = (
        ('AA', 'AA'),
        ('BB', 'BB'),
        ('CC', 'CC'),
        ('DD', 'DD'),
        ('EE', 'EE'),
        ('FF', 'FF'),
        ('Gabriel V', 'Gabriel V'),
        ('Rosaria V', 'Rosaria V'),
        ('Aisha Kande', 'Aisha Kande'),
    )

    STATUS = (
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Order Done', 'Order Done'),
    )

    student = models.ForeignKey(Student, null=True, blank=True, on_delete=models.SET_NULL)
    work_order = models.ForeignKey(WorkOrder, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    dorm = models.CharField(max_length=50, null=True,  choices=DORM_NAME, blank=True)
    room = models.IntegerField(null=True)
    status = models.CharField(max_length=50, null=True, blank=True, choices=STATUS, default='Pending')
    note = models.TextField(max_length=200, null=True)
    repair_date = models.CharField(max_length=20, null=True, blank=True)
    # user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return "{}'s {} order".format(self.student.name, self.work_order)
        # return str(self.work_order)
