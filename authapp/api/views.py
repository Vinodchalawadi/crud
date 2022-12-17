from rest_framework.response  import Response 
from authapp.models import user
from rest_framework.decorators import api_view
from authapp.api.serializers import userserializer

@api_view()
def getuser(request):
    namelist = user.objects.all()
    serializer =  userserializer(namelist)
    return Response(serializer.data)


@api_view()
def userlist(request, pk):
    namelist = user.objects.all(pk=pk)
    serializer =  userserializer(namelist)
    return Response(serializer.data)