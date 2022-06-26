from rest_framework import serializers



class AudioSerializer(serializers.Serializer):
    audio_file = serializers.FileField()



class AudioResponse(serializers.Serializer):
    start_ts = serializers.DecimalField(max_digits=8, decimal_places=2)
    end_ts = serializers.DecimalField(max_digits=8, decimal_places=2)
    word = serializers.CharField()


