from rest_framework import viewsets,permissions

from leads.models import Lead
from .serializers import userSerializer


class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    permission_classes = [
      permissions.AllowAny
    ]
    
    serializer_class = userSerializer