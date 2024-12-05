import { ChartComponent } from "@/components/DashChart";
import DashCalendar from "@/components/DashCalendar";
import GaugeComponent from "@/components/DashGauge";
import { gaugeData } from "@/mocks/mock";

export default function Dashboard() {
  return (
    <div className="flex flex-row h-full max-h-screen w-full bg-background">
      <div className="flex flex-1 flex-col p-4">
        <div className="flex flex-row justify-around">
          {/* Mapeia sobre os dados mockados e renderiza os gauges */}
          {gaugeData.map((gauge, index) => (
            <GaugeComponent
              key={index}
              value={gauge.value}
              total={gauge.total}
              colors={gauge.colorOption}
              types={gauge.type}
            />
          ))}
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
