import "./DashboardCards.css";

import {
    FaDatabase,
    FaTable,
    FaUsers,
    FaChartLine,
    FaServer,
    FaClock
} from "react-icons/fa";

function DashboardCards({

    databaseName = "Chinook.db",

    tables = 13,

    rows = 412,

    queries = 128,

    lastQuery = "2 sec ago",

    status = "Connected"

}) {

    return (

        <div className="dashboard-cards">

            <div className="card">

                <FaDatabase className="card-icon blue"/>

                <h4>Database</h4>

                <h2>{databaseName}</h2>

            </div>

            <div className="card">

                <FaTable className="card-icon green"/>

                <h4>Tables</h4>

                <h2>{tables}</h2>

            </div>

            <div className="card">

                <FaUsers className="card-icon orange"/>

                <h4>Total Rows</h4>

                <h2>{rows}</h2>

            </div>

            <div className="card">

                <FaChartLine className="card-icon purple"/>

                <h4>Queries</h4>

                <h2>{queries}</h2>

            </div>

            <div className="card">

                <FaServer className="card-icon teal"/>

                <h4>Status</h4>

                <h2>{status}</h2>

            </div>

            <div className="card">

                <FaClock className="card-icon red"/>

                <h4>Last Query</h4>

                <h2>{lastQuery}</h2>

            </div>

        </div>

    );

}

export default DashboardCards;