import { useEffect, useRef, useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

import Sidebar from "../components/Sidebar";
import ChatBox from "../components/ChatBox";
import Message from "../components/Message";

import { logoutUser } from "../services/authService";
import {
  createChat,
  getChats,
  updateChat,
  deleteChatAPI,
} from "../services/chatService";

const API = "http://127.0.0.1:8000";

export default function Dashboard() {
  const navigate = useNavigate();

  const user = JSON.parse(localStorage.getItem("user"));

  const [chats, setChats] = useState([]);
  const [currentChat, setCurrentChat] = useState(0);
  const [loading, setLoading] = useState(false);

  const messagesEndRef = useRef(null);

  useEffect(() => {
    if (!user) {
      navigate("/login");
      return;
    }

    loadChats();
  }, []);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({
      behavior: "smooth",
    });
  }, [chats, loading]);

  const loadChats = async () => {
    try {
      const data = await getChats(user.id);

      if (!data || data.length === 0) {
        setChats([
          {
            title: "New Chat",
            messages: [],
          },
        ]);
        return;
      }

      setChats(data);
      setCurrentChat(0);
    } catch (err) {
      console.log(err);

      setChats([
        {
          title: "New Chat",
          messages: [],
        },
      ]);
    }
  };

  const createNewChat = () => {
    setChats((prev) => [
      ...prev,
      {
        title: "New Chat",
        messages: [],
      },
    ]);

    setCurrentChat(chats.length);
  };

  const selectChat = (index) => {
    setCurrentChat(index);
  };

  const deleteChat = async (index) => {
    const chat = chats[index];

    if (chat.id) {
      try {
        await deleteChatAPI(chat.id);
      } catch (err) {
        console.log(err);
      }
    }

    const updated = chats.filter((_, i) => i !== index);

    if (updated.length === 0) {
      updated.push({
        title: "New Chat",
        messages: [],
      });
    }

    setChats(updated);
    setCurrentChat(0);
  };

  const logout = () => {
    logoutUser();
    navigate("/login");
  };

  const sendMessage = async (question) => {
    if (!question.trim()) return;

    const updatedChats = [...chats];
    const chat = updatedChats[currentChat];

    chat.messages.push({
      sender: "user",
      text: question,
    });

    if (chat.title === "New Chat") {
      chat.title =
        question.length > 35
          ? question.substring(0, 35) + "..."
          : question;
    }

    setChats([...updatedChats]);
    setLoading(true);

    try {
      const res = await axios.post(`${API}/chat`, {
        question,
      });

      chat.messages.push({
        sender: "bot",
        text: res.data.answer,
        sql: res.data.sql,
        data: res.data.data,
      });

      if (chat.id) {
        await updateChat(chat.id, {
          title: chat.title,
          messages: chat.messages,
        });
      } else {
        console.log("USER =", user);

        console.log({
          user_id: user?.id,
          title: chat.title,
          messages: chat.messages,
        });

        const saved = await createChat({
          user_id: user?.id,
          title: chat.title,
          messages: chat.messages,
        });

        chat.id = saved.id;
      }

      setChats([...updatedChats]);
    } catch (error) {
      console.log("STATUS:", error.response?.status);
      console.log("ERROR:", error.response?.data);

      chat.messages.push({
        sender: "bot",
        text: "Server Error",
      });

      setChats([...updatedChats]);
    }

    setLoading(false);
  };

  return (
    <div className="layout">
      <Sidebar
        chats={chats}
        currentChat={currentChat}
        createNewChat={createNewChat}
        selectChat={selectChat}
        deleteChat={deleteChat}
      />

      <div className="app">
        <div
          style={{
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
            marginBottom: "20px",
          }}
        >
          <h1>ULEDA AI Database Assistant</h1>

          <button
            onClick={logout}
            style={{
              padding: "10px 20px",
              border: "none",
              borderRadius: "8px",
              cursor: "pointer",
              background: "#ef4444",
              color: "#fff",
            }}
          >
            Logout
          </button>
        </div>

        <div className="chat-window">
          {chats[currentChat]?.messages?.map((message, index) => (
            <Message key={index} message={message} />
          ))}

          {loading && (
            <div className="message-row bot-row">
              <div className="avatar">🤖</div>

              <div className="message bot-message">
                <div className="typing">Thinking...</div>
              </div>
            </div>
          )}

          <div ref={messagesEndRef}></div>
        </div>

        <ChatBox sendMessage={sendMessage} />
      </div>
    </div>
  );
}