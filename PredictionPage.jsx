import React from "react";
import { useParams } from "react-router-dom";
import predictions from "../data/predictions";
import { SYLLABUS_TOPICS } from "../data/syllabusTopics";
import PredictionBarChart from "../components/PredictionBarChart";

export default function PredictionPage() {
  const { subjectId } = useParams();

  const subjectData = predictions[subjectId];
  const subjectName = subjectData?.subject;
  const syllabusUnits = SYLLABUS_TOPICS[subjectName];

  if (!subjectData) {
    return (
      <div className="min-h-screen flex items-center justify-center text-white text-2xl">
        No prediction data found.
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-indigo-900 via-purple-900 to-black p-10 text-white">
      
      {/* Title */}
      <h1 className="text-4xl font-bold mb-6">
        {subjectName} — Topic Prediction
      </h1>

      {/* Prediction Chart */}
      <PredictionBarChart topics={subjectData.topics} />

      {/* Explanation */}
      <p className="mt-8 text-purple-200 max-w-2xl">
        Based on analysis of previous university examination papers, the above
        topics have the highest probability of appearing in the upcoming exam.
        Students should prioritize these areas for efficient preparation.
      </p>

      {/* Full syllabus */}
      <div className="mt-12">
        <h2 className="text-3xl font-semibold mb-6">Complete Syllabus Topics</h2>

        {Object.entries(syllabusUnits).map(([unit, topics]) => (
          <div key={unit} className="mb-6 bg-white/10 p-5 rounded-xl">
            <h3 className="text-xl font-semibold mb-2">{unit}</h3>
            <ul className="list-disc ml-6 text-purple-100">
              {topics.map((t, i) => (
                <li key={i}>{t.topic}</li>
              ))}
            </ul>
          </div>
        ))}
      </div>
    </div>
  );
}
