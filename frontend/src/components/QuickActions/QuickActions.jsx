import "./QuickActions.css";

import {
    FaDatabase,
    FaChartBar,
    FaTable,
    FaDownload,
    FaRobot,
    FaHistory
} from "react-icons/fa";

function QuickActions() {

    const actions = [

        {
            icon: <FaDatabase />,
            title: "Upload Database",
            desc: "Import SQLite, MySQL or PostgreSQL"
        },

        {
            icon: <FaRobot />,
            title: "Ask AI",
            desc: "Generate SQL using natural language"
        },

        {
            icon: <FaTable />,
            title: "Browse Tables",
            desc: "View all tables and records"
        },

        {
            icon: <FaChartBar />,
            title: "Analytics",
            desc: "Generate AI charts instantly"
        },

        {
            icon: <FaDownload />,
            title: "Export Report",
            desc: "Download CSV or PDF reports"
        },

        {
            icon: <FaHistory />,
            title: "Chat History",
            desc: "Continue previous conversations"
        }

    ];

    return (

        <div className="quick-actions">

            {actions.map((item,index)=>(

                <div
                    className="quick-card"
                    key={index}
                >

                    <div className="quick-icon">

                        {item.icon}

                    </div>

                    <h3>{item.title}</h3>

                    <p>{item.desc}</p>

                </div>

            ))}

        </div>

    );

}

export default QuickActions;