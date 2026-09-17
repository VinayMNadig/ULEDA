import "./DatabaseCard.css";

function DatabaseCard({
    database,
    active,
    connect,
    disconnect,
    remove,
}) {

    return (

        <div
            className={
                active
                    ? "database-card active"
                    : "database-card"
            }
        >

            <div>

                <h3>
                    {database.name}
                </h3>

                <p>
                    <b>Size:</b> {database.size} KB
                </p>

                <p>
                    <b>Path:</b> {database.path}
                </p>

            </div>

            <div
                style={{
                    display: "flex",
                    gap: "10px",
                }}
            >

                {!active && (

                    <button
                        className="connect-btn"
                        onClick={() =>
                            connect(database.name)
                        }
                    >
                        Connect
                    </button>

                )}

                {active && (

                    <button
                        className="connect-btn"
                        style={{
                            background: "#dc2626",
                        }}
                        onClick={() =>
                            disconnect &&
                            disconnect()
                        }
                    >
                        Disconnect
                    </button>

                )}

                <button
                    className="connect-btn"
                    style={{
                        background: "#ef4444",
                    }}
                    onClick={() =>
                        remove &&
                        remove(database.name)
                    }
                >
                    Delete
                </button>

            </div>

        </div>

    );

}

export default DatabaseCard;