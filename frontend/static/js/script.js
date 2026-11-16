const form = document.getElementById("chat-form");
const input = document.getElementById("message-input");
const messages = document.getElementById("messages");
const sendButton = document.getElementById("send-btn");
const clearButton = document.getElementById("clear-btn");

function addMessage(role, text) {
  const row = document.createElement("div");
  row.className = `message-row ${role === "user" ? "user-row" : "bot-row"}`;

  const avatar = document.createElement("div");
  avatar.className = "message-avatar";
  avatar.textContent = role === "user" ? "You" : "S";

  const bubble = document.createElement("div");
  bubble.className = "bubble";
  const paragraph = document.createElement("p");
  paragraph.textContent = text; // textContent prevents user text being treated as HTML.
  bubble.appendChild(paragraph);

  row.append(avatar, bubble);
  messages.appendChild(row);
  messages.scrollTop = messages.scrollHeight;
}

async function sendMessage(message) {
  addMessage("user", message);
  input.value = "";
  sendButton.disabled = true;
  sendButton.textContent = "Thinking...";

  try {
    const response = await fetch("/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message })
    });
    const data = await response.json();
    if (!response.ok) throw new Error(data.error || "Something went wrong.");
    addMessage("assistant", data.reply);
  } catch (error) {
    addMessage("assistant", `Sorry, ${error.message}`);
  } finally {
    sendButton.disabled = false;
    sendButton.innerHTML = 'Send <span>➤</span>';
    input.focus();
  }
}

form.addEventListener("submit", (event) => {
  event.preventDefault();
  const message = input.value.trim();
  if (message) sendMessage(message);
});

document.querySelectorAll(".suggestion").forEach((button) => {
  button.addEventListener("click", () => sendMessage(button.dataset.prompt));
});

clearButton.addEventListener("click", async () => {
  try {
    const response = await fetch("/api/clear", { method: "POST" });
    if (!response.ok) throw new Error("Could not clear chat.");
    messages.innerHTML = "";
    addMessage("assistant", "Chat cleared! What would you like to talk about?");
  } catch (error) {
    addMessage("assistant", error.message);
  }
});

async function loadHistory() {
  try {
    const response = await fetch("/api/history");
    const data = await response.json();
    if (data.messages && data.messages.length) {
      messages.innerHTML = "";
      data.messages.forEach((item) => addMessage(item.role, item.message));
    }
  } catch (error) {
    console.error("Could not load chat history:", error);
  }
}

loadHistory();
