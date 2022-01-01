from flask_restplus import fields
from service.restplus import api

INPUT_MAIN_SERVICE = api.model(
  'input_main_service', {
     'x': fields.Integer(required=True, description= "Valor  da variavel de segundo grau"),
     'y': fields.Integer(required=True, description= "Valor da variavel de primeiro grau "),
     'z': fields.Integer(required=True, description= "Valor  sem variavel")})
