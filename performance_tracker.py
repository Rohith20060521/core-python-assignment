import math

def calculate_single_average(marks):
    if not marks:
        return 0.0
    return round(sum(marks) / len(marks), 2)

def track_performance(students_data):
    average_marks = {}
    top_performer = None
    highest_average = -1.0
    for student_name, marks_list in students_data.items():
        current_average = calculate_single_average(marks_list)
        average_marks[student_name] = current_average
        if current_average > highest_average:
            highest_average = current_average
            top_performer = student_name
        elif current_average == highest_average:
            pass
    return average_marks, top_performer
students = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}
average_results, top_student = track_performance(students)
print(f"Average Marks: {average_results}")
print(f"Top Performer: \"{top_student}\"")