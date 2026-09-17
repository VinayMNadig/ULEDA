import "./Welcome.css";

import {
    FaDatabase,
    FaRobot,
    FaChartLine,
    FaCloudUploadAlt,
    FaCode,
    FaShieldAlt,
    FaArrowRight
} from "react-icons/fa";

function Welcome({ onExampleClick }) {

    const examples = [

        "Show all employees",

        "Find top 10 customers",

        "Generate sales chart",

        "List tables",

        "Insert a new employee",

        "Export invoice report"

    ];

    return (

        <div className="welcome">

            <div className="hero">

                <h1>
                    Universal LLM Database Assistant
                </h1>

                <p>

                    Upload any SQL database and interact with it using natural language.

                    Generate SQL, charts, reports and analytics instantly.

                </p>

            </div>

            <div className="feature-grid">

                <div className="feature-card">

                    <FaDatabase className="icon blue"/>

                    <h3>Multi Database</h3>

                    <p>

                        Connect SQLite, MySQL,

                        PostgreSQL and SQL Server.

                    </p>

                </div>

                <div className="feature-card">

                    <FaRobot className="icon purple"/>

                    <h3>AI SQL Generator</h3>

                    <p>

                        Convert English into optimized SQL queries.

                    </p>

                </div>

                <div className="feature-card">

                    <FaChartLine className="icon green"/>

                    <h3>Analytics</h3>

                    <p>

                        Charts, KPIs and dashboards automatically.

                    </p>

                </div>

                <div className="feature-card">

                    <FaShieldAlt className="icon orange"/>

                    <h3>OTP Protection</h3>

                    <p>

                        Secure INSERT UPDATE DELETE and ALTER operations.

                    </p>

                </div>

            </div>

            <div className="upload-card">

                <FaCloudUploadAlt className="upload-icon"/>

                <h2>Upload Database</h2>

                <p>

                    Drag & Drop

                    SQLite

                    MySQL

                    PostgreSQL

                    SQL Server

                </p>

                <button>

                    Upload Database

                </button>

            </div>

            <div className="examples">

                <h2>

                    Try asking...

                </h2>

                <div className="example-grid">

                    {

                        examples.map((item,index)=>(

                            <button

                                key={index}

                                className="example-btn"

                                onClick={()=>onExampleClick(item)}

                            >

                                <FaCode/>

                                {item}

                                <FaArrowRight/>

                            </button>

                        ))

                    }

                </div>

            </div>

        </div>

    );

}

export default Welcome;