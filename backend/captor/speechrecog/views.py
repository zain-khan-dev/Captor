from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from speechrecog.serializers import AudioResponse, AudioSerializer
from rest_framework.views import APIView
from .utils import parseAudioFile

# Create your views here.



class get_audio_subtitles(APIView):

    serializer_class = AudioSerializer


    def post(self, request):
        print(request.FILES['audio_file'])
        audio_file = request.FILES['audio_file']
        parsedData = parseAudioFile(audio_file)
        audioResponse = AudioResponse(data=parsedData, many=True)
        # parseTranslation(request.F)
        if(audioResponse.is_valid()):
            return Response(audioResponse.data)
        print(audioResponse.errors)
        return Response("Error parsing audioResponse")
