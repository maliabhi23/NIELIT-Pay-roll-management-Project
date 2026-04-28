import { useEffect, useState } from "react";
import api from "../api";
import { toast } from "react-toastify";

export default function LeaveTable() {
  const [data, setData] = useState([]);

  const loadLeaves = () => {
    api.get("/leave")
      .then(res => setData(res.data));
  };

  useEffect(() => {
    loadLeaves();
  }, []);

  const approve = async (id) => {
    try {
      await api.put(`/leave/approve/${id}`);
      toast.success("Leave approved");
      loadLeaves();
    } catch {
      toast.error("Approve failed");
    }
  };

  const reject = async (id) => {
    try {
      await api.put(`/leave/reject/${id}`);
      toast.success("Leave rejected");
      loadLeaves();
    } catch {
      toast.error("Reject failed");
    }
  };

  return (
    <div className="table-box">
      <h2>Leave Requests</h2>
      <br />

      <table>
        <thead>
          <tr>
            <th>Employee ID</th>
            <th>Reason</th>
            <th>Status</th>
            <th>Action</th>
          </tr>
        </thead>

        <tbody>
          {data.map(e => (
            <tr key={e.id}>
              <td>{e.employee_id}</td>
              <td>{e.reason}</td>
              <td>
                <b
                  style={{
                    color:
                      e.status === "Approved"
                        ? "green"
                        : e.status === "Rejected"
                        ? "red"
                        : "#f39c12"
                  }}
                >
                  {e.status}
                </b>
              </td>

              <td>
                {e.status === "Pending" ? (
                  <>
                    <button
                      style={{
                        width: "90px",
                        marginRight: "8px"
                      }}
                      onClick={() => approve(e.id)}
                    >
                      Approve
                    </button>

                    <button
                      style={{
                        width: "90px",
                        background: "#c0392b"
                      }}
                      onClick={() => reject(e.id)}
                    >
                      Reject
                    </button>
                  </>
                ) : (
                  <span
                    style={{
                      fontWeight: "bold",
                      color: "#555"
                    }}
                  >
                    Completed
                  </span>
                )}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}