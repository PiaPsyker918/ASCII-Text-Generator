# ASCII-Text-Generator
Генерирует ASCII-текст из обычного текста.

<img width="1211" height="250" alt="ASCIITEXTGENERATORLogo" src="https://github.com/user-attachments/assets/3bf2acac-b1e6-411d-9782-c93731c02f6e" />

```(Скрипт в настоящее время находится в раннем доступе. Если вы обнаружили ошибку, пожалуйста, напишите мне.)```

# Переводы

Английская версия: [English](https://github.com/PiaPsyker918/ASCII-Text-Generator/tree/main/)

# Требования

```

pyfiglet

```

# Установка

1. Установите ZIP-файл

2. Откройте CMD и напишите:
 
```pip install pyfiglet```

3. Следующие шаги в разделе "Как использовать"

# Как использовать

В командной строке напишите

Windows:

```
.\Generator.py
```

Linux:

```
$ ./Generator.py
```

Затем введите текст
и выберите шрифт

# Как это работает

```
                        _|_|  _|            _|              _|
_|_|_|    _|    _|    _|            _|_|_|  _|    _|_|    _|_|_|_|
_|    _|  _|    _|  _|_|_|_|  _|  _|    _|  _|  _|_|_|_|    _|
_|    _|  _|    _|    _|      _|  _|    _|  _|  _|          _|
_|_|_|      _|_|_|    _|      _|    _|_|_|  _|    _|_|_|      _|_|
_|              _|                      _|
_|          _|_|                    _|_|
```

```pyfiglet - это полный порт FIGlet (http://www.figlet.org/) на чистый Python. Он принимает ASCII-текст и отображает его в шрифтах ASCII-арта (как заголовок выше, который использует шрифт 'block').``` ~ Автор Pyfiglet (cjones)

Это на самом деле очень просто, в отличие от ASCII-Video-Generator, потому что ничего не обрабатывается компьютерным зрением или чем-то подобным. Он работает "из коробки".

# Статус упаковки

<img width="205" height="1285" alt="image" src="https://github.com/user-attachments/assets/4bb1c143-446c-40eb-acd6-47212eabd303" />

# Простое использование

```
from pyfiglet import Figlet
f = Figlet(font='slant')
print(f.renderText('текст для преобразования'))
```
или
```
import pyfiglet
f = pyfiglet.figlet_format("текст для преобразования", font="slant")
print(f)
```

# Контакты

[<img width="100" height="100" alt="telegram-circle-icon-for-web-design-free-png" src="https://github.com/user-attachments/assets/1e4c0cb3-a856-417b-86d1-29354b2d92a8" />](https://t.me/Girlanda228)
