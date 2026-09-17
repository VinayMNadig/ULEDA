import "./AnalyticsDashboard.css";

import {
    FaDatabase,
    FaRobot,
    FaBolt,
    FaCheckCircle,
} from "react-icons/fa";

function AnalyticsDashboard({

    queries = 128,

    databases = 3,

    approvals = 25,

    execution = "0.21 sec",

}) {

    return (

        <div className="analytics">

            <div className="analytics-header">

                <h2>

                    📊 AI Analytics Dashboard

                </h2>

                <p>

                    Live statistics of your AI Database Assistant

                </p>

            </div>

            <div className="analytics-grid">

                <div className="analytics-card">

                    <FaRobot className="analytics-icon"/>

                    <h3>

                        {queries}

                    </h3>

                    <span>

                        AI Queries

                    </span>

                </div>

                <div className="analytics-card">

                    <FaDatabase className="analytics-icon"/>

                    <h3>

                        {databases}

                    </h3>

                    <span>

                        Databases

                    </span>

                </div>

                <div className="analytics-card">

                    <FaCheckCircle className="analytics-icon"/>

                    <h3>

                        {approvals}

                    </h3>

                    <span>

                        OTP Approved

                    </span>

                </div>

                <div className="analytics-card">

                    <FaBolt className="analytics-icon"/>

                    <h3>

                        {execution}

                    </h3>

                    <span>

                        Avg Execution

                    </span>

                </div>

            </div>

            <div className="analytics-insight">

                <h3>

                    🧠 AI Insights

                </h3>

                <ul>

                    <li>

                        Most queried table :
                        <strong> Customers</strong>

                    </li>

                    <li>

                        Fastest query :
                        <strong> 0.09 sec</strong>

                    </li>

                    <li>

                        Largest database :
                        <strong> Chinook.db</strong>

                    </li>

                    <li>

                        AI Success Rate :
                        <strong> 99.1%</strong>

                    </li>

                </ul>

            </div>

        </div>

    );

}

export default AnalyticsDashboard;