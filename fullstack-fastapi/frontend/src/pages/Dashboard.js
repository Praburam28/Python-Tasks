export default function Dashboard() {
  return (
    <div>
      <h2>Dashboard</h2>

      <div className="row mt-4">
        <div className="col-md-4">
          <div className="card stat bg-primary text-white">
            Doctors
            <h2>--</h2>
          </div>
        </div>

        <div className="col-md-4">
          <div className="card stat bg-success text-white">
            Patients
            <h2>--</h2>
          </div>
        </div>

        <div className="col-md-4">
          <div className="card stat bg-warning">
            Appointments
            <h2>--</h2>
          </div>
        </div>
      </div>
    </div>
  );
}