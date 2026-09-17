import { useState } from "react";
import { FaPaperPlane, FaPaperclip, FaMicrophone } from "react-icons/fa";
import "./ChatBox.css";

function ChatBox({ sendMessage }) {

    const [question, setQuestion] = useState("");

    const handleSend = () => {

        if (!question.trim()) return;

        sendMessage(question);

        setQuestion("");

    };

    const handleKeyDown = (e) => {

        if (e.key === "Enter" && !e.shiftKey) {

            e.preventDefault();

            handleSend();

        }

    };

    return (

        <div className="chatbox-container">

            <div className="chatbox">

                <button className="icon-btn">

                    <FaPaperclip />

                </button>

                <textarea

                    placeholder="Ask anything about your database..."

                    value={question}

                    onChange={(e) => setQuestion(e.target.value)}

                    onKeyDown={handleKeyDown}

                    rows={1}

                />

                <button className="icon-btn">

                    <FaMicrophone />

                </button>

                <button

                    className="send-btn"

                    onClick={handleSend}

                >

                    <FaPaperPlane />

                </button>

            </div>

        </div>

    );

}

export default ChatBox;