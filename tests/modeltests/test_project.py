import pytest

from model_mommy import mommy

from nalch_application.models import Project


@pytest.mark.django_db
def test_save():
    project = mommy.make(Project)
    assert project.public_name == project.short_name_en
