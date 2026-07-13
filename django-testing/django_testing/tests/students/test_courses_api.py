import pytest

from students.models import Course, Student


@pytest.mark.django_db
def test_retrieve_course(api_client, course_factory):
    course = course_factory(_model=Course, name='Test Course')
    
    url = f'/api/v1/courses/{course.id}/'
    response = api_client.get(url)
    
    assert response.status_code == 200
    assert response.data['id'] == course.id
    assert response.data['name'] == course.name


@pytest.mark.django_db
def test_list_courses(api_client, course_factory):
    course1 = course_factory(_model=Course, name='Course 1')
    course2 = course_factory(_model=Course, name='Course 2')
    
    url = '/api/v1/courses/'
    response = api_client.get(url)
    
    assert response.status_code == 200
    assert len(response.data) == 2
    assert response.data[0]['id'] == course1.id
    assert response.data[1]['id'] == course2.id


@pytest.mark.django_db
def test_filter_courses_by_id(api_client, course_factory):
    course1 = course_factory(_model=Course, name='Course 1')
    course2 = course_factory(_model=Course, name='Course 2')
    
    url = f'/api/v1/courses/?id={course1.id}'
    response = api_client.get(url)
    
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['id'] == course1.id


@pytest.mark.django_db
def test_filter_courses_by_name(api_client, course_factory):
    course1 = course_factory(_model=Course, name='Python Course')
    course2 = course_factory(_model=Course, name='JavaScript Course')
    
    url = '/api/v1/courses/?name=Python'
    response = api_client.get(url)
    
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['name'] == 'Python Course'


@pytest.mark.django_db
def test_create_course(api_client):
    data = {'name': 'New Course'}
    
    url = '/api/v1/courses/'
    response = api_client.post(url, data)
    
    assert response.status_code == 201
    assert Course.objects.filter(name='New Course').exists()


@pytest.mark.django_db
def test_update_course(api_client, course_factory):
    course = course_factory(_model=Course, name='Old Name')
    
    data = {'name': 'Updated Name'}
    url = f'/api/v1/courses/{course.id}/'
    response = api_client.put(url, data)
    
    assert response.status_code == 200
    course.refresh_from_db()
    assert course.name == 'Updated Name'


@pytest.mark.django_db
def test_delete_course(api_client, course_factory):
    course = course_factory(_model=Course, name='ToDelete')
    
    url = f'/api/v1/courses/{course.id}/'
    response = api_client.delete(url)
    
    assert response.status_code == 204
    assert not Course.objects.filter(id=course.id).exists()
