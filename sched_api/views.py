from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from sched_api.models import Subject
from sched_api.serializers import SubjectSerializer

# Create your views here.
@csrf_exempt
def subject_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SubjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def subject_detail(request, pk):
    """
    Retrieve, update or delete a subject.
    """
    try:
        subject = Subject.objects.get(pk=pk)
    except Subject.DoesNotExist:
        return HttpResponse(status=404)

    # Subject object already obtained, now process according to request
    if request.method == 'GET':
        serializer = SubjectSerializer(subject)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SubjectSerializer(subject, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        subject.delete()
        return HttpResponse(status=204)
