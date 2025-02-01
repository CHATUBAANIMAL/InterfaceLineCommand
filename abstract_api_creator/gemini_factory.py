#gemini_factory
from abc import ABC

import google.generativeai as genai
from abstract_api_creator.api_factory import APIFactory



class GeminiResponse(APIFactory, ABC):
    
    def __init__(self):
       
       #configurando o gemini
        self.message = None
        self._api_key = self.configure("gemini_key")
        genai.configure(api_key=self._api_key)
        self.model = genai.GenerativeModel("gemini-1.5-flash")


    

    def get_response(self, message: str) -> str:
        try:
            #tentando estabelecer conexão
            self.message = message
            response = self.model.generate_content(message)
            return response.text
        except Exception as e:
            return f"Erro ao gerar resposta: {e}"
        


    