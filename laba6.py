import tkinter as tk 
from tkinter import messagebox, filedialog 
import random 
import os
import requests  # импортируем библиотеку для работы с запросами

# Ваш API ключ OpenWeatherMap
API_KEY = "YOUR_API_KEY"

def get_weather():
    """ Функция для получения погоды в Ульяновске с помощью OpenWeatherMap API. """
    url = f"http://api.openweathermap.org/data/2.5/weather?q=Ulyanovsk&appid={API_KEY}&units=metric&lang=ru"
    try:
        response = requests.get(url)
        data = response.json()
        
        if data["cod"] == 200:
            temp = data["main"]["temp"]
            description = data["weather"][0]["description"]
            weather_info = f"Температура: {temp}°C\nОписание: {description.capitalize()}"
            label_weather.config(text=weather_info)
        else:
            messagebox.showerror("Ошибка", "Не удалось получить данные о погоде.")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Ошибка", f"Ошибка сети: {e}")

# Инициализация главного окна
root = tk.Tk()
root.geometry("1200x1000")
root.configure(bg="#f5f5dc")

# Добавляем виджет для погоды
button_weather = tk.Button(
    root,
    text="Получить погоду в Ульяновске",
    command=get_weather,
    font=("Arial", 12, "bold"),
    bg="#7ddabf",
    fg="white",
    bd=3
)
button_weather.pack(pady=10)

label_weather = tk.Label(root, text="", font=("Arial", 14), bg="#f5f5dc")
label_weather.pack(pady=10)

root.mainloop()