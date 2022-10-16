from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status

from internals.toolkit import response_creator
from internals.app import app


class ExampleView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        err = app.repository.example.create(request.data)
        if err:
            return err

        return response_creator(
            data='penalty added successfully.',
            status='success',
            status_code=status.HTTP_201_CREATED,
        )
