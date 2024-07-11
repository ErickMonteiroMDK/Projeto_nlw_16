from typing import Dict, Tuple, List
from sqlite3 import Connection


class LinksRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def registry_links(self, link_infos: Dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            """
            INSERT INTO links (id, trips_id, link, title)
            VALUES (?, ?, ?, ?)
            """,
            (
                link_infos["id"],
                link_infos["trips_id"],
                link_infos["link"],
                link_infos["title"],  
            ),
        )
        self.__conn.commit()

    def find_links_from_trip(self, trip_id: str) -> List[Tuple]:
        cursor = self.__conn.cursor()
        cursor.execute("SELECT * FROM links WHERE trips_id = ?", (trip_id,))
        links = cursor.fetchall()
        return links
