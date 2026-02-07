import React, { useRef, useEffect, useState } from "react";
import { Bar } from "react-chartjs-2";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Tooltip,
  Legend,
} from "chart.js";

ChartJS.register(CategoryScale, LinearScale, BarElement, Tooltip, Legend);

export default function PredictionBarChart({ topics }) {
  const chartRef = useRef(null);
  const [gradient, setGradient] = useState(null);

  // Create gradient after chart mounts
  useEffect(() => {
    const chart = chartRef.current;
    if (!chart) return;

    const ctx = chart.ctx;
    const gradientFill = ctx.createLinearGradient(0, 0, 0, 400);

    gradientFill.addColorStop(0, "#000000");   // pure black top
    gradientFill.addColorStop(1, "#434343");   // soft dark gray bottom

    setGradient(gradientFill);
  }, []);

  const data = {
    labels: topics.map(t => t.topic),
    datasets: [
      {
        label: "Weight",
        data: topics.map(t => t.weight),
        backgroundColor: gradient || "#000", // fallback before gradient loads
        borderRadius: 10,
        borderSkipped: false,
      },
    ],
  };

  const options = {
    responsive: true,
    plugins: {
      legend: { display: false },
      tooltip: {
        backgroundColor: "#111",
        titleColor: "#fff",
        bodyColor: "#fff",
      },
    },
    scales: {
      x: {
        ticks: { color: "#fff" },
        grid: { display: false },
      },
      y: {
        ticks: { color: "#fff" },
        grid: { color: "rgba(255,255,255,0.1)" },
      },
    },
  };

  return (
    <div className="bg-white/10 p-6 rounded-2xl">
      <Bar ref={chartRef} data={data} options={options} />
    </div>
  );
}
