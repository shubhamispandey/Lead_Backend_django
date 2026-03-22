from rest_framework.viewsets import ModelViewSet
from .models import Lead
from .serializers import LeadSerializer
from rest_framework.permissions import IsAuthenticated

class LeadViewSet(ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_queryset(self):
        return Lead.objects.filter(created_by=self.request.user)