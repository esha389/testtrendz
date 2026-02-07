import { Link } from "react-router-dom";

export default function PredictionDashboard() {
  return (
    <div className="min-h-screen bg-gray-100 p-10">
      <h1 className="text-3xl font-bold mb-6">Prediction Dashboard</h1>

      <Link
        to="/"
        className="inline-block px-6 py-3 bg-indigo-600 text-white rounded"
      >
        Go to Student View
      </Link>
    </div>
  );
}
