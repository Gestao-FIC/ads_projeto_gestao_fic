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
    amend: events
      .filter((event) => event.type === "amend")
      .map((event) => event.date),
    event: events
      .filter((event) => event.type === "event")
      .map((event) => event.date),
    others: events
      .filter((event) => event.type === "others")
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
          event: "bg-green-200 text-black",
          other: "bg-red-200 text-black",
          amend: "bg-blue-200 text-black",
        }}
      />

      <div className="flex flex-row gap-4 justify-center p-8">
        <div className="flex items-center gap-2">
          <span className="w-4 h-4 rounded-full bg-yellow-200 border"></span>
          <span className="text-secondary">Feriado</span>
        </div>
        <div className="flex items-center gap-2">
          <span className="w-4 h-4 rounded-full bg-green-200 border"></span>
          <span className="text-secondary">Emenda</span>
        </div>
        <div className="flex items-center gap-2">
          <span className="w-4 h-4 rounded-full bg-red-200 border"></span>
          <span className="text-secondary">Evento</span>
        </div>
        <div className="flex items-center gap-2">
          <span className="w-4 h-4 rounded-full bg-blue-200 border"></span>
          <span className="text-secondary">Outros</span>
        </div>
      </div>

      <DashCalendarForm />
    </div>
  );
}
