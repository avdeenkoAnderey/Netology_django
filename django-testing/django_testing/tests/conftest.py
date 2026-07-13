import pytest
from rest_framework.test import APIClient

from students.models import Course, Student


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def course_factory():
    from model_bakery import baker
    return baker.make


@pytest.fixture
def student_factory():
    from model_bakery import baker
    return baker.make
