import { useState } from "react";

function ChatBox({ sendMessage }) {
  const [question, setQuestion] = useState("");

  const handleSend = () => {
    if (!question.trim()) return;

    sendMessage(question);
    setQuestion("");
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter") {
      handleSend();
    }
  };

  return (
    <div className="chat-box">
      <input
        type="text"
        placeholder="Ask something about your database..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        onKeyDown={handleKeyDown}
      />

      <button onClick={handleSend}>
        Send
      </button>
    </div>
  );
}

export default ChatBox;