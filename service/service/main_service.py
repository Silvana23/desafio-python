import time
import json
from loguru import logger
from service.constants import mensagens
import pandas as pd
import numpy as np   
import math


class FuncService():

    def __init__(self):
        logger.debug(mensagens.INICIO_LOAD_SERVICO)
        self.load_servico()

    def load_servico(self):
        """"
        Carrega o servico
        """

        logger.debug(mensagens.FIM_LOAD_SERVICO)

    def executar_soma(self, cal):
        response = {}

        logger.debug(mensagens.INICIO_SERVICO)
        start_time = time.time()

        response_predicts = self.mostrar_raiz(cal['x'], cal['y'], cal['z'])
       
        logger.debug(mensagens.FIM_SERVICO)
        logger.debug(f"Fim de todas as somas em {time.time()-start_time}")
        response = {
                    "Resultado": response_predicts}

        return response

    def localizar_raiz(self, x, y, z):

        logger.debug("calculo sendo iniciado....")

        delta = ((math.pow(2, y)) - 4 * x * z)

        if delta < 0:sqrt = 0
        else:sqrt = ((math.sqrt(delta)))

        n1 = (-y + sqrt)/(2 * x)
        n2 = (-y - sqrt)/(2 * x)

        response = "n1 = " + str(str(n1) + " , " + "n2 = " + str(n2))

        return response
