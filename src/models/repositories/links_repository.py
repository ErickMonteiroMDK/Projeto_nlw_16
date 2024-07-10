from typing import Dict, Tuple, List
from sqlite3 import Connection

class LinksRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn
        
    def registry_links(self, link_infos: Dict) -> None:
       cursor = self.__conn.cursor()
       cursor.execute(
           '''
           INSER INTO links
                (id, trips_id, emails)
            VALUES
                (?,?,?)
           ''', (
               link_infos["id"],
               link_infos["trips_id"],
               link_infos["emails"]
           )
       ) 
       self.__conn.commit()
       
       def find_links_from_trips(self, trip_id: str) -> List[tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''SELECT * FROM links WHERE trips_id = ? ''', (trip_id,)
        )
        trip = cursor.fetchall()
        return trip