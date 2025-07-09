import openai
from app.config import Config

openai.api_key = Config.OPENAI_API_KEY

def generate_summary(text):
    # Заглушка для вызова OpenAI API
    return {
        'main_idea': '...',
        'keywords': '...',
        'tone': '...',
        'content_type': '...'
    }

def generate_comment(summary, persona):
    # Заглушка для генерации комментария
    return 'Комментарий...' 