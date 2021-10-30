import os
import aip

def ocr_basic(file):
    app_id = 'xxxxxxxx'
    api_key = 'xxxxxxxxxxxxxxxxxxxxx'
    secret_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    ocr_text = ''
    if os.path.isfile(file):
        with open(file, 'rb') as f:
            image = f.read()
        ocr_ret = aip.AipOcr(app_id, api_key, secret_key).basicGeneral(image)
        words = ocr_ret.get('words_result')
        print(words)
        if words is not None and len(words):
            for word in words:
                ocr_text += word['words'] + ' '
            return ocr_text
    return None

def ocr_handwrite(file):
    app_id = 'xxxxxxxx'
    api_key = 'xxxxxxxxxxxxxxxxxxxxx'
    secret_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    ocr_text = ''
    if os.path.isfile(file):
        with open(file, 'rb') as f:
            image = f.read()
        ocr_ret = aip.AipOcr(app_id, api_key, secret_key).handwriting(image)
        words = ocr_ret.get('words_result')
        print(words)
        if words is not None and len(words):
            for word in words:
                ocr_text += word['words'] + ' '
            return ocr_text
    return None