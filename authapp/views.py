from django.shortcuts import render
from rest_framework import status
from rest_framework.response  import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from authapp.models import user
from django.http import JsonResponse
from authapp.serializers import userserializer

# Created your class based views here.
class userAPI(APIView):
    def get(self, request):
        try:
            namelist = user.objects.all()
        except user.DoesNotExist:
            return Response({'error':'NOT FOUND'}, status=status.HTTP_404_NOT_FOUND)
        serializer =  userserializer(namelist, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def post(self, request):
        serializer =  userserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)
#Created  class based views for put and delete views here.
class putAPI(APIView):
        def get(self, request, pk):
            try:
                namelist = user.objects.get(pk=pk)
            except user.DoesNotExist:
                return Response({'error':'NOT FOUND'}, status=status.HTTP_404_NOT_FOUND)
            serializer =  userserializer(namelist)
            return Response(serializer.data)

        def put(self, request, pk):
            namelist = user.objects.get(pk=pk)
            serializer =  userserializer(namelist, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors)

        def delete(self, request, pk):
            namelist  = user.objects.get(pk=pk)
            namelist.delete()
            return Response()
## Created without restframework views.
# def  home(request):
#     return render(request, 'home.html')

# def authuser(request):
#     uname = user.objects.all()
#     # print(uname)
#     data = {
#         'uname' : list(uname.values())
#     }
#     return JsonResponse(data)

# def authjson(request, pk):
#     list = user.objects.get(pk = pk)
#     data = {
#         'name' : list.name,
#         'role' : list.role,
#         'company' : list.company,
#         'discription' : list.discription,
#         'active' : list.active
#     }
#     return JsonResponse(data)

 #using rest_framework api_view function
# Created your function based views here.
   #GET method 
@api_view(['GET', 'POST'])
def getuser(request):
    if request.method == 'GET':
        namelist = user.objects.all()
        serializer =  userserializer(namelist, many=True)
        return Response(serializer.data)
#POST method
    if request.method  ==  'POST':
        serializer =  userserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)
    

@api_view(['GET', 'PUT','DELETE'])
def userlist(request, pk):
    if request.method == "GET":
        try:
            namelist = user.objects.get(pk=pk)
        except user.DoesNotExist:
            return Response({'error':'NOT FOUND'}, status=status.HTTP_404_NOT_FOUND)

        serializer =  userserializer(namelist)
        return Response(serializer.data)

    if request.method  ==  'PUT':
        userlist = user.objects.get(pk=pk)
        serializer =  userserializer(userlist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    if request.method  ==  'DELETE':
        namelist  = user.objects.get(pk=pk)
        namelist.delete()
        return Response()
