import json
import os
import subprocess
import urllib.request
import uuid

# IAM token of your Yandex account
IAM_TOKEN = ('<TOKEN>')

# Folder ID of the Yandex service account
FOLDER_ID = '<ID>'


# A method that converts voice messages to text using the Yandex API
def speech_to_text(audio_file):
    # Reading the file for further processing
    with open(audio_file, 'rb') as file:
        data = file.read()

    # Processing Parameters
    params = '&'.join([
        'topic=general',
        "folderId=%s" % FOLDER_ID,
        'lang=ru-RU'
    ])

    # Sending a GET request to the Yandex API with the specified parameters and data
    url = urllib.request.Request('https://stt.api.cloud.yandex.net/speech/v1/stt:recognize?%s' % params, data=data)
    # Authentication via the IAM token
    url.add_header('Authorization', 'Bearer %s' % IAM_TOKEN)

    # Getting data and converting it to UTF-8 format
    responseData = urllib.request.urlopen(url).read().decode('UTF-8')
    decodedData = json.loads(responseData)

    # Returning a response
    if decodedData.get('error_code') is None:
        return decodedData.get('result')


# A method that converts various formats to OggOpus and converts speech to text
def convert(audio_file, input_extension, output_extension):
    # Creating a unique file name
    output_filename = uuid.uuid4().hex
    # Recording an audio file
    with open(output_filename + input_extension, 'wb') as file:
        file.write(audio_file.content)

    # Convert to OggOpus only if not already
    if input_extension != '.ogg':
        subprocess.call([
            'ffmpeg',
            '-i',
            f'{output_filename}{input_extension}',
            '-y',
            f'{output_filename}{output_extension}'
        ])

    # Converting speech to text and returning it
    text = speech_to_text(f'{output_filename}{output_extension}')

    # Clean up temporary files
    os.remove(f'{output_filename}{input_extension}')

    if input_extension != '.ogg':
        os.remove(f'{output_filename}{output_extension}')

    return text
