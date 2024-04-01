from flask import Blueprint
from flask_restful import Api
from .routes import initialize_routes

rcsApp = Blueprint("rcs", __name__, template_folder="templates", url_prefix="/rcs")
rcs_app = Api(rcsApp)
initialize_routes(rcs_app)