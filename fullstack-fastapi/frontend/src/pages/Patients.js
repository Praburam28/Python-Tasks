import { useEffect, useState } from "react";
import API from "../services/api";

export default function Patients() {
  const [name, setName] = useState("");
  const [patients, setPatients] = useState([]);

  const load = () => {
    API.get("/patients/").then(res => setPatients(res.data));
  };

  useEffect(() => {
    load();
  }, []);

  const add = () => {
    API.post("/patients/", { name })
      .then(() => {
        alert("Patient added");
        setName("");
        load();
      })
      .catch(() => alert("Error"));
  };

  return (
    <div className="container mt-4">
      <h2>Patients</h2>

      <input className="form-control my-2"
        value={name}
        onChange={e => setName(e.target.value)}
        placeholder="Patient Name" />

      <button className="btn btn-success mb-3" onClick={add}>
        Add Patient
      </button>

      {patients.map(p => (
        <div className="card p-2 mb-2" key={p.id}>
          {p.name}
        </div>
      ))}
    </div>
  );
}