# MADE WITH HEART 💛 BY SAEPUL BAHRI - 202200402277 - TI22I
from sys import platform
from time import sleep
import os


def clear_display():
    if platform == "linux" or platform == "linux2":
        os.system('clear')
    elif platform == "darwin":
        os.system('cls')
    elif platform == "win32":
        os.system('cls')


def display_grade(grades):
    s_len = 68
    pattern = "{:<3} {:<20} {:<8} {:<15} {:<0}"

    print('=' * s_len)
    print(pattern.format('NO', 'MAJOR', 'GRADE', 'LETTER VALUE', 'PREDICATE'))

    for idx, grade in enumerate(grades):
        result = check_grade(grade=grade['grade'])
        major = grade['major'].capitalize()
        grade_lv = result[0]
        predicate = result[1]

        print('-' * s_len)
        # Print index, major, grade in letter value and predicate
        print(pattern.format(idx + 1, major,
              grade['grade'], grade_lv, predicate))
        print('-' * s_len)


# Check the grades and return a tuple consisting of
# grade in letter value, and predicate
def check_grade(grade):
    if grade >= 90 and grade <= 100:
        return ('A', 'With compliments')
    elif grade >= 80 and grade <= 89:
        return ('B', 'Very satisfy')
    elif grade >= 70 and grade <= 79:
        return ('C', 'Satisfying')
    elif grade >= 60 and grade <= 69:
        return ('D', 'Not satisfactory')
    elif grade >= 0 and grade <= 59:
        return ('E', 'Not pass')
    else:
        return ('Error', 'Invalid grade value')


def get_grade():
    grades = []

    # Tell the user how to exit the form
    print("Enter 'e' of 'E' to exit form")

    while True:
        gradeInput = {}
        major = input('Enter course name: ')

        # Exit the form if the user inserted 'E' for the value
        if major.lower() == 'e':
            break

        grade = input('Enter your grade: ')

        # Fancy separator
        print('----------------------------')

        # Check the validity of the input given and if true append it to grade
        if grade.isnumeric() and not major.isnumeric():
            gradeInput['major'] = major
            gradeInput['grade'] = float(grade)
            grades.append(gradeInput)
        else:
            print('TYPEERROR: you entered wrong data type for major or grade.\nExpected a string for major and a numeric value for grade!')

    clear_display()
    return grades


def main():
    grades = get_grade()
    if len(grades):
        display_grade(grades=grades)
    else:
        print('You have not inserted any data')
        sleep(1)
        print('Closing the app')


main()
