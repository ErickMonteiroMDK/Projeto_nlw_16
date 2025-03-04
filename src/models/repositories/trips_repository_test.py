import pytest  # type: ignore
import uuid
from datetime import datetime, timedelta
from .trips_repository import TripsRepository
from src.models.settings.db_connection_handler import db_connection_handler


db_connection_handler.connect()

trip_id = str(uuid.uuid4())


@pytest.mark.skip(reason="interação com o banco")  
def test_create_trip():
    """Tests creating a trip in the repository."""

    conn = db_connection_handler.get_connection()

    trips_repository = TripsRepository(conn)

    trip_infos = {
        "id": trip_id,
        "destination": "Osasco",
        "start_date": datetime.strptime("02-01-2024", "%d-%m-%y"),
        "end_date": datetime.strptime("02-01-2024", "%d-%m-%y") + timedelta(days=5),
        "owner_name": "Osvaldo",
        "owner_email": "osvaldo@email.com",
    }

    trips_repository.create_trip(trip_infos)


@pytest.mark.skip(reason="interação com o banco")  
def test_find_trip_by_id():
    """Tests finding a trip by ID in the repository."""

    conn = db_connection_handler.get_connection()

    trips_repository = TripsRepository(conn)

    trip = trips_repository.find_trip_by_id(trip_id)

    print(trip)


@pytest.mark.skip(reason="interação com o banco") 
def test_update_trip_status():
    """Tests updating a trip's status in the repository."""

    conn = db_connection_handler.get_connection()

    trips_repository = TripsRepository(conn)

    trips_repository.update_trip_status(trip_id)
