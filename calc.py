# Input format: 100

# On the 5.0 scale:
# Honors: +0.5
# AP/IB/College: +1
# A = 4.0, B = 3.0, C = 2.0, D = 1.0, F = 0.0
# - = -0.3, + = +0.3

# How to read Birdville ISD transcript:
# Q/H: Pre-AP/Honors
# D: College Dual Credit
# J: Completed in junior high/middle I think?
# P: AP
# R: summer I think? It doesn't matter for weighting.

# At "Semesters: " enter -1 to exit

def convert(grade):
    if grade >= 90:
        converted = 4.0
    elif grade >= 80:
        converted = 3.0
    elif grade >= 70:
        converted = 2.0
    elif grade >= 65:
        converted = 1.0
    else:
        converted = 0.0

    if grade % 10 >= 7:
        converted += 0.3
    elif grade % 10 <= 3:
        converted -= 0.3

    return converted


print('When you want to exit, put -1 semesters.')
grades = []
while True:
    semesters = int(input('Semesters: '))
    if semesters == -1:
        break

    course_grades = []
    for _ in range(semesters):
        grade = int(input('Grade: '))
        course_grades.append(grade)
    grade = sum(course_grades) / len(course_grades)

    print('Course type:')
    print('1) Regular')
    print('2) PreAP/Honors')
    print('3) AP/IB/College')
    weight = int(input('Type: '))
    if weight == 1:
        weight = 0
    elif weight == 2:
        weight = 0.5
    else:
        weight = 1
    grades.append([convert(grade), weight])
    print()

unweighted_gpa = (sum([grade[0] for grade in grades]) / len(grades))
weighted_gpa = (sum([grade[0] + grade[1] for grade in grades]) / len(grades))
print(f'Unweighted: {unweighted_gpa} (rounded: {unweighted_gpa:.1f})')
print(f'Weighted: {weighted_gpa} (rounded: {weighted_gpa:.1f})')
