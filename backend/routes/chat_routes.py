import uuid
from flask import Blueprint, jsonify, request, session

from backend.chatbot import generate_reply
from backend.database import save_message, get_messages, clear_messages

chat_bp = Blueprint("chat", __name__)

def get_session_id():
    if "chat_session_id" not in session:
        session["chat_session_id"] = str(uuid.uuid4())
    return session["chat_session_id"]

@chat_bp.post("/chat")
def chat():
    data = request.get_json(silent=True) or {}
    message = str(data.get("message", "")).strip()
    if not message:
        return jsonify({"error": "Please enter a message."}), 400
    if len(message) > 1000:
        return jsonify({"error": "Message is too long. Maximum 1000 characters."}), 400

    session_id = get_session_id()
    history = get_messages(session_id, limit=20)
    previous_user = next(
        (item["message"] for item in reversed(history) if item["role"] == "user"),
        None,
    )

    save_message(session_id, "user", message)
    reply = generate_reply(message, previous_user)
    save_message(session_id, "assistant", reply)
    return jsonify({"reply": reply})

@chat_bp.get("/history")
def history():
    return jsonify({"messages": get_messages(get_session_id())})

@chat_bp.post("/clear")
def clear():
    clear_messages(get_session_id())
    return jsonify({"message": "Chat history cleared."})
