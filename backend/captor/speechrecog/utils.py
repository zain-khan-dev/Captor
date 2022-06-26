from speechrecog.serializers import AudioResponse
from vosk import Model, KaldiRecognizer, SetLogLevel
import sys
import os
import wave
import subprocess
import json


def parseAudioFile(file):
    SetLogLevel(0)

    sample_rate=16000
    model = Model(lang="en-us")

    rec = KaldiRecognizer(model, sample_rate)

    process = subprocess.Popen(['ffmpeg', '-loglevel', 'quiet', '-i',
                                file.temporary_file_path(),
                                '-ar', str(sample_rate) , '-ac', '1', '-f', 's16le', '-'],
                                stdout=subprocess.PIPE)


    rec.SetWords(True)
    rec.SetPartialWords(True)

    result = []
    while True:

        data = process.stdout.read(4000)

        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            
            result.append(rec.Result())

        else:
            rec.PartialResult()

    parsedTimeStampWords = []

    for data in result:
        sentence = json.loads(data)["result"]
        for words in sentence:
            parsedTimeStampWords.append(dict(start_ts = float(round(words["start"],2)), end_ts = float(round(words["end"],2)), word = words["word"]))


    return parsedTimeStampWords
