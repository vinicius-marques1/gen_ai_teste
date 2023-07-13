from vertexai.preview.language_models import TextGenerationModel
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env
from traduzir import translate_text
from flask import Flask, request

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def text_question(temperature: float = 0.2):
    """Ideation example with a Large Language Model"""

    # pergunta
    pergunta = request.get_json()['text']
    pergunta = translate_text(pergunta, 'en')

    # TODO developer - override these parameters as needed:
    parameters = {
        "temperature": temperature,  # Temperature controls the degree of randomness in token selection.
        "max_output_tokens": 256,  # Token limit determines the maximum amount of text output.
        "top_p": 0.8,  # Tokens are selected from most probable to least until the sum of their probabilities equals the top_p value.
        "top_k": 40,  # A top_k of 1 means the selected token is the most probable among all tokens.
    }

    model = TextGenerationModel.from_pretrained("text-bison@001")
    response = model.predict(
        pergunta,
        **parameters,
    )
    print(f"Response from Model: {response.text}")
    translated_answer = translate_text(response.text, 'pt')

    return {
        'fulfillmentResponse': {
            'messages': [
                {
                    'text': {
                        'text': [
                            translated_answer
                        ]
                    }
                }
            ]
        }
    }


if __name__ == "__main__":
    app.run()