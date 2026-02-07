import React from "react";
import { useNavigate } from "react-router-dom";

const subjects = [
  { id: 1, name: "Software Quality Testing" },
  { id: 2, name: "Object Oriented System Design" },
  { id: 3, name: "Unix Programming" },
  { id: 4, name: "Data Mining" },
  { id: 5, name: "ASP.NET" },
];

export default function StudentHome() {
  const navigate = useNavigate();

  return (
    <div className="min-h-screen bg-gradient-to-br from-indigo-900 to-black text-white p-10">
      <h1 className="text-4xl font-bold mb-6">
        🎓 Exam Prediction Dashboard
      </h1>
<p className="text-xl text-purple-200 mt-4 max-w-2xl">
  An AI-assisted academic analytics platform that analyses previous university
  question papers to predict high-priority exam topics using visual insights.
</p>


      <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
        {subjects.map((s) => (
          <div
            key={s.id}
            className="bg-white/10 backdrop-blur-lg rounded-xl p-6 hover:scale-105 transition"
          >
            <h2 className="text-xl font-semibold mb-4">{s.name}</h2>

            <div className="flex gap-3">
              <button
                onClick={() => navigate(`/papers/${s.id}`)}
                className="px-4 py-2 bg-blue-600 rounded hover:bg-blue-700"
              >
                📄 View Papers
              </button>

              <button
                onClick={() => navigate(`/predict/${s.id}`)}
                className="px-4 py-2 bg-purple-600 rounded hover:bg-purple-700"
              >
                📊 View Prediction
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
