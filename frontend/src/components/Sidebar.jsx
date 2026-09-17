import { useNavigate } from "react-router-dom";

import {
    FaPlus,
    FaTrash,
    FaComments,
    FaDatabase,
    FaChartBar,
    FaHistory,
    FaCog,
    FaHome,
    FaMoon,
} from "react-icons/fa";

import "./Sidebar.css";

function Sidebar({

    chats,

    currentChat,

    createNewChat,

    selectChat,

    deleteChat,

}) {

    const navigate = useNavigate();

    return (

        <div className="sidebar">

            {/* ===================== */}
            {/* Logo */}
            {/* ===================== */}

            <div className="sidebar-header">

                <div className="logo-circle">

                    🤖

                </div>

                <div>

                    <h2>ULEDA</h2>

                    <span>AI Database Assistant</span>

                </div>

            </div>

            {/* ===================== */}
            {/* Buttons */}
            {/* ===================== */}

            <button
                className="new-chat-btn"
                onClick={createNewChat}
            >

                <FaPlus />

                <span>New Chat</span>

            </button>

            <button
                className="database-btn"
                onClick={() => navigate("/database")}
            >

                <FaDatabase />

                <span>Database Manager</span>

            </button>

            {/* ===================== */}
            {/* Navigation */}
            {/* ===================== */}

            <div className="sidebar-menu">

                <div className="menu-item active">

                    <FaHome />

                    <span>Dashboard</span>

                </div>

                <div className="menu-item">

                    <FaComments />

                    <span>Chats</span>

                </div>

                <div className="menu-item">

                    <FaDatabase />

                    <span>Databases</span>

                </div>

                <div className="menu-item">

                    <FaChartBar />

                    <span>Analytics</span>

                </div>

                <div className="menu-item">

                    <FaHistory />

                    <span>History</span>

                </div>

                <div className="menu-item">

                    <FaCog />

                    <span>Settings</span>

                </div>

            </div>

            {/* ===================== */}
            {/* Recent Chats */}
            {/* ===================== */}

            <h3 className="recent-title">

                Recent Chats

            </h3>

            <div className="chat-list">

                {

                    chats.map((chat, index) => (

                        <div

                            key={index}

                            className={

                                currentChat === index

                                    ? "chat-item active"

                                    : "chat-item"

                            }

                        >

                            <div

                                className="chat-title"

                                onClick={() =>

                                    selectChat(index)

                                }

                            >

                                <FaComments />

                                <span>

                                    {chat.title}

                                </span>

                            </div>

                            <button

                                className="delete-btn"

                                onClick={() =>

                                    deleteChat(index)

                                }

                            >

                                <FaTrash />

                            </button>

                        </div>

                    ))

                }

            </div>

            {/* ===================== */}
            {/* Footer */}
            {/* ===================== */}

            <div className="sidebar-footer">

                <div className="footer-db">

                    <FaDatabase />

                    <span>Chinook.db</span>

                </div>

                <div className="footer-status">

                    🟢 Connected

                </div>

                <div className="footer-version">

                    <FaMoon />

                    <span>ULEDA AI v1.0</span>

                </div>

            </div>

        </div>

    );

}

export default Sidebar;