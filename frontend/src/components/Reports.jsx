import { useEffect, useState } from "react";
import api from "../api";

export default function Reports() {
  const [data, setData] = useState({
    employees: 0,
    pending_leaves: 0,
    payroll_processed: 0,
    current_month: "",
    current_month_salary_paid: 0
  });

  useEffect(() => {
    api.get("/reports/summary")
      .then(res => setData(res.data));
  }, []);

  return (
    <div className="table-box">
      <h2>Reports Summary</h2>

      <table>
        <tbody>
          <tr>
            <td>Total Employees</td>
            <td>{data.employees}</td>
          </tr>

          <tr>
            <td>Pending Leaves</td>
            <td>{data.pending_leaves}</td>
          </tr>

          <tr>
            <td>Payroll This Month</td>
            <td>{data.payroll_processed}</td>
          </tr>

          <tr>
            <td>Current Month</td>
            <td>{data.current_month}</td>
          </tr>
          <tr>
            <td>Salary Paid</td>
            <td>₹ {data.current_month_salary_paid}</td>
          </tr>
        </tbody>
      </table>
    </div>
  );
}