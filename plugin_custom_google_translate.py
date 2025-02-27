# Google Translate plugin
# author: Vladislav Janvarev

from oneringcore import OneRingCore
import os
import re

modname = os.path.basename(__file__)[:-3] # calculating modname

# start function
def start(core:OneRingCore):
    manifest = { # plugin settings
        "name": "Custom Google Translate", # name
        "version": "1.0", # version

        "translate": {
            "custom_google_translate": (init,translate) # 1 function - init, 2 - translate
        }
    }
    return manifest

def init(core:OneRingCore):
    pass

def translate(core:OneRingCore, text:str, from_lang:str = "", to_lang:str = "", add_params:str = ""):
    # просто выводим текст в консоль
    from deep_translator import GoogleTranslator
    Text = text
    Result = ""
    for TextLine in Text.split("\n"):
        for TextElement in re.findall("""[^ *\"()][A-ZА-Яa-zа-я ,.:'!-]{2,}[^ *\"()]""", TextLine):
            TextLine = TextLine.replace(TextElement, GoogleTranslator(source=from_lang, target=to_lang).translate(TextElement))
        Result += TextLine + "\n"
    return Result
