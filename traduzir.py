from google.cloud import translate
import os 

def translate_text(text: str, target_language_code: str) -> translate.Translation:
    client = translate.TranslationServiceClient()

    response = client.translate_text(
        parent='projects/' + os.environ['PROJECT_ID'],
        contents=[text],
        target_language_code=target_language_code,
    )

    return response.translations[0].translated_text


if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    print(translate_text('Isso é um teste', 'en'))