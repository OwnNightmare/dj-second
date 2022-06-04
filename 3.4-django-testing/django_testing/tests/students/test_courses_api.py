import pytest
from rest_framework.test import APIClient

from students.models import Course, Student
from model_bakery import baker


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory


@pytest.mark.django_db
def test_get_python_course(client, course_factory, student_factory):
    # Arrange:
    students = student_factory(_quantity=5)
    courses = course_factory(_quantity=1, name='Python')
    # python = Course.objects.create(name='Python course')
    # python.students.create(name='Yura', birth_date='1995-10-16')

    # Act:
    course_id = courses[0].id
    response = client.get(f'/api/v1/courses/{course_id}/')
    data = response.json()

    # Assert
    assert response.status_code == 200
    assert data.get('name') == 'Python' and data['id'] == course_id


@pytest.mark.django_db
def test_get_all_courses(client, course_factory, student_factory):
    students = student_factory(_quantity=15)
    courses = course_factory(_quantity=20)

    response = client.get('/api/v1/courses/')
    data = response.json()

    assert 199 < response.status_code < 201
    assert len(data) == len(courses)
    for i, course in enumerate(data):
        assert course['name'] == courses[i].name


@pytest.mark.django_db
def test_get_course_by_name(client, course_factory, student_factory):
    courses = course_factory(_quantity=1, name='New_good_course')
    courses2 = course_factory(_quantity=1, name='New_good_course2')
    students = student_factory(_quantity=10)

    response = client.get('/api/v1/courses/', {'name': 'New_good_course2'})
    data = response.json()

    assert response.status_code == 200
    assert data[-1].get('name') == 'New_good_course2'


@pytest.mark.django_db
def test_get_courses_by_id(client, student_factory, course_factory):
    courses = course_factory(_quantity=10)
    # students = student_factory(_quantity=5)

    response = client.get('/api/v1/courses/')
    data = response.json()
    course_id = data[-1]['id']
    response_filtered = client.get('/api/v1/courses/', {'id': course_id})

    assert response.status_code == 200
    assert len(response.json()) == len(courses)

    assert response_filtered.status_code == 200
    assert len(response_filtered.json()) == 1

    assert response_filtered.json()[0]['id'] == course_id


@pytest.mark.django_db
def test_post_one_course(client, student_factory, course_factory):
    response_before = client.get('/api/v1/courses/')
    counter_before = len(response_before.json())

    student = Student.objects.create(name='Me', birth_date='1995-01-01')
    response_post = client.post('/api/v1/courses/', data={'name': 'Random course', 'student': student})
    response = client.get('/api/v1/courses/', {'student': student})

    response_after = client.get('/api/v1/courses/')
    counter_after = len(response_after.json())

    assert response_post.status_code == 201
    assert response_before.status_code == 200
    assert response_after.status_code == 200
    assert counter_after - counter_before == 1
    assert response.json()[0]['name'] == 'Random course'


@pytest.mark.django_db
def test_patch_one_course(client, student_factory, course_factory):

    student = Student.objects.create(name='Me', birth_date='1995-01-01')
    courses = course_factory(_quantity=1, name='Old course')

    course_id = courses[0].id
    response_get = client.get('/api/v1/courses/', {'id': course_id})

    new_name = 'Old course version 2.0'
    response_patch = client.patch(f'/api/v1/courses/{course_id}/', data={'name': new_name})

    data_before = response_get.json()
    response_patch_data = response_patch.json()

    assert response_get.status_code == 200
    assert response_patch.status_code == 200
    assert len(response_get.json()) == 1
    assert type(response_patch_data) == dict
    assert data_before[0]['name'] == 'Old course'
    assert response_patch_data['name'] == new_name


@pytest.mark.django_db
def test_delete_one_course(client, student_factory, course_factory):

    # good_course = Course.object.create(name='Useful course')
    course = course_factory(name='Bad course', )

    course_id = course.id
    response_before = client.get('/api/v1/courses/')
    course_amount_before = len(response_before.json())

    deleting_response = client.delete(f'/api/v1/courses/{course_id}/')

    response_after = client.get('/api/v1/courses/')
    course_amount_after = len(response_after.json())

    assert deleting_response.status_code == 204
    assert response_before.status_code == 200
    assert response_after.status_code == 200
    assert course_amount_after + 1 == course_amount_before


