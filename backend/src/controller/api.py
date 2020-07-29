from flask import Blueprint, request, current_app

from models.address import AddressModel
from models.user import UserModel

api = Blueprint("api", __name__, url_prefix="/api/v1")


@api.route("/user", methods=["POST", "GET"])
def create_user():
    if request.method == "POST":
        if request.is_json:
            data = request.get_json()
            if UserModel.create_user(UserModel(name=data["name"], email=data["email"], address_id=int(data["address_id"]),
                                               hashed_password=data["password"], role=data["role"], country=data["country"])):
                return {"message": f"user {data.get('name')} has been created successfully."}, 200
            else:
                current_app.logger.error("create user fail")
                return {"message": f"user create fail."}, 400
        else:
            current_app.logger.error("request body error")
            return {"error": "The request payload is not in JSON format"}, 400

    elif request.method == "GET":
        users = UserModel.query.all()
        results = [
            {
                "name": user.name,
                "email": user.email,
                "address": user.address_id,
                "role": user.role
            } for user in users]
        return {"count": len(results), "users": results}, 200


@api.route("/address", methods=["POST", "GET"])
def create_address():
    if request.method == "POST":
        if request.is_json:
            data = request.get_json()
            if AddressModel.create_address(AddressModel(division=data["division"],
                                                        district=data["district"],
                                                        township=data["township"],
                                                        street_address=data["street_address"])):
                return {"message": f"user {data.get('street_address')} has been created successfully."}, 200
            else:
                current_app.logger.error("create address fail")
                return {"message": f"address create fail."}, 400
        else:
            current_app.logger.error("request body error")
            return {"error": "The request payload is not in JSON format"}, 400

    elif request.method == "GET":
        addresses = AddressModel.query.all()
        results = [
            {
                "division": address.division,
                "district": address.district,
                "township": address.township,
                "street_address": address.street_address
            } for address in addresses]
        return {"count": len(results), "addresses": results}, 200
