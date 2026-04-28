import { useState } from "react";
import { useNavigate } from "react-router-dom";
import API from "../services/api";

export default function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const login = () => {
    API.post("/login", { username, password })
      .then((res) => {
        localStorage.setItem("token", res.data.token);
        navigate("/doctors");
      })
      .catch(() => alert("Invalid login"));
  };

  return (
    <div className="container mt-5">
      <div className="card col-md-4 mx-auto p-4 shadow">
        <h3 className="text-center text-primary">Login</h3>

        <input
          className="form-control my-2"
          placeholder="Username"
          onChange={(e) => setUsername(e.target.value)}
        />

        <input
          type="password"
          className="form-control my-2"
          placeholder="Password"
          onChange={(e) => setPassword(e.target.value)}
        />

        <button className="btn btn-primary w-100" onClick={login}>
          Login
        </button>
      </div>
    </div>
  );
}