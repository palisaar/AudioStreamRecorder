import urllib.request
import datetime
import threading

'''
Autor: Lennart Palisaar
20211638
'''


# threading
def record_audio(name, url, recording_length, bg):
    t = threading.Thread(target=startrec, args=(name, url, recording_length, bg))
    t.start()


# eigentlicher recoder
def startrec(name, url, recording_length, bg):
    target_file_name = name + '.mp3'

    audio_src = urllib.request.urlopen(url)

    audio_dest = open(target_file_name, 'wb')  # wb = "write binary"

    start_time = datetime.datetime.now()

    while (datetime.datetime.now() - start_time).seconds < recording_length:
        audio_dest.write(audio_src.read(bg))
    print('recording is done')
    audio_dest.close()


class AudioRecorder:
    def __init__(self):
        pass