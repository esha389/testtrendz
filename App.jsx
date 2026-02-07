import React from "react";
import { Routes, Route } from "react-router-dom";
import StudentHome from "./pages/StudentHome";
import StudentPapers from "./pages/StudentPapers";
import PredictionDashboard from "./pages/PredictionDashboard";
import PredictionPage from "./pages/PredictionPage";

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<StudentHome />} />
      <Route path="/papers/:subjectId" element={<StudentPapers />} />
      <Route path="/predict" element={<PredictionDashboard />} />
      <Route path="/predict/:subjectId" element={<PredictionPage />} />
    </Routes>
  );
}
