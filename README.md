# OneRingTranslator_SillyTavern

### Установка (RU)

#### Изменить настройки (options/Core.json)
```
{
    "allow_multithread": true,
    "api_keys_allowed": [],
    "cache_is_use": true,
    "cache_per_model": true,
    "cache_save_every": 5,
    "debug_input_output": false,
    "default_from_lang": "ru",
    "default_to_lang": "en",
    "default_translate_plugin": "custom_libre_translate",
    "init_on_start": "",
    "user_lang": "",
    "v": "1.5"
}
```
#### Переместить плагин в plugins/custom_libre_translate.py
#### Нстроить plugin_custom_libre_translate.json:
```
{
    "custom_url": "YOUR URL TO LIBRE TRANSLATE \ EXAMPLE: http://192.168.0.124:5555/",
    "v": "1.0"
}
```

### Install (ENG)

#### Change Settings (options/Core.json)
```
{
    "allow_multithread": true,
    "api_keys_allowed": [],
    "cache_is_use": true,
    "cache_per_model": true,
    "cache_save_every": 5,
    "debug_input_output": false,
    "default_from_lang": "Your Language \ EXAPMPLE: ru",
    "default_to_lang": "en",
    "default_translate_plugin": "custom_libre_translate",
    "init_on_start": "",
    "user_lang": "",
    "v": "1.5"
}
```
#### Move plugin to plugins/custom_libre_translate.py
#### Change Settings in plugin_custom_libre_translate.json:
```
{
    "custom_url": "YOUR URL TO LIBRE TRANSLATE \ EXAMPLE: http://192.168.0.124:5555/",
    "v": "1.0"
}
```
