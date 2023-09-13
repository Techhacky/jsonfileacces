import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import PriohubItem
from .serializers import PriohubItemSerializer

@api_view(['GET'])
def priohub_data(request):
    # Replace 'your_app' with the name of your app
    file_path = 'myapp/dwsample1-json.json'

    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            serializer = PriohubItemSerializer(data=data, many=True)
            if serializer.is_valid():
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=400)
    except FileNotFoundError:
        return Response({'error': 'priohub.json file not found'}, status=404)
