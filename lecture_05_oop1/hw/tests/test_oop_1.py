import datetime
from unittest.mock import MagicMock

import pytest
from hw.oop_1 import Homework, Student, Teacher


@pytest.mark.parametrize('text', ['oop', '123', 'Teacher', '\00bx'])
def test_homework_text(text):
    homework = Homework(text, deadline=7)
    assert homework.text == text


@pytest.mark.parametrize('time', [1, 2, 3, 100])
def test_homework(time):
    homework = Homework('no matters', deadline=time)
    assert homework.deadline == datetime.timedelta(days=time)


@pytest.mark.parametrize('time', [2, 5, 10, 100])
def test_homework_is_active(time, monkeypatch):
    homework = Homework(text='oop', deadline=4)
    homework.created = datetime.datetime(2021, 1, 1, 0, 0, 0)

    datetime_mock = MagicMock(wrap=datetime.datetime)
    datetime_mock.now.return_value = datetime.datetime(2021, 1, 3, 0, 0, 0)
    monkeypatch.setattr(datetime, 'datetime', datetime_mock)

    assert homework.is_active()


@pytest.mark.parametrize('first_name, last_name', [('Ivan', 'Petrov'), ('Artur', 'Jack')])
def test_student_name(first_name, last_name):
    student = Student(first_name=first_name, last_name=last_name)
    assert student.first_name + student.last_name == first_name + last_name


@pytest.mark.parametrize('first_name, last_name, time', [('Ivan', 'Petrov', 5), ('Artur', 'Jack', 10)])
def test_student_homework_is_done(first_name, last_name, time, monkeypatch):
    student = Student(first_name=first_name, last_name=last_name)

    homework = Homework('some_text', deadline=time)
    homework.created = datetime.datetime(2021, 1, 1, 0, 0, 0)

    datetime_mock = MagicMock(wrap=datetime.datetime)
    datetime_mock.now.return_value = datetime.datetime(2021, 1, 3, 0, 0, 0)
    monkeypatch.setattr(datetime, 'datetime', datetime_mock)

    assert student.do_homework(homework) == homework


@pytest.mark.parametrize('first_name, last_name, time', [('Ivan', 'Petrov', 5), ('Artur', 'Jack', 10)])
def test_student_homework_is_not_done(first_name, last_name, time, monkeypatch, capsys):
    student = Student(first_name=first_name, last_name=last_name)

    homework = Homework('some_text', deadline=time)
    homework.created = datetime.datetime(2021, 1, 1, 0, 0, 0)

    datetime_mock = MagicMock(wrap=datetime.datetime)
    datetime_mock.now.return_value = datetime.datetime(2021, 1, 11, 0, 0, 0)
    monkeypatch.setattr(datetime, 'datetime', datetime_mock)

    assert student.do_homework(homework) is None
    out, _ = capsys.readouterr()
    assert out == 'You are late\n'


@pytest.mark.parametrize('first_name, last_name', [('Galina', 'Petrovna'), ('Olga', 'Ivanovna')])
def test_teacher_name(first_name, last_name):
    teacher = Teacher(first_name=first_name, last_name=last_name)
    assert teacher.first_name + teacher.last_name == first_name + last_name


@pytest.mark.parametrize('first_name, last_name, text, deadline',
                         [('Ivan', 'Petrov', 'eng', 5), ('Artur', 'Jack', 'math', 10)])
def test_teacher_create_homework_text(first_name, last_name, text, deadline):
    teacher = Teacher(first_name=first_name, last_name=last_name)
    homework_from_teacher = teacher.create_homework(text, deadline)
    assert homework_from_teacher.text == text


@pytest.mark.parametrize('first_name, last_name, text, time',
                         [('Ivan', 'Petrov', 'eng', 5), ('Artur', 'Jack', 'math', 10)])
def test_teacher_create_homework_deadline(first_name, last_name, text, time):
    teacher = Teacher(first_name=first_name, last_name=last_name)
    homework_from_teacher = teacher.create_homework(text, time)
    assert homework_from_teacher.deadline == datetime.timedelta(days=time)
