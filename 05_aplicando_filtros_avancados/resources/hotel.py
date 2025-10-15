from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from models.hotel import HotelModel
import sqlite3

def normalize_path_params(
        city=None,
        stars_min=0,
        stars_max=5,
        daily_min=0,
        daily_max=10000,
        limit=50,
        offset=0,
        **data
):
    if city:
        return {
            'stars_min': stars_min,
            'stars_max': stars_max,
            'daily_min': daily_min,
            'daily_max': daily_max,
            'city': city,
            'limit': limit,
            'offset': offset
        }

    return {
        'stars_min': stars_min,
        'stars_max': stars_max,
        'daily_min': daily_min,
        'daily_max': daily_max,
        'limit': limit,
        'offset': offset
    }

# Parâmetros para filtros
path_params = reqparse.RequestParser()
path_params.add_argument('city', type=str, location='args')
path_params.add_argument('stars_min', type=float, location='args')
path_params.add_argument('stars_max', type=float, location='args')
path_params.add_argument('daily_min', type=float, location='args')
path_params.add_argument('daily_max', type=float, location='args')
path_params.add_argument('limit', type=float, location='args')
path_params.add_argument('offset', type=float, location='args')


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
        connection = sqlite3.connect('instance/banco.db')
        cursor = connection.cursor()

        data = path_params.parse_args()
        valid_data = { key:data[key] for key in data if data[key] is not None }
        params = normalize_path_params(**valid_data)

        if params.get('city'):
            query = ('SELECT * FROM hotels \
                     WHERE (stars >= ? and stars <= ?) \
                     AND (daily >= ? and daily <= ?) \
                     AND (city = ?) \
                     LIMIT ? OFFSET ?')
            formatted_params = tuple([params[key] for key in params])
            result = cursor.execute(query, formatted_params)
        else:
            query = ('SELECT * FROM hotels \
                     WHERE (stars >= ? and stars <= ?) \
                     AND (daily >= ? and daily <= ?) \
                     LIMIT ? OFFSET ?')
            formatted_params = tuple([params[key] for key in params])
            result = cursor.execute(query, formatted_params)

        hotels = []
        for row in result:
            hotels.append({
                'hotel_id': row[0],
                'name': row[1],
                'stars': row[2],
                'daily': row[3],
                'city': row[4]
            })

        return {'hotels': hotels}

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
