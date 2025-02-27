# Libre Translate plugin
# author: Vladislav Janvarev

from oneringcore import OneRingCore
import os
import re

modname = os.path.basename(__file__)[:-3] # calculating modname

# start function
def start(core:OneRingCore):
    manifest = { # plugin settings
        "name": "Custom Libre Translator", # name
        "version": "1.0", # version

        "default_options": {
            "custom_url": "http://192.168.0.124:5555/",  # mirror for LibreTranslator service
        },

        "translate": {
            "custom_libre_translate": (init,translate) # 1 function - init, 2 - translate
        }
    }
    return manifest

def start_with_options(core:OneRingCore, manifest:dict):
    pass
def init(core:OneRingCore):
    pass

def translate(core:OneRingCore, text:str, from_lang:str = "", to_lang:str = "", add_params:str = ""):
    from deep_translator import LibreTranslator
    custom_url = core.plugin_options(modname).get("custom_url")
    #print(custom_url)
    Text = text
    Result = ""
    for TextLine in Text.split("\n"):
        for TextElement in re.findall("""[^ *\"()][A-ZА-Яa-zа-я ,.:'!-]{2,}[^ *\"()]""", TextLine):
            TextLine = TextLine.replace(TextElement, LibreTranslator(source=from_lang, target=to_lang, custom_url=custom_url, api_key = "no_api_key").translate(TextElement))
        Result += TextLine + "\n"
    return Result
