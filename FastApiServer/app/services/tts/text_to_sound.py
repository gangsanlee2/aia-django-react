import os
import webbrowser
from glob import glob
from io import BytesIO

from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play


def tts(word, toSlow=True):
    tts = gTTS(text=word, lang="ko", slow=toSlow)
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)

    # simpleaudio가 있어야 작동한다.
    song = AudioSegment.from_file(fp, format="mp3")
    play(song)

    # ffcache 파일이 생성돼서 glob wild card로 전부 삭제
    fileList = glob("./ffcache*")
    for filePath in fileList:
        os.remove(filePath)


if __name__ == "__main__":
    """tts = gTTS('나는 한국말을 합니다.', lang='ko', tld='com.au')
    tts.save('hello_kor.mp3')
    webbrowser.open("hello_kor.mp3")"""
    tts_en = gTTS('hello', lang='en')
    tts_fr = gTTS('bonjour', lang='fr')
    with open('hello_bonjour.mp3', 'wb') as f:
        tts_en.write_to_fp(f)
        tts_fr.write_to_fp(f)