from flask import jsonify, Blueprint, request

from src.models.repositories import trips_repository

trips_routes_bp = Blueprint("trip_routes", __name__)

# Importation of Controllers
from scr.controllers.trip_creator import TripCreator  # type: ignore
from src.controllers.trip_finder import TripFinder
from src.controllers.trip_confirmer import TripConfirmer

from src.controllers.link_creator import LinkCreator
from src.controllers.link_finder import LinkFinder

from src.controllers.participant_creator import ParticipantCreator
from src.controllers.participant_finder import ParticipantFinder
from src.controllers.participant_confirmer import ParticipantConfirmer

from src.controllers.activity_creator import ActivityCreator
from src.controllers.activity_finder import ActivityFinder

# Importation of Repositories
from src.models.repositories.trips_repository import TripsRepository
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository  # type: ignore
from src.models.repositories.links_repository import LinksRepository
from src.models.repositories.participants_repository import PartcipantsRepository
from src.models.repositories.activities_repository import ActivitesRepository

# Importation of Connection Manager
from src.models.settings.db_connection_handler import db_connection_handler


@trips_routes_bp.route("/trips", methods=["POST"])
def create_trip():
    conn = db_connection_handler.get_connection()
    trip_repository = TripsRepository(conn)
    email_repository = EmailsToInviteRepository(conn)
    controller = TripCreator(trip_repository, email_repository)

    response = controller.create(request.json)

    return jsonify({"body": response["body"], "status_code": response["status_code"]})

@trips_routes_bp.route("/trips/<tripId>", methods=["GET"])
def find_trip(tripId):
    conn = db_connection_handler.get_connection()
    trip_repository = TripsRepository(conn)
    controller = TripFinder(trips_repository)
    
    response = controller.find_trip_details(tripId)
    
    return jsonify({"body": response["body"], "status_code": response["status_code"]})

@trips_routes_bp.route("/trips/<tripId>/confirm", methods=["GET"])
def confirm_trip():
    conn = db_connection_handler.get_connection()
    trip_repository = TripsRepository(conn)
    controller = TripConfirmer(trips_repository)
    
    response = controller.confirm(tripId) # type: ignore
    
    return jsonify({"body": response["body"], "status_code": response["status_code"]})

@trips_routes_bp.route("/trips/<tripId>/links", methods=["POST"])
def create_trip_link():
   conn = db_connection_handler.get_connection() 
   links_repository = LinksRepository(conn)
   controller = LinkCreator(links_repository)
   
   response = controller.create(request.json, tripId) # type: ignore
   
   return jsonify({"body": response["body"], "status_code": response["status_code"]})

@trips_routes_bp.route("/trips/<tripId>/links", methods=["GET"])
def find_trip_link():
   conn = db_connection_handler.get_connection() 
   links_repository = LinksRepository(conn)
   controller = LinkFinder(links_repository)
   
   response = controller.find(tripId) # type: ignore
   
   
   return jsonify({"body": response["body"], "status_code": response["status_code"]})

@trips_routes_bp.route("/trips/<tripId>/invites", methods=["POST"])
def invite_to_trip(tripId):
    conn = db_connection_handler.get_connection() 
    participants_repository = PartcipantsRepository(conn)
    emails_repository = EmailsToInviteRepository(conn)
    controller = ParticipantCreator(participants_repository, emails_repository)
    
    response = controller.create(request.json, tripId)
    
    return jsonify({"body": response["body"], "status_code": response["status_code"]})


@trips_routes_bp.route("/trips/<tripId>/activities", methods=["POST"])
def create_activity(tripId):
    conn = db_connection_handler.get_connection()
    activities_repository = ActivitesRepository(conn)
    controller = ActivityCreator(activities_repository) 
    
    response = controller.create(request.json, tripId)
    
    return jsonify({"body": response["body"], "status_code": response["status_code"]})


@trips_routes_bp.route("/trips/<tripId>/participants", methods=["GET"])
def get_trip_participants(tripId):
    conn = db_connection_handler.get_connection()
    participants_repository = PartcipantsRepository(conn)
    controller = ParticipantFinder(participants_repository)
    
    response = controller.find_participants_from_trip(tripId)
    
    return jsonify({"body": response["body"], "status_code": response["status_code"]})


@trips_routes_bp.route("/trips/<tripId>/activities", methods=["GET"])
def get_trip_activities(tripId):
    conn = db_connection_handler.get_connection()
    activities_repository = ActivitesRepository(conn)
    controller = ActivityFinder(activities_repository)
    
    response = controller.find_from_trip(tripId)
    
    return jsonify({"body": response["body"], "status_code": response["status_code"]})

@trips_routes_bp.route("/participants/<participantId>/confirm", methods=["PATCH"])
def confirm_participant(participantId):
    conn = db_connection_handler.get_connection()
    participant_repository = PartcipantsRepository(conn)
    controller = ParticipantConfirmer(participant_repository)
    
    response = controller.confirm(participantId) # type: ignore
    
    return jsonify({"body": response["body"], "status_code": response["status_code"]})