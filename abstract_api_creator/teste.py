# test.py
from gemini_factory import GeminiResponse
def test_gemini_response():
    # Instanciar a classe filha
    gemini = GeminiResponse()

    # Testar se a resposta está funcionando
    message = input("escreva")
    response = gemini.get_response(message)
    
    print(response)

# Rodar o teste
if __name__ == "__main__":
    test_gemini_response()
