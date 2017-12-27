from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from sched_api.models import Subject
from sched_api.serializers import SubjectSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def subject_list(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SubjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def subject_detail(request, pk, format=None):
    """
    Retrieve, update or delete a subject.
    """
    try:
        subject = Subject.objects.get(pk=pk)
    except Subject.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    # Subject object already obtained, now process according to request
    if request.method == 'GET':
        serializer = SubjectSerializer(subject)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SubjectSerializer(subject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        subject.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
