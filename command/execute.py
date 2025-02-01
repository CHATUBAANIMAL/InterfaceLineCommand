from abstract_api_creator import gemini_factory
from strategy import IAResponseStrategy

class GeminiStrategy(IAResponseStrategy):
    def __init__(self):
        self.api = gemini_factory.GeminiResponse.get_response()  # Instância da Gemini API

    def get_response(self, prompt: str) -> str:
        return self.api.get_response(prompt)
