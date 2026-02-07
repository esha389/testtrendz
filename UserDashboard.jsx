import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

export default function UserHome() {
  const [subjects, setSubjects] = useState([]);
  const [papers, setPapers] = useState([]);
  const [selectedSubject, setSelectedSubject] = useState("");
  const [error, setError] = useState("");

  const navigate = useNavigate();

  // Fetch subjects
  useEffect(() => {
    fetch("http://127.0.0.1:8000/admin/subjects")
      .then((res) => res.json())
      .then(setSubjects)
      .catch(() => setError("Failed to load subjects"));
  }, []);

  // Fetch papers
  useEffect(() => {
    fetch("http://127.0.0.1:8000/admin/papers")
      .then((res) => res.json())
      .then(setPapers)
      .catch(() => setError("Failed to load papers"));
  }, []);

  const filteredPapers = selectedSubject
    ? papers.filter((p) => p.subject_id === Number(selectedSubject))
    : [];

  return (
    <div className="p-6 max-w-5xl mx-auto">
      <h1 className="text-3xl font-bold mb-6">📚 Question Papers</h1>

      {error && <p className="text-red-600 mb-4">{error}</p>}

      {/* Subject selector */}
      <select
        className="border p-2 mb-6 w-full max-w-sm"
        value={selectedSubject}
        onChange={(e) => setSelectedSubject(e.target.value)}
      >
        <option value="">Select Subject</option>
        {subjects.map((s) => (
          <option key={s.id} value={s.id}>
            {s.name}
          </option>
        ))}
      </select>

      {/* Papers table */}
      {filteredPapers.length > 0 && (
        <table className="w-full border">
          <thead>
            <tr className="bg-gray-200">
              <th className="border p-2">Year</th>
              <th className="border p-2">Exam Type</th>
              <th className="border p-2">Action</th>
            </tr>
          </thead>
          <tbody>
            {filteredPapers.map((p) => (
              <tr key={p.id}>
                <td className="border p-2">{p.year}</td>
                <td className="border p-2">{p.exam_type}</td>
                <td className="border p-2">
                  <button
                    className="bg-blue-600 text-white px-3 py-1 rounded"
                    onClick={() => navigate(`/papers/${p.id}`)}
                  >
                    View Questions
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}

      {selectedSubject && filteredPapers.length === 0 && (
        <p>No papers found for this subject.</p>
      )}
    </div>
  );
}