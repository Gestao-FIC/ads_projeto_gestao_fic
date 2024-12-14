import * as React from "react";
import { CoursesType } from "@/mocks/mock";
import { diasSemana, iniciaisDias } from "@/mocks/mock";

export function CourseDetails({ course }: { course: CoursesType | null }) {
  // Função para estilizar os dias da semana
  // const renderDiasSemana = () => {
  //   return diasSemana.map((dia, index) => {
  //     const isCursoDay = course?.diaSemana.includes(dia);
  //     return (
  //       <span
  //         key={index}
  //         className={`mr-1 ${
  //           isCursoDay ? "font-bold text-yellow-400" : "text-secondary"
  //         }`}
  //       >
  //         {iniciaisDias[index]}
  //       </span>
  //     );
  //   });
  // };

  if (!course) {
    return (
      <div className="bg-primary h-screen p-4 text-secondary shadow-md w-80 rounded-l-2xl">
        <h2 className="font-bold mb-4 text-xl text-white">Detalhes do Curso</h2>
        <hr className="mb-4 border-secondary" />
        <p className="text-center text-white">
          Selecione um curso para ver os detalhes.
        </p>
      </div>
    );
  }

  return (
    <div className="bg-primary h-screen p-4 text-secondary shadow-md w-80 rounded-l-2xl">
      <h2 className="font-bold mb-4 text-xl text-white">Detalhes do Curso</h2>
      <hr className="mb-4 border-secondary" />
      <div className="space-y-2">
        <p className="flex justify-between">
          <span className="font-semibold text-white">Turno:</span>{" "}
          {course.shift === "M"
            ? "Manhã"
            : course.shift === "T"
            ? "Tarde"
            : "Noite"}
        </p>
        <p className="flex justify-between">
          <span className="font-semibold text-white">Carga Horária:</span>
          <p>{course.duration}</p>
        </p>
        {/* <p className="flex justify-between">
          <span className="font-semibold text-white">Dias da Semana:</span>
          <p>{renderDiasSemana()}</p>
        </p> */}
        <p className="flex justify-between">
          <span className="font-semibold text-white">Data Início:</span>
          <p>{course.period_from}</p>
        </p>
        <p className="flex justify-between">
          <span className="font-semibold text-white">Data Fim:</span>
          <p>{course.period_to}</p>
        </p>
        <p className="flex justify-between">
          <span className="font-semibold text-white">Docente:</span>
          <p>{course.teacher}</p>
        </p>
        <p className="flex justify-between">
          <span className="font-semibold text-white">Quórum:</span>
          <p>{course.quorum}%</p>
        </p>
      </div>
    </div>
  );
}
