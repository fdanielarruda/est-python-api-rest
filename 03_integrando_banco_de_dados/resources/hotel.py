from flask_restful import Resource, reqparse
from sqlalchemy.sql.coercions import expect

from models.hotel import HotelModel


class Hoteis(Resource):
    def get(self):
        return {'hotels': [hotel.json() for hotel in HotelModel.get_all()]}


class Hotel(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('nome', type=str, required=True, help="The field 'nome' cannot be left blank.")
    atributos.add_argument('estrelas', type=float, required=True, help="The field 'estrelas' cannot be left blank.")
    atributos.add_argument('diaria')
    atributos.add_argument('cidade')

    def get(self, id):
        hotel = HotelModel.find_hotel(id)
        if hotel:
            return hotel.json()
        return {'message': 'Hotel not found.'}, 404

    def post(self, id):
        if HotelModel.find_hotel(id):
            return {"message": "Hotel id '{}' already exists.".format(id)}, 400

        dados = Hotel.atributos.parse_args()
        hotel = HotelModel(id, **dados)

        try:
            hotel.save_hotel()
        except Exception as e:
            return {
                'message': 'An internal error ocurred trying to save hotel.',
                'error': str(e)
            }, 500

        return hotel.json(), 201

    def put(self, id):
        dados = Hotel.atributos.parse_args()

        hotel_encontrado = HotelModel.find_hotel(id)
        if hotel_encontrado:
            hotel_encontrado.update_hotel(**dados)
            hotel_encontrado.save_hotel()
            return hotel_encontrado.json(), 200

        hotel = HotelModel(id, **dados)

        try:
            hotel.save_hotel()
        except Exception as e:
            return {
                'message': 'An internal error ocurred trying to save hotel.',
                'error': str(e)
            }, 500

        return hotel.json(), 201

    def delete(self, id):
        hotel = HotelModel.find_hotel(id)
        if hotel:
            try:
                hotel.delete_hotel()
            except Exception as e:
                return {
                    'message': 'An internal error ocurred trying to delete hotel.',
                    'error': str(e)
                }, 500

            return {'message': 'Hotel deleted'}

        return {'message': 'Hotel not found.'}, 404
