import { useEffect, useState } from "react";
import api from "../api";
import { toast } from "react-toastify";

export default function AIAssistant() {
  const [question, setQuestion] = useState("");
  const [loading, setLoading] = useState(false);

  const [messages, setMessages] = useState(() => {
    const saved = localStorage.getItem("ai_chat_history");
    return saved ? JSON.parse(saved) : [];
  });

  useEffect(() => {
    localStorage.setItem(
      "ai_chat_history",
      JSON.stringify(messages)
    );
  }, [messages]);

  const askAI = async () => {
    if (!question.trim()) {
      toast.error("Ask something");
      return;
    }

    const userMsg = {
      role: "user",
      text: question
    };

    const updated = [...messages, userMsg];
    setMessages(updated);
    setQuestion("");
    setLoading(true);

    try {
      const res = await api.post("/ai/ask", {
        question,
        history: updated
      });

      setMessages([
        ...updated,
        {
          role: "assistant",
          text: res.data.answer
        }
      ]);
    } catch {
      toast.error("AI request failed");
    } finally {
      setLoading(false);
    }
  };

  const clearChat = () => {
    localStorage.removeItem("ai_chat_history");
    setMessages([]);
  };

  return (
    <div className="table-box">
      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          marginBottom: "15px"
        }}
      >
        <h2>AI Payroll Assistant</h2>

        <button
          onClick={clearChat}
          style={{
            width: "140px",
            background: "#c0392b"
          }}
        >
          Clear Chat
        </button>
      </div>

      <div
        style={{
          height: "420px",
          overflowY: "auto",
          background: "#f7f9fc",
          padding: "15px",
          borderRadius: "10px",
          marginBottom: "15px"
        }}
      >
        {messages.length === 0 && (
          <p style={{ color: "#666" }}>
            Start conversation with AI...
          </p>
        )}

        {messages.map((m, i) => (
          <div
            key={i}
            style={{
              marginBottom: "14px",
              display: "flex",
              justifyContent:
                m.role === "user"
                  ? "flex-end"
                  : "flex-start"
            }}
          >
            <div
              style={{
                maxWidth: "70%",
                padding: "12px 16px",
                borderRadius: "12px",
                whiteSpace: "pre-wrap",
                background:
                  m.role === "user"
                    ? "#0b1f4d"
                    : "#ffffff",
                color:
                  m.role === "user"
                    ? "#fff"
                    : "#111",
                boxShadow:
                  "0 2px 10px rgba(0,0,0,0.08)"
              }}
            >
              {m.text}
            </div>
          </div>
        ))}

        {loading && (
          <div style={{ color: "#666" }}>
            AI is thinking...
          </div>
        )}
      </div>

      <div
        style={{
          display: "flex",
          gap: "10px"
        }}
      >
        <input
          style={{ marginBottom: 0 }}
          placeholder="Ask payroll AI..."
          value={question}
          onChange={(e) =>
            setQuestion(e.target.value)
          }
          onKeyDown={(e) =>
            e.key === "Enter" && askAI()
          }
        />

        <button
          onClick={askAI}
          disabled={loading}
          style={{ widt
            h: "120px" }}
        >
          Send
        </button>
      </div>

    </div>
 
);

} 