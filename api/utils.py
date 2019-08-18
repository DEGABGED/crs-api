import json
from cacheback.decorators import cacheback
from crs_parser.parsers import CRSScheduleParser
from api.serializers import SubjectSerializer

@cacheback(lifetime=60, fetch_on_miss=False)
def fetch_subjects(search):
    # Fetches subjects from the CRS Parser by term, as well as saves it in the database
    parser = CRSScheduleParser()
    results = parser.get_by_search(search)

    for result in map(lambda x: x.toJSON(), results):
        serializer = SubjectSerializer(data=json.loads(result))
        if serializer.is_valid():
            serializer.save()

    return search