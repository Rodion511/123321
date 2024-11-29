import tkinter as tk
from tkinter import messagebox, filedialog
import random
import os

# Привет
def greet():
    """
    Функция для приветствия пользователя. Отображает сообщение с введённым именем.
    Если имя не введено, появляется предупреждение.
    """
    name = entry_name.get()
    if name:
        messagebox.showinfo("Приветствие", f"Привет, {name}!")
    else:
        messagebox.showwarning("Ошибка", "Введите имя")

# Сумма
def calculate():
    """
    Функция для выполнения арифметических операций (сумма, разность, умножение, деление) 
    с двумя числами, введёнными пользователем. Выводит результаты вычислений.
    В случае ошибки (нечисловые данные) появляется предупреждение.
    """
    try:
        num1 = float(entry_num1.get())  
        num2 = float(entry_num2.get())  
        addition = num1 + num2
        subtraction = num1 - num2
        multiplication = num1 * num2
        division = num1 / num2 if num2 != 0 else "Деление на 0!"
        result_message = (
            f"Сумма: {addition}\n"
            f"Разность: {subtraction}\n"
            f"Умножение: {multiplication}\n"
            f"Деление: {division}"
        )
        messagebox.showinfo("Результаты вычислений", result_message)
    except ValueError:
        messagebox.showwarning("Ошибка", "Введите корректные числа!")

# Рандом
random_numbers = []
def generate_random_numbers():
    """
    Функция для генерации 10 случайных чисел от 1 до 100 и отображения их в интерфейсе.
    """
    global random_numbers
    random_numbers = [random.randint(1, 100) for _ in range(10)]
    label_random_numbers.config(
        text=f"Сгенерированные числа: {', '.join(map(str, random_numbers))}"
    )

def find_min_max():
    """
    Функция для поиска минимального и максимального чисел из списка сгенерированных случайных чисел.
    Если список пуст, появляется предупреждение.
    """
    if random_numbers:
        minimum = min(random_numbers)
        maximum = max(random_numbers)
        messagebox.showinfo("Минимум и Максимум", f"Минимум: {minimum}\nМаксимум: {maximum}")
    else:
        messagebox.showwarning("Ошибка", "Сначала сгенерируйте числа!")

# Файл
def generate_files_with_random_numbers():
    """
    Функция для создания 3 файлов, каждый из которых содержит 10 случайных чисел от 1 до 100.
    Файлы сохраняются в папке "random_files".
    """
    folder = "random_files"
    os.makedirs(folder, exist_ok=True)
    for i in range(1, 4):
        numbers = random.sample(range(1, 101), 10)
        file_path = os.path.join(folder, f"file_{i}.txt")
        with open(file_path, "w") as f:
            f.write("\n".join(map(str, numbers)))
    messagebox.showinfo("Файлы созданы", "Три файла с уникальными числами успешно созданы!")

# Открываем файл
def open_file_and_display_content():
    """
    Функция для открытия выбранного пользователем текстового файла и отображения его содержимого.
    """
    file_path = filedialog.askopenfilename(
        initialdir="random_files",
        title="Выберите файл",
        filetypes=(("Текстовые файлы", "*.txt"), ("Все файлы", "*.*"))
    )
    if file_path:
        with open(file_path, "r") as f:
            content = f.read()
        messagebox.showinfo("Содержимое файла", content)

# Инициализация главного окна
root = tk.Tk()
root.geometry("1200x1000")
root.configure(bg="#f5f5dc")

# Привет
label_name = tk.Label(root, text="Введите имя:", font=("Arial", 12), bg="#f5f5dc")
label_name.pack(pady=10)
entry_name = tk.Entry(root, font=("Arial", 12), width=25, bd=2, relief="groove")
entry_name.pack(pady=5)
button_greet = tk.Button(
    root,
    text="Приветствовать",
    command=greet,
    font=("Arial", 12, "bold"),
    bg="#7ddabf",
    fg="white",
    bd=3
)
button_greet.pack(pady=10)

# Сложение
label_num1 = tk.Label(root, text="Введите первое число:", font=("Arial", 12), bg="#f5f5dc")
label_num1.pack(pady=10)
entry_num1 = tk.Entry(root, font=("Arial", 12), width=25, bd=2, relief="groove")
entry_num1.pack(pady=5)
label_num2 = tk.Label(root, text="Введите второе число:", font=("Arial", 12), bg="#f5f5dc")
label_num2.pack(pady=10)
entry_num2 = tk.Entry(root, font=("Arial", 12), width=25, bd=2, relief="groove")
entry_num2.pack(pady=5)
button_calculate = tk.Button(
    root,
    text="Вычислить",
    command=calculate,
    font=("Arial", 12, "bold"),
    bg="#7ddabf",
    fg="white",
    bd=3
)
button_calculate.pack(pady=20)

# Рандом
label_random_numbers = tk.Label(root, text="", font=("Arial", 12), bg="#f5f5dc")
label_random_numbers.pack(pady=10)
button_generate_numbers = tk.Button(
    root,
    text="Сгенерировать числа",
    command=generate_random_numbers,
    font=("Arial", 12, "bold"), 
    bg="#7ddabf",
    fg="white",
    bd=3
)
button_generate_numbers.pack(pady=10)
button_find_min_max = tk.Button(
    root,
    text="Найти минимум и максимум",
    command=find_min_max,
    font=("Arial", 12, "bold"),
    bg="#7ddabf",
    fg="white",
    bd=3
)
button_find_min_max.pack(pady=10)

# Файлы
button_generate_files = tk.Button(
    root,
    text="Создать файлы с числами",
    command=generate_files_with_random_numbers,
    font=("Arial", 12, "bold"),
    bg="#7ddabf",
    fg="white",
    bd=3
)
button_generate_files.pack(pady=20)

button_open_file = tk.Button(
    root,
    text="Открыть файл",
    command=open_file_and_display_content,
    font=("Arial", 12, "bold"),
    bg="#7ddabf",
    fg="white",
    bd=3
)
button_open_file.pack(pady=20)

root.mainloop()