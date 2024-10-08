from rest_framework import viewsets, permissions
from .models import Client
from .serializers import ClientSerializer, ClientDetailSerializer
from rest_framework.response import Response
from rest_framework import status

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ClientDetailSerializer
        return ClientSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
