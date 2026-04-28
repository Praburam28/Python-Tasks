import { Link, useNavigate } from "react-router-dom";

export default function Navbar() {
  const navigate = useNavigate();

  const logout = () => {
    localStorage.removeItem("token");
    navigate("/");
  };

  return (
    <nav className="navbar navbar-dark bg-primary p-3">
      <div className="container">
        <h4 className="text-white">🏥 MedApp</h4>

        <div>
          <Link className="btn btn-light mx-2" to="/doctors">Doctors</Link>
          <Link className="btn btn-light mx-2" to="/patients">Patients</Link>
          <Link className="btn btn-light mx-2" to="/appointment">Appointment</Link>

          <button className="btn btn-danger mx-2" onClick={logout}>
            Logout
          </button>
        </div>
      </div>
    </nav>
  );
}