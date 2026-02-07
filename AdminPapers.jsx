import { useEffect, useState } from "react";

export default function AdminPapers() {
  const [papers, setPapers] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/admin/papers")
      .then((res) => res.json())
      .then(setPapers)
      .catch(() => setPapers([]));
  }, []);

  return (
    <div className="p-10">
      <h1 className="text-2xl font-bold mb-6">Uploaded Papers</h1>

      <ul className="space-y-3">
        {papers.map((p, i) => (
          <li key={i} className="border p-4 rounded">
            {p.subject} – {p.year}
          </li>
        ))}
      </ul>
    </div>
  );
}
