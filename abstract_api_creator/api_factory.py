#api_factory

from abc import ABC, abstractmethod
import os
from dotenv import load_dotenv

class APIFactory(ABC):
    load_dotenv()
    _api_key = None

      


    @classmethod
    def configure(cls, key_name: str) -> str:
        """ Retorna a chave API dentro da pasta .env 
        """
        api_key = os.getenv(key_name)
        cls._api_key = api_key
        return api_key

    @abstractmethod
    def get_response(self, message: str) -> str:
       """" Lógica para a criação das resposta da IA. Deve ser criado pelas classes filhas
       """

