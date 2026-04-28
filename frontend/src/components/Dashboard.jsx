import { useEffect, useState } from "react";
import api from "../api";

export default function Dashboard() {
  const [summary, setSummary] = useState({
    employees: 0,
    pending_leaves: 0,
    payroll_processed: 0,
    current_month: "",
    current_month_salary_paid: 0
  });

  useEffect(() => {
    api.get("/reports/summary")
      .then(res => setSummary(res.data))
      .catch(() => {});
  }, []);

  return (
    <>
      <div className="cards">
        <div className="card">
          <h3>Total Employees</h3>
          <h1>{summary.employees}</h1>
        </div>

        <div className="card">
          <h3>Pending Leaves</h3>
          <h1>{summary.pending_leaves}</h1>
        </div>

        <div className="card">
          <h3>Payroll This Month</h3>
          <h1>{summary.payroll_processed}</h1>
        </div>
      </div>

      <div className="table-box">
        <h2>Current Month Salary Paid</h2>
        <br />

        <p style={{
          color:"#666",
          marginBottom:"12px",
          fontWeight:"bold"
        }}>
          {summary.current_month}
        </p>

        <h1 style={{ color:"#0b1f4d" }}>
          ₹ {summary.current_month_salary_paid}
        </h1>
      </div>
    </>
  );
}