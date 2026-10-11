


PASS_MARK = 40

def calculate_average(marks):
    total = 0
    for mark in marks:
        total += mark
    return total / len(marks)

def is_passing(mark):
    return mark >= PASS_MARK

def get_grade(average):
    if average >= 90:
        return "Distinction"
    elif average >= 60:
        return "First"
    elif average >= 45:
        return "Second"
    else:
        return "Fail"
