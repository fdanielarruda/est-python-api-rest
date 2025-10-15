from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from models.hotel import HotelModel


class Hotels(Resource):
    @staticmethod
    def get_parser():
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, help="The field 'name' cannot be left blank.")
        parser.add_argument('stars', type=float, required=True, help="The field 'stars' cannot be left blank.")
        parser.add_argument('daily')
        parser.add_argument('city')
        return parser

    def get(self):
        return {'hotels': [hotel.json() for hotel in HotelModel.get_all()]}

    @jwt_required()
    def post(self):
        data = Hotels.get_parser().parse_args()
        hotel = HotelModel(**data)

        try:
            hotel.save_hotel()
        except Exception as e:
            return {
                'message': 'An internal error occurred trying to save hotel.',
                'error': str(e)
            }, 500

        return hotel.json(), 201

class Hotel(Resource):
    def get(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            return hotel.json()
        return {'message': 'Hotel not found.'}, 404

    @jwt_required()
    def put(self, hotel_id):
        data = Hotels.get_parser().parse_args()
        hotel_found = HotelModel.find_hotel(hotel_id)

        if hotel_found:
            hotel_found.update_hotel(**data)
            hotel_found.save_hotel()
            return hotel_found.json(), 200

        hotel = HotelModel(**data)

        try:
            hotel.save_hotel()
        except Exception as e:
            return {
                'message': 'An internal error occurred trying to save hotel.',
                'error': str(e)
            }, 500

        return hotel.json(), 201

    @jwt_required()
    def delete(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            try:
                hotel.delete_hotel()
            except Exception as e:
                return {
                    'message': 'An internal error occurred trying to delete hotel.',
                    'error': str(e)
                }, 500

            return {'message': 'Hotel deleted'}

        return {'message': 'Hotel not found.'}, 404
