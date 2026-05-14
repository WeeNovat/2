students = [
    (1, "Йолкін", [85, 90, 78]),
    (2, "Шевченко", [92, 88, 95]),
    (3, "Бусько", [40, 25, 1])
]

def get_student_info(record):

    sid, surname, grades = record
    return f"Студент: {surname}, ID: {sid}"

def calculate_average(data):
    all_grades = []
    for _, _, grades in data:
        all_grades.extend(grades)
    avg = sum(all_grades) / len(all_grades)
    return round(avg, 2)

print("--- Звіт по студентах ---")
for s in students:
    print(get_student_info(s))

print(f"\nЗагальний середній бал: {calculate_average(students)} балів")

print("\nСпроба змінити кортеж:")
try:
    students[0][0] = 99
except TypeError as e:
    print(f"Помилка: {e} (Кортеж незмінний!)")

students[0][2].append(100)
print(f"Але список оцінок змінити можна: {students[0]}")