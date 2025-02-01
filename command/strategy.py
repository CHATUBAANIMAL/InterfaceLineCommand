from abc import ABC, abstractmethod

class IAResponseStrategy(ABC):
    @abstractmethod
    def get_response(self, prompt: str) -> str:
        """Método para obter resposta de uma IA"""
        pass
