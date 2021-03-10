import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class OrderFilter(django_filters.FilterSet):
    # start_date = DateFilter(field_name="date_created", lookup_expr='gte')
    # end_date = DateFilter(field_name="date_created", lookup_expr='lte')
    note = CharFilter(field_name="note", lookup_expr='icontains')
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['student', 'room', 'date_created', 'repair_date']

class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = ['student_id']

class MaintenanceOrderFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        fields = ['work_order', 'dorm']
