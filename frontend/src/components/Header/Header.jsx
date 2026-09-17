import "./Header.css";
import {
    FaBell,
    FaSearch,
    FaDatabase,
    FaCircle,
    FaUserCircle
} from "react-icons/fa";

function Header() {

    return (

        <div className="header">

            <div className="header-left">

                <h1>AI Database Assistant</h1>

                <p>
                    Ask anything about your database using natural language.
                </p>

            </div>

            <div className="header-right">

                <div className="search-box">

                    <FaSearch />

                    <input
                        type="text"
                        placeholder="Search chats..."
                    />

                </div>

                <div className="db-status">

                    <FaDatabase />

                    <span>Chinook.db</span>

                    <FaCircle className="online"/>

                </div>

                <button className="notify-btn">

                    <FaBell/>

                </button>

                <div className="profile-box">

                    <FaUserCircle size={34}/>

                    <div>

                        <strong>Vinay</strong>

                        <p>Administrator</p>

                    </div>

                </div>

            </div>

        </div>

    );

}

export default Header;