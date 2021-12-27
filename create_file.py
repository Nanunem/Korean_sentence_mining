from get_audio import Audio
from get_content import Text


class Download:
    """
    Download of the audio and text asociated to a date (dialogue and/or examples)
    """
    def __init__(self, user_request):
        self.user_request = user_request

    def download(self, dates):
        for num, item in enumerate(self.user_request):
            print(f"Downloading of the {dates[num]} files (text and audio)")
            item = item.upper()
            text = Text(dates[num])
            content = text.text_search()
            folder_path = "files_created"

            # Downloading both dialogues and example sentences
            if "ALL" in item.upper():
                print(f"Downloading both dialogues and example sentences")
                dialogue_number = len(content['sentences'])
                for i in range(1, dialogue_number+1):
                    audio = Audio(content['sentences'][i-1]['sentence_pron_file'])
                    audio.audio_search(f"{folder_path}/dialogue_{dates[num]}_{str(i)}")
                    with open(f"{folder_path}/dialogue_{dates[num]}_{str(i)}.txt", "w", encoding="utf-8") as output_file :
                        output_file.write(str(content['sentences'][i-1]['sentence']))

                example_number = len(content['studys'][0]['examples'])
                for i in range(1, example_number+1):
                    audio = Audio(content['studys'][0]['examples'][i-1]['pron_file_url'])
                    audio.audio_search(f"{folder_path}/exemple_{dates[num]}_{str(i)}")
                    with open(f"{folder_path}/exemple_{dates[num]}_{str(i)}.txt", "w", encoding="utf-8") as output_file:
                        output_file.write(content['studys'][0]['title'])
                        output_file.write("\n")
                        output_file.write(content['studys'][0]['translation'])
                        output_file.write("\n")
                        output_file.write(content['studys'][0]['examples'][i-1]['example'])

            elif "DIAL" in item.upper():
                print(f"Downloading the dialogues")
                # Downloading only the dialogues (not the example sentences)
                dialogue_number = len(content['sentences'])
                for i in range(1, dialogue_number+1):
                    audio = Audio(content['sentences'][i-1]['sentence_pron_file'])
                    audio.audio_search(f"{folder_path}/dialogue_{dates[num]}_{str(i)}")
                    with open(f"{folder_path}/dialogue_{dates[num]}_{str(i)}.txt", "w", encoding="utf-8") as output_file :
                        output_file.write(content['sentences'][i-1]['sentence'])

            elif "EXAM" in item.upper():
                print(f"Downloading the example sentences")
                # Downloading the example sentences (not the dialogues)
                example_number = len(content['studys'][0]['examples'])
                for i in range(1, example_number+1):
                    audio = Audio(content['studys'][0]['examples'][i-1]['pron_file_url'])
                    audio.audio_search(f"{folder_path}/exemple_{dates[num]}_{str(i)}")
                    with open(f"{folder_path}/exemple_{dates[num]}_{str(i)}.txt", "w", encoding="utf-8") as output_file:
                        output_file.write(content['studys'][0]['title'])
                        output_file.write("\n")
                        output_file.write(content['studys'][0]['translation'])
                        output_file.write("\n")
                        output_file.write(content['studys'][0]['examples'][i-1]['example'])

            else:
                print("Error, please put \"ALL\", \"DIALogue\" ou \"EXAMple\"")