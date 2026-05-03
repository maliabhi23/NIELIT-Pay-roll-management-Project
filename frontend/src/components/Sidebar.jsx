export default function Sidebar({ setPage, logout }) {
  return (
    <div className="sidebar">
      <h2>NIELITPAY360 </h2>

      <div className="menu">
        <button onClick={() => setPage("dashboard")}>
          Dashboard
        </button>

        <button onClick={() => setPage("employees")}>
          Employees
        </button>

        <button onClick={() => setPage("leave")}>
          Leave
        </button>

        <button onClick={() => setPage("payroll")}>
          Payroll
        </button>

        <button onClick={() => setPage("reports")}>
          Reports
        </button>

        <button onClick={() => setPage("ai")}>
          AI Assistant
        </button>

        <button
          onClick={logout}
          style={{ background: "#c0392b" }}
        >
          Logout
        </button>
      </div>
    </div>
  );
}