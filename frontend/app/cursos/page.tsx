"use client";

import { DataTableDemo } from "@/components/testetable";
import React from "react";
import { CourseDetails } from "@/components/CourseDetails";

export default function Cursos() {
  const [selectedCourse, setSelectedCourse] = React.useState<Payment | null>(null);

  const handleCourseSelect = (course: any) => {
    setSelectedCourse(course);
  };

  const handleCloseSidebar = () => {
    setSelectedCourse(null);
  };

  return (
    <div className="flex h-screen w-full">
      <div className="flex-1 text-center content-center bg-gray-100 p-4">
        <div className="mx-auto max-w-7xl">
          <h1 className="text-2xl font-bold mb-4">Cursos</h1>
          <DataTableDemo onCourseSelect={handleCourseSelect} />
        </div>
      </div>
      
      {selectedCourse && (
        <div className="w-1/4 bg-white shadow-lg">
          <CourseDetails
            key={selectedCourse.id}
            course={selectedCourse}
            onClose={handleCloseSidebar}
          />
        </div>
      )}
    </div>
  );
}
