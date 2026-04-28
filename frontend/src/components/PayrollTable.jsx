import { useEffect, useState } from "react";
import api from "../api";
import { toast } from "react-toastify";

export default function PayrollTable() {
  const [employees, setEmployees] = useState([]);
  const [payroll, setPayroll] = useState([]);

  const loadData = async () => {
    const emp = await api.get("/employees");
    const sal = await api.get("/payroll");

    setEmployees(emp.data);
    setPayroll(sal.data);
  };

  useEffect(() => {
    loadData();
  }, []);

  const processSalary = async (id) => {
    try {
      await api.post(`/payroll/process/${id}`);
      toast.success("Salary processed");
      loadData();
    } catch {
      toast.error("Processing failed");
    }
  };

  return (
    <>
      <div className="table-box" style={{ marginBottom: "25px" }}>
        <h2>Process Salary</h2>
        <br />

        <table>
          <thead>
            <tr>
              <th>Employee</th>
              <th>Department</th>
              <th>Action</th>
            </tr>
          </thead>

          <tbody>
            {employees.map(e => (
              <tr key={e.id}>
                <td>{e.name}</td>
                <td>{e.department}</td>
                <td>
                  <button
                    style={{ width: "160px" }}
                    onClick={() => processSalary(e.id)}
                  >
                    Process Salary
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <div className="table-box">
        <h2>Salary History</h2>
        <br />

        <table>
          <thead>
            <tr>
              <th>Employee ID</th>
              <th>Gross</th>
              <th>PF</th>
              <th>Tax</th>
              <th>Net Salary</th>
              <th>Month</th>
            </tr>
          </thead>

          <tbody>
            {payroll.map((e, i) => (
              <tr key={i}>
                <td>{e.employee_id}</td>
                <td>₹ {e.gross}</td>
                <td>₹ {e.pf}</td>
                <td>₹ {e.tax}</td>
                <td>₹ {e.net_salary}</td>
                <td>{e.month}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </>
  );
}