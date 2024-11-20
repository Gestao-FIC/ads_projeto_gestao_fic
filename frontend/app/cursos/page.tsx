"use client";

import React from "react";
import { CourseDetails } from "@/components/CourseDetails";

export default function Cursos() {
  return (
    <div className="flex h-screen w-full bg-gray-100">
      <div className="flex-1">Course Table</div>
      <CourseDetails />
    </div>
  );
}
