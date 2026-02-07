import { useState } from "react";

export default function AdminUpload() {
  const [file, setFile] = useState(null);

  const handleUpload = () => {
    if (!file) return;
    alert("Upload handled on backend");
  };

  return (
    <div className="p-10">
      <h1 className="text-2xl font-bold mb-4">Admin Upload</h1>

      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
        className="mb-4"
      />

      <button
        onClick={handleUpload}
        className="px-4 py-2 bg-green-600 text-white rounded"
      >
        Upload
      </button>
    </div>
  );
}
