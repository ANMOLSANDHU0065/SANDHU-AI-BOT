from backend.chatbot import generate_reply

def test_known_question_returns_relevant_answer():
    answer = generate_reply("What is Python?")
    assert "programming language" in answer

def test_empty_message_returns_prompt():
    answer = generate_reply("   ")
    assert "type a message" in answer.lower()
