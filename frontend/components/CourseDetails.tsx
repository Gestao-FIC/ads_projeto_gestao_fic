import * as React from "react";
import { X } from "lucide-react";
import { Payment } from "../path-to-your-file";

interface CourseDetailsProps {
  course: Payment;
  onClose: () => void;
}

export function CourseDetails({ course, onClose }: CourseDetailsProps) {
  // Definindo os dias da semana e suas iniciais
  const diasSemana = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"];
  const iniciaisDias = ["D", "S", "T", "Q", "Q", "S", "S"];

  // Função para estilizar os dias da semana
  const renderDiasSemana = () => {
    return diasSemana.map((dia, index) => {
      const isCursoDay = course.diaSemana.includes(dia);
      return (
        <span
          key={index}
          className={`mr-1 ${isCursoDay ? 'font-bold text-yellow-400' : 'text-secondary'}`}
        >
          {iniciaisDias[index]}
        </span>
      );
    });
  };

  return (
    <div className="bg-primary h-full p-4 text-secondary shadow-md relative">
      <button
        onClick={onClose}
        className="absolute top-2 right-2 text-secondary hover:text-white transition"
      >
        <X size={24} />
      </button>
      <h2 className="font-bold mb-4 text-xl text-white">Detalhes do Curso</h2>
      <hr className="mb-4 border-secondary" />
      <div className="space-y-2">
        <p className="flex justify-between">
          <span className="font-semibold text-white">Turno:</span>{" "}
          {course.turno === "M" ? "Manhã" : course.turno === "T" ? "Tarde" : "Noite"}
        </p>
        <p className="flex justify-between">
          <span className="font-semibold text-white">Carga Horária:</span> <p>{course.cargaHoraria}</p>
        </p>
        <p className="flex justify-between">
          <span className="font-semibold text-white">Dias da Semana:</span> <p>{renderDiasSemana()}</p>
        </p>
        <p className="flex justify-between">
          <span className="font-semibold text-white">Data Início:</span> <p>{course.dataInicio}</p>
        </p>
        <p className="flex justify-between">
          <span className="font-semibold text-white">Data Fim:</span> <p>{course.dataFim}</p>
        </p>
        <p className="flex justify-between">
          <span className="font-semibold text-white">Docente:</span> <p>{course.docentes}</p>
        </p>
        <p className="flex justify-between">
          <span className="font-semibold text-white">Quórum:</span> <p>{course.quorum}%</p>
        </p>
      </div>
    </div>
  );
}
