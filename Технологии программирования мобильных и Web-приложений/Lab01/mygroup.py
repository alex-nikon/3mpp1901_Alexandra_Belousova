groupmates = [
    {
        "name": "Михаил",
        "surname": "Каргальцев",
        "exams": ["Информатика", "История", "Философия"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Илья",
        "surname": "Галузинский",
        "exams": ["История", "Математика", "ИЗО"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Павел",
        "surname": "Петрушенков",
        "exams": ["Философия", "ИЗО", "Физкультура"],
        "marks": [4, 5, 5]
    },
        {
        "name": "Екатерина",
        "surname": "Иванова",
        "exams": ["Физкультура", "Информатика", "Музыка"],
        "marks": [3, 5, 5]
    },
        {
        "name": "Роман",
        "surname": "Нохрин",
        "exams": ["Алгебра", "Геометрия", "Физика"],
        "marks": [5, 5, 5]
    },
        {
        "name": "Ефим",
        "surname": "Андреев",
        "exams": ["Философия", "Физика", "ИЗО"],
        "marks": [5, 5, 4]
    }
]

def print_av_score(marks):
    return 0 if not marks else sum(marks) / len(marks)

av_score = int(input())

def print_av_score_print_students(students, av_score):
    for student in students:
        if print_av_score(student["marks"]) > av_score:
            print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))

print_av_score_print_students(groupmates, av_score)