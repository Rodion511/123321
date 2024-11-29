# Проект на Tkinter: Приветствие, вычисления и работа с файлами

Этот проект представляет собой графическое приложение на Python с использованием библиотеки tkinter. Программа предоставляет несколько функций для взаимодействия с пользователем:

## Функции приложения

1. Приветствие пользователя/
   Пользователь вводит своё имя, и программа отображает приветственное сообщение. Если имя не введено, появляется предупреждение.



2. Арифметические вычисления:
   Программа выполняет арифметические операции (сумма, разность, умножение, деление) с двумя числами, введёнными пользователем. В случае ошибки (например, если введены нечисловые данные) выводится предупреждение.

3. Генерация случайных чисел:
   Программа генерирует 10 случайных чисел от 1 до 100 и отображает их на экране.

4. Поиск минимального и максимального значения:
   Программа находит минимальное и максимальное значение среди сгенерированных случайных чисел и отображает их.

5. Создание файлов с случайными числами:
   Программа создаёт три текстовых файла, каждый из которых содержит 10 случайных чисел. Файлы сохраняются в папке random_files.

6. Открытие файлов и отображение их содержимого:
   Пользователь может выбрать текстовый файл из папки random_files, и программа отобразит его содержимое.

## Структура проекта

- app.py — основной файл программы, содержащий логику приложения.
- random_files/ — папка, в которой хранятся созданные файлы с случайными числами.
- README.md — файл с инструкцией по запуску и описанием проекта.

## Инструкция по запуску

1. Установите Python:
   Убедитесь, что у вас установлен Python версии 3.6 или выше. 

2. **Установите библиотеку tkinter**:
   Библиотека tkinter должна быть установлена по умолчанию в большинстве дистрибутивов Python. Если она не установлена, выполните команду:
   `bash
   pip install tk