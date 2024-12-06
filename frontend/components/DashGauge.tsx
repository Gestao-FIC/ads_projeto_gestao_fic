"use client";

import React, { useState, useRef, useEffect } from "react";
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
  total: initialTotal,
  colors = "blue",
  types = "Cursos",
}: GaugeProps) {
  const [total, setTotal] = useState(initialTotal);
  const [isEditing, setIsEditing] = useState(false);
  const inputRef = useRef<HTMLInputElement | null>(null);

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

  const handleEditTotal = () => setIsEditing(true);

  const handleTotalChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setTotal(Number(event.target.value));
  };

  const handleSaveTotal = async () => {
    setIsEditing(false);
    try {
      // Simula uma requisição PUT (substitua a URL pelo endpoint correto)
      await fetch("https://sua-api.com/endpoint", {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ total }),
      });
      console.log("Meta atualizada com sucesso!");
    } catch (error) {
      console.error("Erro ao atualizar a meta:", error);
    }
  };

  const handleBlur = () => {
    if (isEditing) handleSaveTotal();
  };

  const handleKeyDown = (event: React.KeyboardEvent<HTMLInputElement>) => {
    if (event.key === "Enter") {
      handleSaveTotal();
    }
  };

  // Foco automático ao entrar no modo de edição
  useEffect(() => {
    if (isEditing && inputRef.current) {
      inputRef.current.focus();
    }
  }, [isEditing]);

  return (
    <div className="flex flex-col items-center justify-center w-52 h-52 bg-white p-4 rounded-lg shadow-md">
      <CircularProgressbar
        value={percentage}
        text={`${percentage.toFixed(0)}%`}
        className="font-medium"
        circleRatio={0.7}
        styles={buildStyles({
          textColor: "#000",
          pathColor: getColor(),
          trailColor: "#e5e7eb",
          rotation: 0.65,
        })}
      />
      <div className="text-center mt-2">
        <p
          className="text-md cursor-pointer"
          onClick={handleEditTotal}
          title="Clique para editar"
        >
          {isEditing ? (
            <input
              ref={inputRef}
              type="number"
              value={total}
              className="border-b-2 border-blue-400 focus:outline-none text-center"
              onChange={handleTotalChange}
              onKeyDown={handleKeyDown}
              onBlur={handleBlur}
            />
          ) : (
            `${value}/${total}`
          )}
        </p>
        <p className="text-lg font-semibold">{types}</p>
      </div>
    </div>
  );
}
