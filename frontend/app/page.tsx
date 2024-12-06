"use client";

import { useEffect, useState } from "react";
import { ChartComponent } from "@/components/DashChart";
import DashCalendar from "@/components/DashCalendar";
import GaugeComponent from "@/components/DashGauge";
import { fetchGoals } from "@/utils/fetch/goal"; // Usa agora a função Axios

interface GoalApiResponse {
  id: string;
  year: number;
  goal_description: string;
  value: number;
}

export default function Dashboard() {
  const [goals, setGoals] = useState<GoalApiResponse[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchData = async () => {
      setLoading(true);
      setError(null);

      try {
        const data = await fetchGoals();
        setGoals(data);
      } catch (error) {
        console.error("Erro ao buscar as metas:", error);
        setError("Não foi possível carregar os dados das metas.");
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  return (
    <div className="flex flex-row h-full max-h-screen w-full bg-background">
      <div className="flex flex-1 flex-col p-4">
        <div className="flex flex-row justify-around">
          {loading ? (
            <p>Carregando metas...</p>
          ) : error ? (
            <p className="text-red-500">{error}</p>
          ) : (
            goals.map((gauge) => (
              <GaugeComponent
                key={gauge.id}
                id={gauge.id}
                year={gauge.year}
                value={300}
                total={gauge.value}
                types={gauge.goal_description}
              />
            ))
          )}
        </div>
        <div className="flex-1 flex flex-col">
          <p className="font-semibold text-xl mx-auto my-2">
            Carga horária do docente
          </p>
          <ChartComponent />
        </div>
      </div>
      <DashCalendar />
    </div>
  );
}
