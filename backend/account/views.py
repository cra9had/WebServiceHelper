from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser


class CreateRegisterLink(APIView):
    permission_classes = (IsAdminUser,)

    def post(self):
        pass        
