import { useState } from "react";
import { ToastContainer } from "react-toastify";

import Login from "./components/Login";
import Sidebar from "./components/Sidebar";
import Dashboard from "./components/Dashboard";
import EmployeeTable from "./components/EmployeeTable";
import LeaveTable from "./components/LeaveTable";
import PayrollTable from "./components/PayrollTable";
import Reports from "./components/Reports";
import AIAssistant from "./components/AIAssistant";

export default function App() {
  const [loggedIn, setLoggedIn] = useState(
    !!localStorage.getItem("token")
  );

  const [role, setRole] = useState(
    localStorage.getItem("role") || "admin"
  );

  const [page, setPage] = useState("dashboard");

  const logout = () => {
    localStorage.clear();
    setLoggedIn(false);
    setRole("");
    setPage("dashboard");
  };

  if (!loggedIn) {
    return (
      <>
        <Login
          setLoggedIn={setLoggedIn}
          setRole={setRole}
        />
        <ToastContainer />
      </>
    );
  }

  const renderPage = () => {
    switch (page) {
      case "dashboard":
        return <Dashboard />;
      case "employees":
        return <EmployeeTable />;
      case "leave":
        return <LeaveTable />;
      case "payroll":
        return <PayrollTable />;
      case "reports":
        return <Reports />;
      case "ai":
        return <AIAssistant />;
      default:
        return <Dashboard />;
    }
  };

  return (
    <>
      <div className="layout">
        <Sidebar
          setPage={setPage}
          logout={logout}
        />

        <div className="content">
          {renderPage()}
        </div>
      </div>

      <ToastContainer />
    </>
  );
}