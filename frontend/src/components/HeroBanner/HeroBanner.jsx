import "./HeroBanner.css";
import { FaDatabase, FaRobot } from "react-icons/fa";
import { useRef } from "react";
import { uploadDatabase } from "../../services/databaseService";

function HeroBanner() {

    const fileInputRef = useRef(null);

    const openFilePicker = () => {
        fileInputRef.current.click();
    };

    const handleUpload = async (event) => {

        const file = event.target.files[0];

        if (!file) return;

        try {

            const formData = new FormData();

            formData.append("file", file);

            await uploadDatabase(formData);

            alert(`${file.name} uploaded successfully ✅`);

            // Refresh page so active database updates
            window.location.reload();

        } catch (error) {

            console.error(error);

            alert("Upload Failed ❌");

        }

    };

    return (

        <div className="hero-banner">

            <div className="hero-left">

                <h1>🤖 ULEDA AI Database Assistant</h1>

                <p>
                    Ask anything about your database using Natural Language.
                    Generate SQL, visualize data, manage multiple databases,
                    and analyze information with AI.
                </p>

                <div className="hero-buttons">

                    <button
                        className="primary-btn"
                        onClick={openFilePicker}
                    >
                        <FaDatabase />
                        Upload Database
                    </button>

                    <button className="secondary-btn">
                        <FaRobot />
                        Browse Database
                    </button>

                    <input
                        type="file"
                        accept=".db,.sqlite,.sqlite3"
                        ref={fileInputRef}
                        style={{ display: "none" }}
                        onChange={handleUpload}
                    />

                </div>

            </div>

            <div className="hero-right">

                <div className="hero-chip">SQLite</div>

                <div className="hero-chip">MySQL</div>

                <div className="hero-chip">PostgreSQL</div>

                <div className="hero-chip">SQL Server</div>

                <div className="hero-chip">Oracle</div>

            </div>

        </div>

    );
}

export default HeroBanner;