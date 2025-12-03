import sys

# Исходный список студентов
groupmates = [
    {
        "name": "Евпатий",
        "surname": "Простоквашин",
        "exams": ["Алхимия", "Земледелие", "История"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Персефона",
        "surname": "Тринидадская",
        "exams": ["Музыка", "Теология", "Флюидология"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Изяслав",
        "surname": "Мироедус",
        "exams": ["Грамматика", "Инженерия", "История"],
        "marks": [5, 4, 5]
    },
    {
        "name": "Рейнальдо",
        "surname": "Шайтанбеков",
        "exams": ["История", "Атлетика", "Астрология"],
        "marks": [5, 4, 4]
    },
    {
        "name": "Айгуль",
        "surname": "Хротгарсон",
        "exams": ["Медицина", "Теология", "Земледелие"],
        "marks": [3, 3, 5]
    },
    {
        "name": "Варавва",
        "surname": "Мутелидзе",
        "exams": ["Астрология", "Право", "Геометрия"],
        "marks": [4, 4, 3]
    }
]

# Функция для вывода списка студентов
def print_students(students):
    header = ("Имя".ljust(15), "Фамилия".ljust(20), "Средний балл".ljust(15), "Экзамены".ljust(55), "Оценки".ljust(20))
    print(" | ".join(header))
    print("-" * 140)

    for student in students:
        # Вычисляем средний балл для текущего студента
        marks = student["marks"]
        if not marks:
            avg_mark = 0.0
        else:
            avg_mark = round(sum(marks) / len(marks), 2)
            
        row = (
            student["name"].ljust(15),
            student["surname"].ljust(20),
            str(avg_mark).ljust(15),
            str(student["exams"]).ljust(55),
            str(student["marks"]).ljust(20)
        )
        print(" | ".join(row))


# --- Основная функция для фильтрации (без изменений) ---
def filter_students_by_avg_mark(students, min_avg_mark):
    """
    Фильтрует студентов, чей средний балл выше заданного порога.
    """
    
    filtered_list = []
    
    for student in students:
        marks = student["marks"]
        if not marks:
            continue
            
        avg_mark = sum(marks) / len(marks)
        
        if avg_mark > min_avg_mark:
            filtered_list.append(student)
            
    return filtered_list


# --- Логика выполнения ---
def main():
    print("--- Список всех студентов ---")
    print_students(groupmates)
    print("-" * 140)

    # 1. Запрашиваем у пользователя минимальный средний балл
    while True:
        try:
            min_mark_input = float(input("\nВведите минимальный средний балл для фильтрации: "))
            
            if min_mark_input < 1 or min_mark_input > 5:
                 print("❗ Введите значение от 1 до 5.")
                 continue

            break
        except ValueError:
            print("❗ Некорректный ввод. Пожалуйста, введите число (например, 4 или 4.5).")

    # 2. Фильтруем студентов
    students_above_average = filter_students_by_avg_mark(groupmates, min_mark_input)

    # 3. Выводим результат
    print(f"\n--- Студенты, чей средний балл выше {min_mark_input} ---")

    if students_above_average:
        print_students(students_above_average)
    else:
        print(f"Пороговое значение {min_mark_input} слишком высоко. Ни один студент не удовлетворяет условию.")

if __name__ == "__main__":
    main()
