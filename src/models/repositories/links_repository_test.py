import pytest # type: ignore
import uuid
from src.models.repositories.links_repository import LinksRepository
from src.models.settings.db_connection_handler import db_connection_handler
from.emails_to_invite_repository import EmailsToInviteRepository

db_connection_handler.connect()
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason="interacao com o banco")
def test_registry_links():
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)
    
    links_trips_info = {
        "id": str(uuid.uuid4()),
        "trip_id": trip_id,
        "email": "olaMundo@email.com"
    }
    
    links_repository.registry_links(links_trips_info)
    
@pytest.mark.skip(reaso="interacao com o banco")
def test_find_links_form_trip():
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)
    
    links = links_repository.find_links_from_trips(trip_id)
    print()
    print(links)