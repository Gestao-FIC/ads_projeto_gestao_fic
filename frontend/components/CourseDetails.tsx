import * as React from "react";
import { courseDetails } from "@/mocks/mock";
import { diasSemana, iniciaisDias } from "@/mocks/mock";

export function CourseDetails() {
  // Função para estilizar os dias da semana
  const renderDiasSemana = () => {
    return diasSemana.map((dia, index) => {
      const isCursoDay = courseDetails.diaSemana.includes(dia);
      return (
        <span
          key={index}
          className={`mr-1 ${
            isCursoDay ? "font-bold text-yellow-400" : "text-secondary"
          }`}
        >
          {iniciaisDias[index]}
        </span>
      );
    });
  };

  return (
    <div className="bg-primary h-screen p-4 text-secondary shadow-md w-80 rounded-l-2xl">
      <h2 className="font-bold mb-4 text-xl text-white">Detalhes do Curso</h2>
      <hr className="mb-4 border-secondary" />
      <div className="space-y-2">
        <p className="flex justify-between">
          <span className="font-semibold text-white">Turno:</span>{" "}
          {courseDetails.turno === "M"
            ? "Manhã"
            : courseDetails.turno === "T"
            ? "Tarde"
            : "Noite"}
        </p>
        <p className="flex justify-between">
          <span className="font-semibold text-white">Carga Horária:</span>{" "}
          <p>{courseDetails.cargaHoraria}</p>
        </p>
        <p className="flex justify-between">
          <span className="font-semibold text-white">Dias da Semana:</span>{" "}
          <p>{renderDiasSemana()}</p>
        </p>
        <p className="flex justify-between">
          <span className="font-semibold text-white">Data Início:</span>{" "}
          <p>{courseDetails.dataInicio}</p>
        </p>
        <p className="flex justify-between">
          <span className="font-semibold text-white">Data Fim:</span>{" "}
          <p>{courseDetails.dataFim}</p>
        </p>
        <p className="flex justify-between">
          <span className="font-semibold text-white">Docente:</span>{" "}
          <p>{courseDetails.docente}</p>
        </p>
        <p className="flex justify-between">
          <span className="font-semibold text-white">Quórum:</span>{" "}
          <p>{courseDetails.quorum}%</p>
        </p>
      </div>
    </div>
  );
}
