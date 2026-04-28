import { useEffect, useState } from "react";
import API from "../services/api";

export default function Appointment() {
  const [doctors, setDoctors] = useState([]);
  const [patients, setPatients] = useState([]);

  const [doctorId, setDoctorId] = useState("");
  const [patientId, setPatientId] = useState("");

  useEffect(() => {
    API.get("/doctors/").then(res => setDoctors(res.data));
    API.get("/patients/").then(res => setPatients(res.data));
  }, []);

  const book = () => {
    if (!doctorId || !patientId) {
      alert("Select doctor and patient");
      return;
    }

    API.post("/appointment/", {
      doctor_id: parseInt(doctorId),
      patient_id: parseInt(patientId)
    }).then(() => alert("Appointment booked"));
  };

  return (
    <div className="container mt-4">
      <h2>Appointment</h2>

      <select className="form-control my-2"
        onChange={e => setDoctorId(e.target.value)}>
        <option value="">Select Doctor</option>
        {doctors.map(d => (
          <option key={d.id} value={d.id}>{d.name}</option>
        ))}
      </select>

      <select className="form-control my-2"
        onChange={e => setPatientId(e.target.value)}>
        <option value="">Select Patient</option>
        {patients.map(p => (
          <option key={p.id} value={p.id}>{p.name}</option>
        ))}
      </select>

      <button className="btn btn-warning" onClick={book}>
        Book Appointment
      </button>
    </div>
  );
}