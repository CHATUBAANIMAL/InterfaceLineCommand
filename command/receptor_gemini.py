from typing import Protocol

from abstract_api_creator.gemini_factory import GeminiResponse


class Command(Protocol):
    def execute(self) -> str:
        pass

class GeminiCommand(Command):
    def __init__(self, gemini: GeminiResponse, message: str):
        self.gemini = gemini
        self.message = message
        

    def execute(self) -> str:
        return self.gemini.get_response(self.message)


