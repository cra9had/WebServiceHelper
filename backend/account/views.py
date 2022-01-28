from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .services.registration import is_link_valid, create_user
from .serializers import RegisterUserSerializer, RegisterPageSerializer
from .exceptions import UserAlreadyExist, URLHashDoesNotExist


class RegisterPageView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterPageSerializer

    def post(self, request) -> Response:
        serializer = RegisterPageSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.validate(request.data)
            if is_link_valid(data["url_hash"]):
                return Response({}, status=status.HTTP_200_OK)
        return Response({}, status=status.HTTP_404_NOT_FOUND)


class RegisterAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterUserSerializer

    def post(self, request) -> Response:
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.validate(request.data)
            print(data)
            try:
                token = create_user(data["username"], data["email"], data["password"], data["url_hash"])
                return Response({"token": token}, status=status.HTTP_200_OK)
            except UserAlreadyExist:
                return Response({"error_message": "Username or email is already exist"},
                                status=status.HTTP_400_BAD_REQUEST)
            except URLHashDoesNotExist:
                pass

        return Response({}, status=status.HTTP_404_NOT_FOUND)
