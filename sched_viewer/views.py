from django.shortcuts import render
from django.http import HttpResponse
from crs.schedule_parser import *

# Create your views here.

def index(request):
    crs_parser = CRSScheduleParser()
    subjects = crs_parser.get_by_search("CS 180")
    return HttpResponse("Hello, world. You're at the schedule index." +
                str(subjects[0])
            )
