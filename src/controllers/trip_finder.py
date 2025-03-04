from typing import Dict


class TripFinder:

    def __init__(self, trips_repository: object) -> None:
        self.__trips_repository = trips_repository

    def find_trip_details(self, trip_id: str) -> Dict:
        try:
            trip = self.__trips_repository.find_trip_by_id(trip_id)  # Assuming correct method name

            if not trip:
                raise Exception("No Trip Found")

            return {
                "body": {
                    "trip": {
                        "id": trip[0],
                        "destination": trip[1],
                        "starts_at": trip[2],
                        "ends_at": trip[3],
                        "status": trip[6],  
                    }
                },
                "status_code": 200,
            }

        except Exception as exception:
            return {
                "body": {"error": str(exception)},
                "status_code": 400,
            }
