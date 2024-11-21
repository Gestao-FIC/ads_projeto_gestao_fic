"use client";

import React from "react";
import { CircularProgressbar, buildStyles } from "react-circular-progressbar";
import "react-circular-progressbar/dist/styles.css";

interface GaugeProps {
  value: number;
  total: number;
  colors?: "red" | "blue" | "green";
  types?: string;
}

export default function GaugeComponent({
  value,
  total,
  colors = "blue",
  types = "Cursos",
}: GaugeProps) {
  const percentage = (value / total) * 100;

  const getColor = () => {
    switch (colors) {
      case "red":
        return "#f87171"; // vermelho (Tailwind cor: 'red-400')
      case "green":
        return "#34d399"; // verde (Tailwind cor: 'green-400')
      case "blue":
      default:
        return "#60a5fa"; // azul (Tailwind cor: 'blue-400')
    }
  };

  return (
    <div className="flex flex-col items-center justify-center w-52 h-52 bg-white p-4 rounded-lg shadow-md">
      <div className="flex flex-col items-center mb-2">
        <p className="text-[0.6rem]">Progresso</p>
      </div>
      <CircularProgressbar
        value={percentage}
        text={`${percentage.toFixed(0)}%`}
        circleRatio={0.7}
        styles={buildStyles({
          textColor: "#000",
          pathColor: getColor(),
          trailColor: "#e5e7eb",
          rotation: 0.65,
        })}
      />
      <div className="text-center mt-2">
        <p className="text-xs">{`${value}/${total}`}</p>
        <p className="text-lg font-semibold">{types}</p>
      </div>
    </div>
  );
}
