//import "./Analytics.css";

import {
    FaDatabase,
    FaRobot,
    FaClock,
    FaCheckCircle,
    FaChartBar,
    FaBrain
} from "react-icons/fa";

function Analytics() {

    return (

        <div className="analytics-page">

            <div className="analytics-header">

                <h1>📊 Analytics Dashboard</h1>

                <p>
                    Monitor AI performance, database activity and query statistics.
                </p>

            </div>

            <div className="analytics-grid">

                <div className="analytics-card">

                    <FaRobot className="analytics-icon" />

                    <h2>AI Queries</h2>

                    <h1>128</h1>

                    <p>Total AI queries executed</p>

                </div>

                <div className="analytics-card">

                    <FaDatabase className="analytics-icon" />

                    <h2>Databases</h2>

                    <h1>5</h1>

                    <p>Connected databases</p>

                </div>

                <div className="analytics-card">

                    <FaCheckCircle className="analytics-icon" />

                    <h2>OTP Approved</h2>

                    <h1>26</h1>

                    <p>Secure SQL approvals</p>

                </div>

                <div className="analytics-card">

                    <FaClock className="analytics-icon" />

                    <h2>Avg Execution</h2>

                    <h1>0.82 s</h1>

                    <p>Average execution time</p>

                </div>

            </div>

            <div className="insight-card">

                <div className="insight-title">

                    <FaBrain />

                    <span>AI Insights</span>

                </div>

                <ul>

                    <li>✔ Database performance is healthy.</li>

                    <li>✔ Most queries complete in under 1 second.</li>

                    <li>✔ OTP approval rate is high.</li>

                    <li>✔ No abnormal SQL activity detected.</li>

                </ul>

            </div>

            <div className="chart-placeholder">

                <FaChartBar size={60} />

                <h2>Charts Coming Soon</h2>

                <p>
                    Query trends, execution graphs and AI analytics will appear here.
                </p>

            </div>

        </div>

    );

}

export default Analytics;