import { useEffect, useState } from "react";
import API from "../services/api";

export default function Doctors() {
  const [name, setName] = useState("");
  const [doctors, setDoctors] = useState([]);

  const load = () => {
    API.get("/doctors/").then(res => setDoctors(res.data));
  };

  useEffect(() => {
    load();
  }, []);

  const add = () => {
    API.post("/doctors/", { name })
      .then(() => {
        alert("Doctor added");
        setName("");
        load();
      })
      .catch(() => alert("Error"));
  };

  return (
    <div className="container mt-4">
      <h2>Doctors</h2>

      <input className="form-control my-2"
        value={name}
        onChange={e => setName(e.target.value)}
        placeholder="Doctor Name" />

      <button className="btn btn-success mb-3" onClick={add}>
        Add Doctor
      </button>

      {doctors.map(d => (
        <div className="card p-2 mb-2" key={d.id}>
          {d.name}
        </div>
      ))}
    </div>
  );
}