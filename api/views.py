from rest_framework import viewsets
from rest_framework.response import Response

from api.models import HealthPlan, Query
from .serializers import QuerySerializer, UserDataSerializer
from .utils import interpret_query, generate_health_plan


class InterpretViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = QuerySerializer(data=request.data)
        if serializer.is_valid():
            query = serializer.validated_data['query']
            answer = interpret_query(query)

            query_instance = Query.objects.create(
                query=query,
                answer=answer
            )

            return Response({'answer': answer})
        return Response(serializer.errors, status=400)


class HealthPlanViewSet(viewsets.ViewSet):
    def create(self, request):
        medical_history = request.data.get('medical_history')
        if medical_history == '':
            medical_history = 'no'
            request.data['medical_history'] = medical_history

        serializer = UserDataSerializer(data=request.data)
        if serializer.is_valid():
            user_data = serializer.validated_data
            plan = generate_health_plan(user_data)

            HealthPlan.objects.create(
                age=user_data['age'],
                weight=user_data['weight'],
                medical_history=user_data['medical_history'],
                plan=plan
            )

            return Response({'health_plan': plan})
        return Response(serializer.errors, status=400)
