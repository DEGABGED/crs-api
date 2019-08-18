from django.shortcuts import render
from django.http import HttpResponse
from crs_parser.parsers import CRSScheduleParser

# Create your views here.

def index(request):
    crs_parser = CRSScheduleParser()
    subjects = crs_parser.get_by_search("CS 17")
    return HttpResponse("<p>Hello, world. You're at the schedule index.</p>"
                        + "<ul><li>" 
                        + "</li><li>".join(list(map(str, subjects)))
                        + "</li></ul>"
            )
