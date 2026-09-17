import "./Message.css";

import {
    FaRobot,
    FaUser,
    FaCopy,
    FaDownload
} from "react-icons/fa";

function Message({ message }) {

    const copySQL = () => {

        if (message.sql) {

            navigator.clipboard.writeText(message.sql);

            alert("SQL Copied");

        }

    };

    const exportCSV = () => {

        if (!message.data || message.data.length === 0) return;

        const headers = Object.keys(message.data[0]);

        const rows = message.data.map(Object.values);

        const csv = [

            headers.join(","),

            ...rows.map(r => r.join(","))

        ].join("\n");

        const blob = new Blob([csv], {

            type: "text/csv"

        });

        const url = URL.createObjectURL(blob);

        const a = document.createElement("a");

        a.href = url;

        a.download = "results.csv";

        a.click();

    };

    return (

        <div

            className={`message-row ${message.sender}`}

        >

            <div className="avatar">

                {

                    message.sender === "user"

                        ? <FaUser />

                        : <FaRobot />

                }

            </div>

            <div className="bubble">

                <div className="message-text">

                    {message.text}

                </div>

                {

                    message.sql && (

                        <>

                            <div className="sql-header">

                                Generated SQL

                            </div>

                            <pre className="sql-box">

                                {message.sql}

                            </pre>

                            <button

                                className="sql-btn"

                                onClick={copySQL}

                            >

                                <FaCopy />

                                Copy SQL

                            </button>

                        </>

                    )

                }

                {

                    message.data &&

                    message.data.length > 0 && (

                        <>

                            <div className="table-header">

                                Query Results

                            </div>

                            <div className="table-wrapper">

                                <table>

                                    <thead>

                                        <tr>

                                            {

                                                Object.keys(message.data[0]).map(

                                                    key => (

                                                        <th key={key}>

                                                            {key}

                                                        </th>

                                                    )

                                                )

                                            }

                                        </tr>

                                    </thead>

                                    <tbody>

                                        {

                                            message.data.map(

                                                (row,index)=>(

                                                    <tr key={index}>

                                                        {

                                                            Object.values(row).map(

                                                                (value,i)=>(

                                                                    <td key={i}>

                                                                        {String(value)}

                                                                    </td>

                                                                )

                                                            )

                                                        }

                                                    </tr>

                                                )

                                            )

                                        }

                                    </tbody>

                                </table>

                            </div>

                            <button

                                className="export-btn"

                                onClick={exportCSV}

                            >

                                <FaDownload />

                                Export CSV

                            </button>

                        </>

                    )

                }

            </div>

        </div>

    );

}

export default Message;