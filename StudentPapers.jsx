import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";

export default function StudentPapers() {
  const { subjectId } = useParams();
  const [papers, setPapers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    axios
      .get(`http://127.0.0.1:8000/admin/papers/${subjectId}`)
      .then((res) => {
        setPapers(res.data || []);
        setLoading(false);
      })
      .catch(() => {
        setError("Failed to load papers");
        setLoading(false);
      });
  }, [subjectId]);

  if (loading) return <p className="p-6">Loading papers...</p>;
  if (error) return <p className="p-6 text-red-500">{error}</p>;

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Question Papers</h1>

      {papers.length === 0 ? (
        <p>No papers found for this subject.</p>
      ) : (
        <ul className="space-y-3">
          {papers.map((paper) => (
            <li key={paper.id} className="bg-blue p-4 rounded shadow">
              <a
  href={`http://127.0.0.1:8000${paper.image_path}`}
  target="_blank"
  rel="noopener noreferrer"
  className="text-blue-600 underline"
>
  View Paper
</a>

            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
