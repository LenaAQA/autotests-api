import pytest

from fixtures.users import UserFixture
from fixtures.files import FileFixture
from clients.exercises.exercises_client import ExercisesClient, get_exercises_client
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema
from pydantic import BaseModel


class ExerciseFixture(BaseModel):
    request: CreateExerciseRequestSchema
    response: CreateExerciseResponseSchema


@pytest.fixture
def exercises_client(function_user: UserFixture) -> ExercisesClient:
    return get_exercises_client(function_user.authentication_user)


@pytest.fixture
def function_exercise(
        courses_client: ExercisesClient,
        function_user: UserFixture,
        function_file: FileFixture
):
    request = CreateExerciseRequestSchema()
    response = courses_client.create_exercise(request)
    return ExerciseFixture(request=request, response=response)
