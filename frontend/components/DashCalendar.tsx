"use client";

import DashCalendarForm from "./DashForm";
import { Calendar } from "./ui/calendar";
import * as React from "react";
import { events } from "@/mocks/mock";

export default function DashCalendar() {
  const [date, setDate] = React.useState<Date | undefined>(new Date());

  const modifiers = {
    holiday: events
      .filter((event) => event.type === "holiday")
      .map((event) => event.date),
    vacation: events
      .filter((event) => event.type === "vacation")
      .map((event) => event.date),
    blockage: events
      .filter((event) => event.type === "blockage")
      .map((event) => event.date),
  };

  return (
    <div className="bg-primary p-4 rounded-l-2xl">
      <Calendar
        mode="single"
        selected={date}
        onSelect={setDate}
        className="rounded-md border flex justify-center items-center"
        fixedWeeks
        modifiers={modifiers}
        modifiersClassNames={{
          holiday: "bg-yellow-200 text-black",
          vacation: "bg-green-200 text-black",
          blockage: "bg-red-200 text-black",
        }}
      />

      <div className="flex flex-row gap-4 justify-center p-8">
        <div className="flex items-center gap-2">
          <span className="w-4 h-4 rounded-full bg-yellow-200 border"></span>
          <span className="text-secondary">Feriado</span>
        </div>
        <div className="flex items-center gap-2">
          <span className="w-4 h-4 rounded-full bg-green-200 border"></span>
          <span className="text-secondary">Férias</span>
        </div>
        <div className="flex items-center gap-2">
          <span className="w-4 h-4 rounded-full bg-red-200 border"></span>
          <span className="text-secondary">Bloqueio</span>
        </div>
      </div>

      <DashCalendarForm />
    </div>
  );
}
