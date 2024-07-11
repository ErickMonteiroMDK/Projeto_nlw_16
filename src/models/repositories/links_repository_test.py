import pytest  # type: ignore
import uuid
from .links_repository import LinksRepository
from src.models.settings.db_connection_handler import db_connection_handler


db_connection_handler.connect()
trip_id = str(uuid.uuid4())
link_id = str(uuid.uuid4())


@pytest.mark.skip(reason="interação com banco")
def test_registry_links():
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)

    links_info = {
        "id": link_id,
        "trip_id": trip_id,
        "link": "somelink.com",
        "title": "Hotel",
    }

    links_repository.registry_links(links_info)


@pytest.mark.skip(reason="interação com banco")
def test_find_links_from_trip():
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)

    response = links_repository.find_links_from_trips(trip_id)

    assert isinstance(response, list)
    assert isinstance(response[0], tuple)

    print()
    print(response)
