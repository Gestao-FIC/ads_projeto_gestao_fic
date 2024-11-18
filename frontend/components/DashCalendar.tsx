"use client";

import { Calendar } from "./ui/calendar";
import * as React from "react";

export default function DashCalendar() {
  const [date, setDate] = React.useState<Date | undefined>(new Date());

  return (
    <div className="bg-primary p-4 rounded-l-2xl">
      <Calendar
        mode="single"
        selected={date}
        onSelect={setDate}
        className="rounded-md border flex justify-center items-center"
        fixedWeeks
      />
    </div>
  );
}
