import { useState } from "react";
import api from "../api";
import { toast } from "react-toastify";

export default function AIAssistant() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const askAI = async () => {
    if (!question.trim()) {
      toast.error("Ask something");
      return;
    }

    try {
      const res = await api.post("/ai/ask", {
        question
      });

      setAnswer(res.data.answer);
    } catch {
      toast.error("AI request failed");
    }
  };

  return (
    <div className="table-box">
      <h2>AI Payroll Assistant</h2>
      <br />

      <input
        placeholder="Ask AI..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
      />

      <button
        style={{ marginBottom: "20px" }}
        onClick={askAI}
      >
        Ask
      </button>

      <div
        style={{
          background: "#f8f9fb",
          padding: "20px",
          borderRadius: "10px",
          minHeight: "120px",
          fontSize: "16px"
        }}
      >
        {answer || "Ask about payroll, leaves, salary..."}
      </div>
    </div>
  );
}