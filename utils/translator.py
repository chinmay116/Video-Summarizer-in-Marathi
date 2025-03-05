from deep_translator import GoogleTranslator
from .constants import LANGUAGE_CODE_MAP


def translate_text(text, target_language):
    """Translate text using deep-translator library"""
    try:
        # Convert language codes if needed
        lang_code = LANGUAGE_CODE_MAP.get(target_language, target_language)

        # Initialize translator and perform translation
        translator = GoogleTranslator(source='auto', target=lang_code)
        return translator.translate(text)

    except Exception as e:
        raise Exception(f"Translation error: {str(e)}")