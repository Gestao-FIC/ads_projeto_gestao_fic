"use client";

import React, { useState, useRef, useEffect } from "react";
import { CircularProgressbar, buildStyles } from "react-circular-progressbar";
import "react-circular-progressbar/dist/styles.css";
import { updateGoal } from "@/utils/fetch/goal"; // Importa a função de atualização

interface GaugeProps {
  id: string; // ID da meta, necessário para o PUT
  year: number; //ano
  value: number; // Valor atual (progresso)
  total: number; // Meta inicial
  types?: string;
}

export default function GaugeComponent({
  id,
  year,
  value,
  total: initialTotal,
  types,
}: GaugeProps) {
  const [total, setTotal] = useState(initialTotal);
  const [isEditing, setIsEditing] = useState(false);
  const [error, setError] = useState<string | null>(null); // Para exibir erros, se houver
  const inputRef = useRef<HTMLInputElement | null>(null);

  const percentage = (value / total) * 100;

  const getColor = () => {
    switch (types) {
      case "receita":
        return "#f87171"; // vermelho (Tailwind cor: 'red-400')
      case "matriculas":
        return "#34d399"; // verde (Tailwind cor: 'green-400')
      case "cursos":
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
    setError(null); // Limpa o erro antes de tentar salvar

    try {
      // Chama a função de atualização no backend
      await updateGoal(id, {
        year: year,
        goal_description: types,
        value: total,
      });
      console.log("Meta atualizada com sucesso!");
    } catch (error) {
      console.error("Erro ao atualizar a meta:", error);
      setError("Erro ao salvar a meta. Tente novamente.");
    }
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
              onBlur={() => {
                setIsEditing(false);
                setTotal(initialTotal);
              }}
            />
          ) : types != "receita" ? (
            <>
              {Math.round(value)}/{Math.round(total)}
            </>
          ) : (
            <>
              {value} / {total}
            </>
          )}
        </p>
        <p className="font-semibold first-letter:uppercase">{types}</p>
        {error && <p className="text-sm text-red-500 mt-1">{error}</p>}
      </div>
    </div>
  );
}
