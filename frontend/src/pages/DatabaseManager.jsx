import { useEffect, useState } from "react";
import DatabaseCard from "../components/DatabaseCard";

import {

    getDatabases,

    uploadDatabase,

    connectDatabase,

    disconnectDatabase,

    deleteDatabase,

    getActiveDatabase,

} from "../services/databaseService";

import "./DatabaseManager.css";

function DatabaseManager() {

    const [databases, setDatabases] = useState([]);

    const [activeDatabase, setActiveDatabase] = useState(null);

    const [selectedFile, setSelectedFile] = useState(null);

    const [loading, setLoading] = useState(false);

    // =====================================
    // Load Data
    // =====================================

    const loadDatabases = async () => {

        try {

            const list = await getDatabases();

            setDatabases(list);

            const active = await getActiveDatabase();

            setActiveDatabase(active);

        }

        catch (err) {

            console.log(err);

        }

    };

    useEffect(() => {

        loadDatabases();

    }, []);

    // =====================================
    // Upload Database
    // =====================================

    const upload = async () => {

        if (!selectedFile) {

            alert("Please select a database.");

            return;

        }

        try {

            setLoading(true);

            const formData = new FormData();

            formData.append(

                "file",

                selectedFile

            );

            await uploadDatabase(formData);

            alert("Database uploaded successfully.");

            setSelectedFile(null);

            loadDatabases();

        }

        catch (err) {

            console.log(err);

            alert("Upload failed.");

        }

        finally {

            setLoading(false);

        }

    };

    // =====================================
    // Connect Database
    // =====================================

    const connect = async (databaseName) => {

        try {

            await connectDatabase(databaseName);

            alert("Database Connected.");

            loadDatabases();

        }

        catch (err) {

            console.log(err);

        }

    };

    // =====================================
    // Disconnect
    // =====================================

    const disconnect = async () => {

        try {

            await disconnectDatabase();

            alert("Database Disconnected.");

            loadDatabases();

        }

        catch (err) {

            console.log(err);

        }

    };

    // =====================================
    // Delete Database
    // =====================================

    const remove = async (databaseName) => {

        if (

            !window.confirm(

                `Delete ${databaseName}?`

            )

        )

            return;

        try {

            await deleteDatabase(databaseName);

            loadDatabases();

        }

        catch (err) {

            console.log(err);

        }

    };

    return (

        <div className="database-page">

            <h1>

                🗄 Database Manager

            </h1>

            <br />

            <div className="upload-box">

                <input

                    type="file"

                    accept=".db,.sqlite"

                    onChange={(e) =>

                        setSelectedFile(

                            e.target.files[0]

                        )

                    }

                />

                <button

                    onClick={upload}

                    disabled={loading}

                >

                    {

                        loading

                            ? "Uploading..."

                            : "Upload Database"

                    }

                </button>

            </div>

            <hr />

            <h3>

                Active Database

            </h3>

            <p>

                {

                    activeDatabase?.database_name ||

                    "No Database Connected"

                }

            </p>

            <hr />

            <h2>

                Uploaded Databases

            </h2>

            {

                databases.length === 0 ? (

                    <p>

                        No databases uploaded.

                    </p>

                ) : (

                    databases.map((db) => (

                        <DatabaseCard

                            key={db.name}

                            database={db}

                            active={

                                activeDatabase?.database_name === db.name

                            }

                            connect={connect}

                            disconnect={disconnect}

                            remove={remove}

                        />

                    ))

                )

            }

        </div>

    );

}

export default DatabaseManager;