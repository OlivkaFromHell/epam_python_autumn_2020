import datetime
from unittest.mock import MagicMock

import pytest
from hw.oop_2 import DeadlineError, Homework, HomeworkResult, Student, Teacher

# ---------------------------------
# |       TESTS FROM OOP_1        |
# ---------------------------------


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

    solution = 'solution'
    assert student.do_homework(homework, solution).homework == homework
    assert student.do_homework(homework, solution).solution == solution
    assert student.do_homework(homework, solution).author == student
    assert student.do_homework(homework, solution).created == datetime.datetime.now()


@pytest.mark.parametrize('first_name, last_name, time', [('Ivan', 'Petrov', 5), ('Artur', 'Jack', 10)])
def test_student_homework_is_not_done(first_name, last_name, time, monkeypatch, capsys):
    student = Student(first_name=first_name, last_name=last_name)

    homework = Homework('some_text', deadline=time)
    homework.created = datetime.datetime(2021, 1, 1, 0, 0, 0)

    datetime_mock = MagicMock(wrap=datetime.datetime)
    datetime_mock.now.return_value = datetime.datetime(2021, 1, 11, 0, 0, 0)
    monkeypatch.setattr(datetime, 'datetime', datetime_mock)

    with pytest.raises(DeadlineError):
        student.do_homework(homework, 'solution')


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


# ---------------------------------
# |       TESTS FOR OOP_2        |
# ---------------------------------


@pytest.mark.parametrize('first_name, last_name, time', [('Ivan', 'Petrov', 5), ('Artur', 'Jack', 10)])
def test_student_do_homework_return_homeworkresult(first_name, last_name, time, monkeypatch):
    student = Student(first_name=first_name, last_name=last_name)

    homework = Homework('some_text', deadline=time)
    homework.created = datetime.datetime(2021, 1, 1, 0, 0, 0)

    datetime_mock = MagicMock(wrap=datetime.datetime)
    datetime_mock.now.return_value = datetime.datetime(2021, 1, 3, 0, 0, 0)
    monkeypatch.setattr(datetime, 'datetime', datetime_mock)

    solution = 'solution'
    assert isinstance(student.do_homework(homework, solution), HomeworkResult)


def test_check_homework():
    new_teacher = Teacher('Ilya', 'Shadrin')
    old_teacher = Teacher('Viktor', 'Smetanin')

    lazy_student = Student('Ivan', 'Petrov')
    good_student = Student('Sergei', 'Sokolov')

    oop_hw = new_teacher.create_homework('Learn OOP', 1)
    docs_hw = old_teacher.create_homework('Read docs', 5)

    result_1 = good_student.do_homework(oop_hw, 'I have done this hw')
    result_2 = good_student.do_homework(docs_hw, 'I have done this hw too')
    result_3 = lazy_student.do_homework(docs_hw, 'done')

    new_teacher.check_homework(result_1)
    new_teacher.check_homework(result_2)
    new_teacher.check_homework(result_3)

    assert len(Teacher.homework_done) == 2


def test_check_homework_where_solution_less_5_symbols():
    old_teacher = Teacher('Viktor', 'Smetanin')
    lazy_student = Student('Ivan', 'Petrov')

    oop_hw = old_teacher.create_homework('Learn OOP', 1)

    result = lazy_student.do_homework(oop_hw, 'done')

    assert not old_teacher.check_homework(result)


def test_check_homework_with_same_result():
    # (нужно гаранитровать остутствие повторяющихся результатов по каждому
    # заданию)
    Teacher.reset_results()
    new_teacher = Teacher('Ilya', 'Shadrin')
    old_teacher = Teacher('Viktor', 'Smetanin')
    lazy_student = Student('Ivan', 'Petrov')

    oop_hw = old_teacher.create_homework('Learn OOP', 2)
    result = lazy_student.do_homework(oop_hw, 'I have done this hw')

    old_teacher.check_homework(result)
    new_teacher.check_homework(result)
    print(Teacher.homework_done)
    assert Teacher.homework_done == {result.homework: [result]}


def test_check_homework_with_different_students():
    # проверка, что новая homework не сотрет старую
    Teacher.reset_results()
    new_teacher = Teacher('Ilya', 'Shadrin')
    old_teacher = Teacher('Viktor', 'Smetanin')

    lazy_student = Student('Ivan', 'Petrov')
    good_student = Student('Sergei', 'Sokolov')

    docs_hw = old_teacher.create_homework('Read docs', 5)

    result_1 = good_student.do_homework(docs_hw, 'I have done this hw too')
    result_2 = lazy_student.do_homework(docs_hw, 'Homework is done')

    new_teacher.check_homework(result_1)
    new_teacher.check_homework(result_2)
    print('\n', Teacher.homework_done)
    assert len(Teacher.homework_done[docs_hw]) == 2


def test_homework_done_is_global_for_all_instances():

    teacher = Teacher('Viktor', 'Smetanin')
    student = Student('Ivan', 'Petrov')

    oop_hw = teacher.create_homework('Learn OOP', 1)
    result = student.do_homework(oop_hw, 'I have done this hw')
    teacher.check_homework(result)

    temp_1 = teacher.homework_done
    temp_2 = Teacher.homework_done

    assert temp_1 is temp_2


def test_teacher_reset_results():

    teacher = Teacher('Ivan', 'Smetanin')
    student = Student('Ivan', 'Petrov')

    oop_hw = teacher.create_homework('Learn OOP', 1)
    result = student.do_homework(oop_hw, 'I have done this hw')

    teacher.check_homework(result)
    Teacher.reset_results()

    assert len(Teacher.homework_done) == 0
