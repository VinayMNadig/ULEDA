import "./Sidebar.css";
import {
    FaComments,
    FaDatabase,
    FaUpload,
    FaSignOutAlt
} from "react-icons/fa";

function Sidebar({ logout }) {

    const handleUpload = async (e) => {

        const file = e.target.files[0];

        if (!file) return;

        const formData = new FormData();

        formData.append("file", file);

        try {

            const response = await fetch(
                "http://127.0.0.1:8000/database/upload",
                {
                    method: "POST",
                    body: formData,
                }
            );

            if (!response.ok) {
                throw new Error("Upload failed");
            }

            const data = await response.json();

            alert("✅ Database Uploaded Successfully!");

            console.log(data);

        }
        catch (err) {

            console.error(err);

            alert("❌ Upload Failed");

        }

    };

    return (

        <div className="sidebar">

            {/* Logo */}

            <div className="logo-section">

                <div className="logo">

                    🤖

                </div>

                <div>

                    <h2>ULEDA</h2>

                    <p>AI Database Assistant</p>

                </div>

            </div>

            {/* Menu */}

            <div className="menu">

                <div className="menu-item active">

                    <FaComments />

                    <span>AI Chat</span>

                </div>

                <label className="menu-item">

                    <FaUpload />

                    <span>Upload Database</span>

                    <input
                        type="file"
                        accept=".db,.sqlite,.sqlite3"
                        hidden
                        onChange={handleUpload}
                    />

                </label>

                <div className="menu-item">

                    <FaDatabase />

                    <span>Database</span>

                </div>

            </div>

            {/* Bottom */}

            <div className="sidebar-bottom">

                <button
                    className="logout-btn"
                    onClick={logout}
                >

                    <FaSignOutAlt />

                    Logout

                </button>

                <div className="version">

                    ULEDA AI v1.0

                </div>

            </div>

        </div>

    );

}

export default Sidebar;