import ResultTable from "./ResultTable";

function Message({ message }) {
  const isUser = message.sender === "user";

  const copySQL = () => {
    navigator.clipboard.writeText(message.sql);
    alert("SQL copied to clipboard!");
  };

  return (
    <div className={`message-row ${isUser ? "user-row" : "bot-row"}`}>
      <div className="avatar">
        {isUser ? "👤" : "🤖"}
      </div>

      <div
        className={
          isUser
            ? "message user-message"
            : "message bot-message"
        }
      >
        <p>{message.text}</p>

        {message.sql && (
          <details className="sql-box">
            <summary>Generated SQL</summary>

            <pre>{message.sql}</pre>

            <button
              className="copy-btn"
              onClick={copySQL}
            >
              📋 Copy SQL
            </button>
          </details>
        )}

        {message.data && message.data.length > 0 && (
          <details className="data-box">
            <summary>
              Database Results ({message.data.length})
            </summary>

            <ResultTable data={message.data} />
          </details>
        )}
      </div>
    </div>
  );
}

export default Message;