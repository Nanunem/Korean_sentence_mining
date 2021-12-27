import requests

class Audio:
    """
    Download and save the audio of a specific date
    """
    root_path = "https://learn.dict.naver.com/dictPronunciation.dict?filePaths="
    def __init__(self, url_audio):
        self.url_audio = url_audio

    def audio_search(self, mp3_file_name):
        url_source = self.root_path + self.url_audio
        content_source = requests.get(url_source).json()
        url_mp3 = content_source['url'][0]
        mp3 = requests.get(url_mp3)
        with open(mp3_file_name + ".mp3", 'wb') as Mp3File:
            Mp3File.write(mp3.content)
