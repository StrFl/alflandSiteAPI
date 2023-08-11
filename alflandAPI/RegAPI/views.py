from django.forms import model_to_dict
from django.http import HttpResponse
from rest_framework import generics, viewsets, mixins, status
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from .models import UserFields, SkinsFile

from .serializers import UserFieldsSerializer, MyFileSerializer, UserRegistrationSerializer
from datetime import datetime

import os


class RegAPIList(generics.ListCreateAPIView):
    queryset = UserFields.objects.all()
    serializer_class = UserFieldsSerializer




class FileUploadView(APIView):
    def post(self, request):
        file_serializer = MyFileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FileDownloadView(APIView):
    def get(self, request, file_id):
        try:
            file_obj = SkinsFile.objects.get(id=file_id)
            file_path = file_obj.file.path
            with open(file_path, 'rb') as f:
                response = HttpResponse(f.read(), content_type="application/octet-stream")
                response['Content-Disposition'] = 'attachment; filename="' + os.path.basename(file_path) + '"'
                return response
        except SkinsFile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)




class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'User registered successfully.'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class BalanceAPIView(APIView):
    # queryset = UserFields.objects.all()
    # serializer_class = UserFieldsSerializer

    # updActivity()

    # @action(methods=['post'], url_path='updBal', detail=True)
    # def post(self, request):
    #     try:

    #         ob = UserFields()
    #         ob.user_id = 1
    #         ob.balance = {
    #             "transactions": [].append({"transaction": request.bala, 'boughtObject': "string"}),
    #             "value": request.bala,
    #         }
    #         ob.save()
    #     except Exception:
    #         print("troble with bd balance")

    permission_classes = [IsAuthenticated]



    def get(self, request,transaction, boughtObject, format=None):
        user_fields = UserFields.objects.get(
            pk='372fd37e84a3427996f1d3a50eef3ef2')
        user_fields.balance = {
                 
                    "transactions": [{"transaction": 0, 'boughtObject': " "}],
                    "value": 0,
                }
            
        user_fields.save()
        return Response({'default'}, status=status.HTTP_200_OK)


    def post(self, request, transaction, boughtObject, format=None):
        # Retrieve the balance from the request data
        balance_data = transaction

        # Perform any data validation or manipulation if needed

        # Update the UserFields model with the new balance data    user_fields.balance.get('balance').get('transactions')
        user_fields = UserFields.objects.get(
            pk='372fd37e84a3427996f1d3a50eef3ef2')
        response_data = {'default'}
        

        try:
            user_fields.balance.get('transactions').append({"transaction": balance_data, 'boughtObject': str(boughtObject)})
            user_fields.balance = response_data = {
                 
                    "transactions": user_fields.balance.get('transactions'),
                    "value": balance_data,
                }
            

            user_fields.save()
        except Exception:
            print('-----------------------------------------------------')

        # Return the response in the desired format    .append({"transaction": balance_data, 'boughtObject': str(boughtObject)})

        return Response(response_data, status=status.HTTP_200_OK)
