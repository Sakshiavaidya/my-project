from rest_framework import viewsets, permissions
from .models import Project
from .serializers import ProjectSerializer, ProjectCreateSerializer
from rest_framework.response import Response
from rest_framework import status
from clients.models import Client

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.action == 'list':
            return self.request.user.projects.all()
        return Project.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return ProjectCreateSerializer
        return ProjectSerializer

    def perform_create(self, serializer):
        client_id = self.kwargs.get('client_id')
        client = Client.objects.get(id=client_id)
        serializer.save(created_by=self.request.user, client=client)
