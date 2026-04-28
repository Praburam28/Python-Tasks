import Sidebar from "./Sidebar";
import Navbar from "./Navbar";

export default function Layout({ children }) {
  return (
    <div className="d-flex">
      <Sidebar />

      <div className="w-100">
        <Navbar />
        <div className="p-4">{children}</div>
      </div>
    </div>
  );
}