import requests
import json
import pyperclip
from config import api_key

def ocr_space_file(filename, overlay=False, api_key=api_key, language='eng', engine=5):
    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               'OCREngine': engine,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r.content.decode()

def ocr_space_url(url, overlay=False, api_key=api_key, language='eng',engine=5):
    payload = {'url': url,
               'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               'OCREngine': engine,
               }
    r = requests.post('https://api.ocr.space/parse/image',
                      data=payload,
                      )
    return r.content.decode()

def get_ocr_results(url,engine) -> str:
    test_url = ocr_space_url(url=url,engine=engine)
    loads = json.loads(test_url)
    for l in loads['ParsedResults']:
        temp_text = l['ParsedText'].replace('\r\n', ' ').replace('\n',' ')
        return temp_text
    
if __name__ == '__main__':
    url = 'image_url'
    get_ocr_results(url,2)