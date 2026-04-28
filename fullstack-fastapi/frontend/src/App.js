import { BrowserRouter, Routes, Route } from "react-router-dom";

import Login from "./pages/Login";
import Doctors from "./pages/Doctors";
import Patients from "./pages/Patients";
import Appointment from "./pages/Appointment";
import ProtectedRoute from "./components/ProtectedRoute";
import Navbar from "./components/Navbar";

function App() {
  return (
    <BrowserRouter>
      <Routes>

        <Route path="/" element={<Login />} />

        <Route path="/doctors" element={
          <ProtectedRoute>
            <>
              <Navbar />
              <Doctors />
            </>
          </ProtectedRoute>
        } />

        <Route path="/patients" element={
          <ProtectedRoute>
            <>
              <Navbar />
              <Patients />
            </>
          </ProtectedRoute>
        } />

        <Route path="/appointment" element={
          <ProtectedRoute>
            <>
              <Navbar />
              <Appointment />
            </>
          </ProtectedRoute>
        } />

      </Routes>
    </BrowserRouter>
  );
}

export default App;