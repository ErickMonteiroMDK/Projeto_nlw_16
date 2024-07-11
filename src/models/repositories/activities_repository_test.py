import pytest  # type: ignore
import uuid
from .activities_repository import ActivitiesRepository
from src.models.settings.db_connection_handler import db_connection_handler


db_connection_handler.connect()
trip_id = str(uuid.uuid4())
activity_id = str(uuid.uuid4())


@pytest.mark.skip(reason="interação com banco")
def test_registry_activity():
    conn = db_connection_handler.get_connection()
    activities_repository = ActivitiesRepository(conn)

    activity_info = {
        "id": activity_id,
        "trips_id": trip_id,
        "title": "Visit Museum",
        "occurs_at": "2024-07-11 10:00:00",
    }

    activities_repository.registry_activity(activity_info)


@pytest.mark.skip(reason="interação com banco")
def test_find_activities_from_trip():
    conn = db_connection_handler.get_connection()
    activities_repository = ActivitiesRepository(conn)

    activity_info = {
        "id": activity_id,
        "trips_id": trip_id,
        "title": "Visit Museum",
        "occurs_at": "2024-07-11 10:00:00",
    }

    activities_repository.registry_activity(activity_info)  # Register activity before finding

    response = activities_repository.find_activities_from_trip(trip_id)

    assert isinstance(response, list)
    assert isinstance(response[0], tuple)

    print()
    print(response)
