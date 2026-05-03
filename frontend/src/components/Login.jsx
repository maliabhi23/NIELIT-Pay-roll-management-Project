import { useState } from "react";
import api from "../api";
import { toast } from "react-toastify";

export default function Login({ setLoggedIn, setRole }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const login = async () => {
    try {
      const res = await api.post("/auth/login", {
        username,
        password
      });

      localStorage.setItem("token", res.data.access_token);
      localStorage.setItem("role", res.data.role);

      setRole(res.data.role);
      setLoggedIn(true);

      toast.success("Login successful");
    } catch {
      toast.error("Invalid credentials");
    }
  };

  return (
    <div className="login-page">
      <div className="login-box">
        <h1>NIELITPAY360 </h1>

        <input
          placeholder="Username"
          value={username}
          onChange={(e)=>setUsername(e.target.value)}
        />

        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e)=>setPassword(e.target.value)}
        />

        <button onClick={login}>
          Login
        </button>
      </div>
    </div>
  );
}