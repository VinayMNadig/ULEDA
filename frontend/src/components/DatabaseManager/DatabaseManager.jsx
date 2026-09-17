import "./DatabaseManager.css";

import {

    FaDatabase,

    FaCloudUploadAlt,

    FaCheckCircle,

    FaTrash,

    FaExchangeAlt,

} from "react-icons/fa";

function DatabaseManager() {

    const databases = [

        {
            name: "Chinook.db",
            type: "SQLite",
            status: "Connected",
            active: true,
        },

        {
            name: "Sales.db",
            type: "SQLite",
            status: "Disconnected",
            active: false,
        },

        {
            name: "HR.db",
            type: "SQLite",
            status: "Disconnected",
            active: false,
        },

    ];

    return (

        <div className="database-manager">

            <div className="db-header">

                <h2>

                    🗄 Database Manager

                </h2>

                <p>

                    Manage multiple databases connected to ULEDA.

                </p>

            </div>

            {/* Upload Card */}

            <div className="upload-card">

                <FaCloudUploadAlt className="upload-icon"/>

                <h3>

                    Upload New Database

                </h3>

                <p>

                    Supported Formats

                </p>

                <div className="supported">

                    <span>SQLite</span>

                    <span>MySQL</span>

                    <span>PostgreSQL</span>

                    <span>SQL Server</span>

                </div>

                <button>

                    Upload Database

                </button>

            </div>

            {/* Connected Databases */}

            <div className="database-list">

                {

                    databases.map((db,index)=>(

                        <div

                            key={index}

                            className="database-card"

                        >

                            <div>

                                <FaDatabase className="db-icon"/>

                            </div>

                            <div className="db-info">

                                <h3>

                                    {db.name}

                                </h3>

                                <p>

                                    {db.type}

                                </p>

                            </div>

                            <div className="db-status">

                                {

                                    db.active ?

                                    <span className="active">

                                        <FaCheckCircle />

                                        Active

                                    </span>

                                    :

                                    <button>

                                        <FaExchangeAlt />

                                        Switch

                                    </button>

                                }

                            </div>

                            <button

                                className="delete-db"

                            >

                                <FaTrash/>

                            </button>

                        </div>

                    ))

                }

            </div>

        </div>

    );

}

export default DatabaseManager;