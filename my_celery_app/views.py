from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .tasks import add, create_status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from celery.result import AsyncResult
from django.http import JsonResponse
from .serializers import *


@csrf_exempt
@api_view(['POST'])
def adding(request):
    result = add.delay(5, 3)
    print(f'Task ID: {result.id}')
    return JsonResponse({'task_id': result.id})


@csrf_exempt
@api_view(['GET'])
def check_task_status(request):
    task_id = request.GET.get('task_id')
    # task_id = request.query_params.get('task_id')
    print(task_id)
    if not task_id:
        return JsonResponse({'error': 'No task_id provided'}, status=400)
    try:
        result = AsyncResult(task_id)
        if result.ready():
            return JsonResponse({'status': result.status, 'result': result.result})
        else:
            return JsonResponse({'status': result.status, 'result': None})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


class CandidateSet(APIView):

    def post(self, request):
        try:
            serializer = CandidateSerializer(data=request.data)
            if serializer.is_valid():
                candidate = serializer.save()
                print(candidate.id)
                status_set(candidate.id)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=400)


def status_set(cid):
    candidateId = cid
    try:
        candidate_status = create_status.delay(candidateId)
        print(candidate_status)
        return candidate_status
    except Exception as e:
        print(e)
        return None

