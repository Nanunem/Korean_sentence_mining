from get_audio import Audio
from get_content import Text
import os

class Download:
    """
    Download of the audio and text asociated to a date (dialogue and/or examples)
    """
    folder_path = "files_created"
    def __init__(self, user_request):
        self.user_request = user_request

    def _check_files_folder(self):
        if os.path.isdir(self.folder_path):
            pass
        else:
            os.mkdir(self.folder_path)

    def _get_dialogue(self, content, date):
        self._check_files_folder()
        dialogue_number = len(content['sentences'])
        for i in range(1, dialogue_number + 1):
            audio = Audio(content['sentences'][i - 1]['sentence_pron_file'])
            audio.audio_search(f"{self.folder_path}/dialogue_{date}_{str(i)}")
            with open(f"{self.folder_path}/dialogue_{date}_{str(i)}.txt", "w", encoding="utf-8") as output_file:
                output_file.write(str(content['sentences'][i - 1]['sentence']))

    def _get_example(self, content, date):
        self._check_files_folder()
        example_number = len(content['studys'][0]['examples'])
        for i in range(1, example_number + 1):
            audio = Audio(content['studys'][0]['examples'][i - 1]['pron_file_url'])
            audio.audio_search(f"{self.folder_path}/exemple_{date}_{str(i)}")
            with open(f"{self.folder_path}/exemple_{date}_{str(i)}.txt", "w", encoding="utf-8") as output_file:
                output_file.write(content['studys'][0]['title'])
                output_file.write("\n")
                output_file.write(content['studys'][0]['translation'])
                output_file.write("\n")
                output_file.write(content['studys'][0]['examples'][i - 1]['example'])

    def download(self, dates):
        for num, item in enumerate(self.user_request):
            print(f"Downloading of the {dates[num]} files (text and audio)")
            item = item.upper()
            text = Text(dates[num])
            content = text.text_search()

            # Downloading both dialogues and example sentences
            if "ALL" in item.upper():
                print(f"Downloading both dialogues and example sentences\n")
                self._get_dialogue(content, dates[num])
                self._get_example(content, dates[num])

            elif "DIAL" in item.upper():
                print(f"Downloading the dialogues\n")
                # Downloading only the dialogues (not the example sentences)
                self._get_dialogue(content, dates[num])

            elif "EXAM" in item.upper():
                print(f"Downloading the example sentences\n")
                # Downloading the example sentences (not the dialogues)
                self._get_example(content, dates[num])

            else:
                print("Error, please put \"ALL\", \"DIALogue\" ou \"EXAMple\"")