import DashCalendar from "@/components/DashCalendar";

export default function Dashboard() {
  return (
    <div className="flex flex-row h-full w-full bg-secondary">
      <div className="flex-1">clean</div>
      <DashCalendar />
    </div>
  );
}
