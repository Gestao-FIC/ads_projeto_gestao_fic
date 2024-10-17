"use client";

import Link from "next/link";
import { useState } from "react";
import { PiBook, PiCalendar, PiClock, PiUser } from "react-icons/pi";

const courseDetails = {
  turno: "Noturno",
  cargaHoraria: "40 horas",
  diaSemana: "Segunda e Quarta",
  dataInicio: "10/11/2024",
  dataFim: "10/12/2024",
  docente: "Prof. João Silva",
};

const CourseSidebar = () => {
  const [activePath, setActivePath] = useState("/cursos");

  const handleLinkClick = (path: string) => {
    setActivePath(path);
  };

  return (
    <div className="bg-primary w-52 flex flex-col">
      <div className="p-4 flex flex-col justify-center items-center gap-2">
        <p className="text-secondary font-bold">Detalhes do Curso</p>
      </div>
      <div className="flex-1 py-10 flex flex-col text-secondary gap-4 px-4">
        <div className="flex flex-row items-center gap-2">
          <PiClock size={24} color="white" />
          <p className="text-lg">Turno: {courseDetails.turno}</p>
        </div>
        <div className="flex flex-row items-center gap-2">
          <PiClock size={24} color="white" />
          <p className="text-lg">Carga Horária: {courseDetails.cargaHoraria}</p>
        </div>
        <div className="flex flex-row items-center gap-2">
          <PiCalendar size={24} color="white" />
          <p className="text-lg">Dia da Semana: {courseDetails.diaSemana}</p>
        </div>
        <div className="flex flex-row items-center gap-2">
          <PiCalendar size={24} color="white" />
          <p className="text-lg">Data de Início: {courseDetails.dataInicio}</p>
        </div>
        <div className="flex flex-row items-center gap-2">
          <PiCalendar size={24} color="white" />
          <p className="text-lg">Data de Fim: {courseDetails.dataFim}</p>
        </div>
        <div className="flex flex-row items-center gap-2">
          <PiUser size={24} color="white" />
          <p className="text-lg">Docente: {courseDetails.docente}</p>
        </div>
      </div>
      <div className="p-4">
        <Link
          href="/cursos"
          className={`text-muted-foreground hover:text-muted transition-all ease-in-out font-medium ${
            activePath === "/cursos" ? "text-primary" : "text-secondary"
          }`}
          onClick={() => handleLinkClick("/cursos")}
        >
          Voltar para Cursos
        </Link>
      </div>
    </div>
  );
};

export default CourseSidebar;
