from rest_framework import viewsets, response, status

from myapp.models import Roles
from myapp.searializers import RolesSerializer


class RoleViewSet(viewsets.ModelViewSet):
    '''
    Contains information about a command-line Unix program.
    '''
    queryset = Roles.objects.all()
    lookup_field = 'id'
    serializer_class = RolesSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.get_serializer().destroy(instance)
        print("Instance destroyed!")
        return response.Response(status=status.HTTP_204_NO_CONTENT)