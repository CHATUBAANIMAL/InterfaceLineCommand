#cli prompt
import click
from abstract_api_creator.gemini_factory import GeminiResponse



@click.command()
@click.option("-P", "--prompt", type=click.STRING, help="Prompt para a IA")
def prompt(prompt):
    """
    Use aspas para seus textos
    """
    gemini_response = GeminiResponse()
    response = gemini_response.get_response(prompt)
    return response
    
    

