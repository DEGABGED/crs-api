from rest_framework import serializers
from sched_api.models import *

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('class_code', 'course', 'class_name', 'credits', 'schedule', 'instructor', 'remarks', 'slots_avail', 'slots_total', 'demand')
