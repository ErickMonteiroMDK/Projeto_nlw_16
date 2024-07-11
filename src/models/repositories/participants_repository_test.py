import pytest  # type: ignore
import uuid
from .participants_repository import ParticipantsRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
trip_id = str(uuid.uuid4())
participant_id = str(uuid.uuid4())
emails_to_invite_id = str(uuid.uuid4())


@pytest.mark.skip(reason="interação com banco")
def test_registry_participants():
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)

    participant_info = {
        "id": participant_id,
        "trip_id": trip_id,
        "emails_to_invite_id": emails_to_invite_id,
        "name": "John Doe",
    }

    participants_repository.registry_participants(participant_info)


@pytest.mark.skip(reason="interação com banco")
def test_find_participants_from_trip():
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)

    response = participants_repository.find_participants_from_trip(trip_id)

    assert isinstance(response, list)
    assert isinstance(response[0], tuple)

    print()
    print(response)


@pytest.mark.skip(reason="interação com banco")
def test_update_participant_status():
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)

    participant_info = {
        "id": participant_id,
        "trip_id": trip_id,
        "emails_to_invite_id": emails_to_invite_id,
        "name": "John Doe",
    }

    participants_repository.registry_participants(participant_info)
    participants_repository.update_participant_status(participant_id)

    cursor = conn.cursor()
    cursor.execute("SELECT is_confirmed FROM participants WHERE id = ?", (participant_id,))
    status = cursor.fetchone()

    assert status[0] == 1
