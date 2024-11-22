import EducatorCalendar from "@/components/EducatorCalendar";
import { TeacherTable } from "@/components/TeacherTable";
import React from "react";

export default function Docentes() {
  return (
    <div className="flex h-screen bg-background">
      <div className="flex-1"></div>
      <TeacherTable />
      <EducatorCalendar />
    </div>
  );
}
