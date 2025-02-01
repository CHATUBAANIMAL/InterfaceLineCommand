from abc import ABC, abstractmethod

class AICommandBase(ABC):
    
    @abstractmethod
    def (self, prompt: str) -> str:
        """Método que deve ser implementado pelas classes filhas para retornar a resposta da IA."""
        pass
