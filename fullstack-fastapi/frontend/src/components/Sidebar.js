import { Link } from "react-router-dom";

export default function Sidebar() {
  return (
    <div
      style={{
        width: "220px",
        height: "100vh",
        background: "#0f172a",
        color: "white",
        padding: "20px"
      }}
    >
      <h4>🏥 MedApp</h4>

      <Link to="/dashboard" className="d-block text-white my-3">Dashboard</Link>
      <Link to="/doctors" className="d-block text-white my-3">Doctors</Link>
      <Link to="/patients" className="d-block text-white my-3">Patients</Link>
      <Link to="/appointment" className="d-block text-white my-3">Appointment</Link>
    </div>
  );
}