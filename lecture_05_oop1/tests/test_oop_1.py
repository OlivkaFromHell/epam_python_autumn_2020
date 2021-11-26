import datetime
from unittest.mock import Mock

import pytest
from hw.oop_1 import Homework, Student, Teacher


@pytest.mark.parametrize('text', ['oop', '123', 'Teacher', '\00bx'])
def test_homework_text(text):
    homework = Homework(text, days=7)
    assert homework.text == text


@pytest.mark.parametrize('time', [1, 2, 3, 100])
def test_homework(time):
    homework = Homework('no matters', days=time)
    assert homework.deadline == datetime.timedelta(days=time)


@pytest.mark.parametrize('time', [2, 5, 10, 100])
def test_homework_is_active(time):
    homework = Mock()
    homework.text = 'oop'
    homework.deadline = datetime.timedelta(days=time)
    homework.created = datetime.datetime(2021, 1, 1, 0, 0, 0)
    homework.is_active = datetime.datetime(2021, 1, 2, 0, 0, 0) - homework.deadline < homework.created

    assert homework.is_active


@pytest.mark.parametrize('first_name, last_name', [('Ivan', 'Petrov'), ('Artur', 'Jack')])
def test_student_name(first_name, last_name):
    student = Student(first_name=first_name, last_name=last_name)
    assert student.first_name + student.last_name == first_name + last_name


@pytest.mark.parametrize('first_name, last_name, time', [('Ivan', 'Petrov', 5), ('Artur', 'Jack', 10)])
def test_student_homework_is_done(first_name, last_name, time):
    student = Student(first_name=first_name, last_name=last_name)

    homework = Mock()
    homework.text = 'oop'
    homework.deadline = datetime.timedelta(days=time)
    homework.created = datetime.datetime(2021, 1, 1, 0, 0, 0)
    homework.is_active.return_value = datetime.datetime(2021, 1, 2, 0, 0, 0) - homework.deadline < homework.created

    assert student.do_homework(homework) == homework


@pytest.mark.parametrize('first_name, last_name, time', [('Ivan', 'Petrov', 5), ('Artur', 'Jack', 10)])
def test_student_homework_is_not_done(first_name, last_name, time):
    student = Student(first_name=first_name, last_name=last_name)

    homework = Mock()
    homework.text = 'oop'
    homework.deadline = datetime.timedelta(days=time)
    homework.created = datetime.datetime(2000, 1, 1, 0, 0, 0)
    homework.is_active.return_value = datetime.datetime(2021, 1, 2, 0, 0, 0) - homework.deadline < homework.created

    assert not student.do_homework(homework)


@pytest.mark.parametrize('first_name, last_name', [('Galina', 'Petrovna'), ('Olga', 'Ivanovna')])
def test_teacher_name(first_name, last_name):
    teacher = Teacher(first_name=first_name, last_name=last_name)
    assert teacher.first_name + teacher.last_name == first_name + last_name


@pytest.mark.parametrize('first_name, last_name, text, time',
                         [('Ivan', 'Petrov', 'eng', 5), ('Artur', 'Jack', 'math', 10)])
def test_teacher_create_homework(first_name, last_name, text, time):
    teacher = Teacher(first_name=first_name, last_name=last_name)

    assert teacher.create_homework(text, time).text == Homework(text, time).text
