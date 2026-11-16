
from backend.nlp_engine import engine


def generate_reply(message, previous_user_message=None):
    """Generate a response using the project's NLP matching engine."""
    return engine.get_response(message, previous_user_message)
