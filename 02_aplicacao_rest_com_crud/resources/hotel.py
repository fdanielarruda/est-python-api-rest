from flask_restful import Resource, reqparse
from models.hotel import HotelModel

hoteis = [
    {
        'id': 1,
        'nome': 'Alpha Hotel',
        'estrelas': 4.3,
        'diaria': 420.34,
        'cidade': 'Rio de Janeiro'
    },
    {
        'id': 2,
        'nome': 'Plaza Hotel',
        'estrelas': 3.9,
        'diaria': 370.99,
        'cidade': 'São Paulo'
    },
    {
        'id': 3,
        'nome': 'Iracema Beach Hotel',
        'estrelas': 4.1,
        'diaria': 400.00,
        'cidade': 'Fortaleza'
    }
]


class Hoteis(Resource):
    def get(self):
        return hoteis


class Hotel(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('nome')
    atributos.add_argument('estrelas')
    atributos.add_argument('diaria')
    atributos.add_argument('cidade')

    def find_hotel(id):
        for hotel in hoteis:
            if hotel['id'] == id:
                return hotel
        return None

    def get(self, id):
        hotel = Hotel.find_hotel(id)
        if hotel:
            return hotel
        return {'message': 'Hotel not found.'}, 404

    def post(self, id):
        dados = Hotel.atributos.parse_args()
        objeto_hotel = HotelModel(id, **dados)
        novo_hotel = objeto_hotel.json()
        hoteis.append(novo_hotel)

        return novo_hotel, 201

    def put(self, id):
        dados = Hotel.atributos.parse_args()
        objeto_hotel = HotelModel(id, **dados)
        novo_hotel = objeto_hotel.json()

        hotel = Hotel.find_hotel(id)
        if hotel:
            hotel.update(novo_hotel)
            return novo_hotel, 200

        hoteis.append(novo_hotel)
        return novo_hotel, 201

    def delete(self, id):
        global hoteis
        hoteis = [hotel for hotel in hoteis if hotel['id'] != id]
        return {'message': 'Hotel deleted'}
