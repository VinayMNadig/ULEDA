import "./Settings.css";

import {
    FaUser,
    FaMoon,
    FaRobot,
    FaDownload,
    FaKey,
    FaSignOutAlt,
} from "react-icons/fa";

function Settings({ logout }) {

    return (

        <div className="settings-page">

            <div className="settings-header">

                <h2>⚙ Settings</h2>

                <p>
                    Manage your ULEDA preferences.
                </p>

            </div>

            <div className="settings-grid">

                {/* Profile */}

                <div className="setting-card">

                    <FaUser className="setting-icon" />

                    <h3>Profile</h3>

                    <p>Vinay M</p>

                </div>

                {/* Theme */}

                <div className="setting-card">

                    <FaMoon className="setting-icon" />

                    <h3>Theme</h3>

                    <button>

                        Dark Mode

                    </button>

                </div>

                {/* AI Model */}

                <div className="setting-card">

                    <FaRobot className="setting-icon" />

                    <h3>AI Model</h3>

                    <select>

                        <option>

                            Llama 3.3 70B

                        </option>

                        <option>

                            GPT-4

                        </option>

                        <option>

                            Gemini

                        </option>

                    </select>

                </div>

                {/* Export */}

                <div className="setting-card">

                    <FaDownload className="setting-icon" />

                    <h3>Export Chats</h3>

                    <button>

                        Download

                    </button>

                </div>

                {/* API */}

                <div className="setting-card">

                    <FaKey className="setting-icon" />

                    <h3>API Key</h3>

                    <button>

                        Manage

                    </button>

                </div>

                {/* Logout */}

                <div className="setting-card logout-card">

                    <FaSignOutAlt className="setting-icon" />

                    <h3>Logout</h3>

                    <button onClick={logout}>

                        Logout

                    </button>

                </div>

            </div>

        </div>

    );

}

export default Settings;