import { DataTableDemo } from "@/components/testetable";
import React from "react";
import CourseSidebar from "@/components/CourseSidebar"; // Assumindo que o componente da barra lateral foi criado

export default function Cursos() {
  return (
    <div className="flex h-full w-full">
      {/* Conteúdo da tabela à esquerda */}
      <div className="flex-1 text-center content-center bg-secondary p-4">
        <DataTableDemo />
      </div>

      {/* Barra lateral à direita */}
      <CourseSidebar />
    </div>
  );
}
