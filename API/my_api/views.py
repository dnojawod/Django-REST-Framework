from rest_framework.response import Response
from .models import Hero
from .serializer import HeroSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class heroes(APIView):
    permission_classes = [IsAuthenticated|ReadOnly]

    def get(self, request):
        if request.GET:
            id = request.GET.get('id')
            name = request.GET.get('name')
            alias = request.GET.get('alias')
            if id:
                heroes = Hero.objects.filter(id=id)
            elif name:
                heroes = Hero.objects.filter(name=name)
            elif alias:
                heroes = Hero.objects.filter(alias=alias)
        else:
            heroes = Hero.objects.all()
        serializer = HeroSerializer(heroes, many=True)
        return Response(serializer.data)

    def post(self, request):
        for entry in request.data:
            serializer = HeroSerializer(data=entry)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=400)
        return Response("Entries committed")

    def put(self, request):
        for entry in request.data:
            id = entry.get('id')
            heroes = Hero.objects.get(id=id)
            serializer = HeroSerializer(heroes, data=entry)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=400)
        return Response("Entries updated")

    def delete(self, request):
        if request.GET:
            id = request.GET.get('id')
            name = request.GET.get('name')
            alias = request.GET.get('alias')
            if id:
                heroes = Hero.objects.filter(id=id)
            elif name:
                heroes = Hero.objects.filter(name=name)
            elif alias:
                heroes = Hero.objects.filter(alias=alias)
            heroes.delete()
            return Response("Entries deleted", status=204)
        else:
            return Response("No parameter entered", status=404)
