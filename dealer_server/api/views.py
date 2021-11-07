from rest_framework.decorators import api_view
from rest_framework.response import Response

from comms_logic import status
from comms_logic import status_helpers

# Create your views here.
@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        return Response(status.TEST)
    else:
        status_helpers.changeTest()
        return Response(status.TEST)
