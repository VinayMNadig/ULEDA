import "./History.css";

import {
    FaRobot,
    FaClock,
    FaDatabase,
    FaCheckCircle,
    FaSearch,
} from "react-icons/fa";

function History() {

    const history = [

        {

            day: "Today",

            items: [

                {

                    question: "Show all customers",

                    sql: "SELECT * FROM Customers",

                    status: "Executed",

                    time: "10:45 AM",

                },

                {

                    question: "Add Phone column",

                    sql: "ALTER TABLE Customers ADD COLUMN Phone TEXT",

                    status: "OTP Approved",

                    time: "10:12 AM",

                },

            ],

        },

        {

            day: "Yesterday",

            items: [

                {

                    question: "Show top albums",

                    sql: "SELECT * FROM Albums LIMIT 10",

                    status: "Executed",

                    time: "4:15 PM",

                },

            ],

        },

    ];

    return (

        <div className="history-page">

            <div className="history-header">

                <h2>

                    📜 History

                </h2>

                <p>

                    Previous AI conversations and executed SQL queries.

                </p>

            </div>

            <div className="history-search">

                <FaSearch />

                <input

                    type="text"

                    placeholder="Search history..."

                />

            </div>

            {

                history.map((section,index)=>(

                    <div

                        key={index}

                        className="history-section"

                    >

                        <h3>

                            {section.day}

                        </h3>

                        {

                            section.items.map((item,i)=>(

                                <div

                                    key={i}

                                    className="history-card"

                                >

                                    <div className="history-top">

                                        <FaRobot />

                                        <span>

                                            {item.question}

                                        </span>

                                    </div>

                                    <div className="history-sql">

                                        <FaDatabase />

                                        <code>

                                            {item.sql}

                                        </code>

                                    </div>

                                    <div className="history-bottom">

                                        <div>

                                            <FaCheckCircle />

                                            {item.status}

                                        </div>

                                        <div>

                                            <FaClock />

                                            {item.time}

                                        </div>

                                    </div>

                                </div>

                            ))

                        }

                    </div>

                ))

            }

        </div>

    );

}

export default History;