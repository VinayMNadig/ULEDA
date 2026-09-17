import { useState, useEffect, useRef } from "react";
import "./ChatPage.css";

function ChatPage({ messages, loading, sendMessage }) {

    const [input, setInput] = useState("");

    const chatEndRef = useRef(null);

    useEffect(() => {

        chatEndRef.current?.scrollIntoView({
            behavior: "smooth"
        });

    }, [messages]);

    const handleSend = () => {

        if (!input.trim()) return;

        sendMessage(input);

        setInput("");

    };

    return (

        <div className="chat-page">

            <div className="chat-header">

                <h2>🤖 ULEDA AI Database Assistant</h2>

                <p>
                    Ask anything about your database using natural language.
                </p>

            </div>

            <div className="chat-body">

                {

                    messages.length === 0 && (

                        <div className="welcome">

                            <h2>👋 Welcome to ULEDA</h2>

                            <p>

                                Ask anything like

                            </p>

                            <ul>

                                <li>Show all customers</li>

                                <li>List all employees</li>

                                <li>Show sales report</li>

                                <li>How many tables are there?</li>

                            </ul>

                        </div>

                    )

                }

                {

                    messages.map((msg, index) => (

                        <div

                            key={index}

                            className={`message ${msg.sender}`}

                        >

                            <div className="message-title">

                                {

                                    msg.sender === "user"

                                        ? "🧑 You"

                                        : "🤖 ULEDA"

                                }

                            </div>

                            <div className="message-text">

                                <pre>{msg.text}</pre>

                            </div>

                            {

                                msg.sql && (

                                    <details className="sql-box">

                                        <summary>View SQL</summary>

                                        <pre>{msg.sql}</pre>

                                    </details>

                                )

                            }

                            {

                                msg.data && msg.data.length > 0 && (

                                    <div className="table-container">

                                        <table className="result-table">

                                            <thead>

                                                <tr>

                                                    {

                                                        Object.keys(msg.data[0]).map((col) => (

                                                            <th key={col}>{col}</th>

                                                        ))

                                                    }

                                                </tr>

                                            </thead>

                                            <tbody>

                                                {

                                                    msg.data.map((row, i) => (

                                                        <tr key={i}>

                                                            {

                                                                Object.keys(msg.data[0]).map((col) => (

                                                                    <td key={col}>{String(row[col])}</td>

                                                                ))

                                                            }

                                                        </tr>

                                                    ))

                                                }

                                            </tbody>

                                        </table>

                                    </div>

                                )

                            }

                        </div>

                    ))

                }

                {

                    loading && (

                        <div className="message assistant">

                            <div className="message-title">

                                🤖 ULEDA

                            </div>

                            <div className="message-text">

                                Thinking...

                            </div>

                        </div>

                    )

                }

                <div ref={chatEndRef}></div>

            </div>

            <div className="chat-input">

                <input

                    type="text"

                    value={input}

                    placeholder="Ask anything..."

                    onChange={(e) =>
                        setInput(e.target.value)
                    }

                    onKeyDown={(e) => {

                        if (e.key === "Enter") {

                            handleSend();

                        }

                    }}

                />

                <button onClick={handleSend}>

                    Send

                </button>

            </div>

        </div>

    );

}

export default ChatPage;