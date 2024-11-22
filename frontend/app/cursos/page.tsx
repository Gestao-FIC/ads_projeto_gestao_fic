"use client";

import React, { useState } from "react";
import { CourseDetails } from "@/components/CourseDetails";
import { CourseTable } from "@/components/CourseTable";
import { CoursesType } from "@/mocks/mock";

export default function Cursos() {
  const [selectedCourse, setSelectedCourse] = useState<CoursesType | null>(
    null
  );

  return (
    <div className="flex max-h-screen w-full bg-background">
      <CourseTable setSelectedCourse={setSelectedCourse} />
      <CourseDetails course={selectedCourse} />
    </div>
  );
}
