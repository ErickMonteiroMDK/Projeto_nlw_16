from typing import Dict

class ParticipantConfirmer:
    def __init__(self, participant_repository) -> None:
        self.__participant_repository = participant_repository
        
    def confirm(self, trip_id) -> Dict:
        try
            self.__participant_repository.update_participant_status(trip_id) # type: ignore
            return {"body": None, "status_code": 204}
        
        except Exception as exception:
            return {
                "body": {"error": str(exception)},
                "status_code": 400
            }
