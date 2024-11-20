export const teacherData = [
  {
    nome: "Ana Silva",
    horas: 20,
  },
  {
    nome: "Carlos Santos",
    horas: 15,
  },
  {
    nome: "Maria Oliveira",
    horas: 25,
  },
  {
    nome: "João Pereira",
    horas: 18,
  },
  {
    nome: "Fernanda Lima",
    horas: 22,
  },
  {
    nome: "Lucas Almeida",
    horas: 10,
  },
  {
    nome: "Paula Costa",
    horas: 30,
  },
  {
    nome: "Roberto Ferreira",
    horas: 12,
  },
  {
    nome: "Renata Gomes",
    horas: 14,
  },
  {
    nome: "Felipe Rocha",
    horas: 16,
  },
  {
    nome: "Juliana Martins",
    horas: 19,
  },
  {
    nome: "André Souza",
    horas: 17,
  },
  {
    nome: "Mariana Costa",
    horas: 23,
  },
  {
    nome: "Ricardo Lima",
    horas: 27,
  },
  {
    nome: "Tatiane Ribeiro",
    horas: 11,
  },
  {
    nome: "Thiago Almeida",
    horas: 24,
  },
  {
    nome: "Sofia Lima",
    horas: 13,
  },
  {
    nome: "Eduardo Martins",
    horas: 29,
  },
  {
    nome: "Larissa Mendes",
    horas: 15,
  },
  {
    nome: "Gustavo Rocha",
    horas: 21,
  },
];

export const gaugeData = [
  {
    value: 37,
    total: 124,
    colorOption: "red" as "red" | "blue" | "green",
    type: "Cursos",
  },
  {
    value: 75,
    total: 100,
    colorOption: "blue" as "red" | "blue" | "green",
    type: "Financeiro",
  },
  {
    value: 50,
    total: 80,
    colorOption: "green" as "red" | "blue" | "green",
    type: "Matrículas",
  },
];

type EventType = "holiday" | "vacation" | "blockage";

interface CalendarEvent {
  date: Date;
  type: EventType;
}

export const events: CalendarEvent[] = [
  { date: new Date(2024, 0, 1), type: "holiday" },
  { date: new Date(2024, 0, 15), type: "vacation" },
  { date: new Date(2024, 0, 31), type: "blockage" },
  { date: new Date(2024, 1, 10), type: "holiday" },
  { date: new Date(2024, 1, 20), type: "vacation" },
  { date: new Date(2024, 1, 28), type: "blockage" },
  { date: new Date(2024, 2, 5), type: "holiday" },
  { date: new Date(2024, 2, 15), type: "vacation" },
  { date: new Date(2024, 2, 25), type: "blockage" },
];

export type Payment = {
  id: string;
  cursos: string;
  turmas: string;
  docentes: string;
  turno: "M" | "T" | "N";
  matriculas: string;
  quorum: number;
  cargaHoraria: string;
  diaSemana: string[];
  dataInicio: string;
  dataFim: string;
};

export const data: Payment[] = [
  {
    id: "m5gr84i9",
    cursos: "Costureiro de Máquina",
    turmas: "CEP.COS.MAQ.N-2",
    docentes: "André Cassulino",
    turno: "N",
    matriculas: "19/40",
    quorum: 40,
    cargaHoraria: "40 horas",
    diaSemana: ["Segunda", "Quarta"],
    dataInicio: "10/11/2024",
    dataFim: "10/12/2024",
  },
  {
    id: "3u1reuv4",
    cursos: "Eletricista Instalador",
    turmas: "CEP.EL.INS.N-1",
    docentes: "Gabriel Claro",
    turno: "T",
    matriculas: "22/40",
    quorum: 60,
    cargaHoraria: "50 horas",
    diaSemana: ["Terça", "Quinta"],
    dataInicio: "08/08/2024",
    dataFim: "09/10/2024",
  },
  {
    id: "derv1ws0",
    cursos: "Aperfeiçoamento Profissional",
    turmas: "SA.LIDTM.I-3",
    docentes: "Luciana Fugita",
    turno: "N",
    matriculas: "30/40",
    quorum: 80,
    cargaHoraria: "30 horas",
    diaSemana: ["Segunda", "Sexta"],
    dataInicio: "15/09/2024",
    dataFim: "15/10/2024",
  },
  {
    id: "derv1ws0",
    cursos: "Aperfeiçoamento Profissional",
    turmas: "SA.LIDTM.I-3",
    docentes: "Luciana Fugita",
    turno: "N",
    matriculas: "30/40",
    quorum: 80,
    cargaHoraria: "30 horas",
    diaSemana: ["Segunda", "Sexta"],
    dataInicio: "15/09/2024",
    dataFim: "15/10/2024",
  },
  {
    id: "derv1ws0",
    cursos: "Aperfeiçoamento Profissional",
    turmas: "SA.LIDTM.I-3",
    docentes: "Luciana Fugita",
    turno: "N",
    matriculas: "30/40",
    quorum: 80,
    cargaHoraria: "30 horas",
    diaSemana: ["Segunda", "Sexta"],
    dataInicio: "15/09/2024",
    dataFim: "15/10/2024",
  },
  {
    id: "derv1ws0",
    cursos: "Aperfeiçoamento Profissional",
    turmas: "SA.LIDTM.I-3",
    docentes: "Luciana Fugita",
    turno: "N",
    matriculas: "30/40",
    quorum: 80,
    cargaHoraria: "30 horas",
    diaSemana: ["Segunda", "Sexta"],
    dataInicio: "15/09/2024",
    dataFim: "15/10/2024",
  },
  {
    id: "derv1ws0",
    cursos: "Aperfeiçoamento Profissional",
    turmas: "SA.LIDTM.I-3",
    docentes: "Luciana Fugita",
    turno: "N",
    matriculas: "30/40",
    quorum: 80,
    cargaHoraria: "30 horas",
    diaSemana: ["Segunda", "Sexta"],
    dataInicio: "15/09/2024",
    dataFim: "15/10/2024",
  },
  {
    id: "derv1ws0",
    cursos: "Aperfeiçoamento Profissional",
    turmas: "SA.LIDTM.I-3",
    docentes: "Luciana Fugita",
    turno: "N",
    matriculas: "30/40",
    quorum: 80,
    cargaHoraria: "30 horas",
    diaSemana: ["Segunda", "Sexta"],
    dataInicio: "15/09/2024",
    dataFim: "15/10/2024",
  },
  {
    id: "derv1ws0",
    cursos: "Aperfeiçoamento Profissional",
    turmas: "SA.LIDTM.I-3",
    docentes: "Luciana Fugita",
    turno: "N",
    matriculas: "30/40",
    quorum: 80,
    cargaHoraria: "30 horas",
    diaSemana: ["Segunda", "Sexta"],
    dataInicio: "15/09/2024",
    dataFim: "15/10/2024",
  },
  {
    id: "derv1ws0",
    cursos: "Aperfeiçoamento Profissional",
    turmas: "SA.LIDTM.I-3",
    docentes: "Luciana Fugita",
    turno: "N",
    matriculas: "30/40",
    quorum: 80,
    cargaHoraria: "30 horas",
    diaSemana: ["Segunda", "Sexta"],
    dataInicio: "15/09/2024",
    dataFim: "15/10/2024",
  },
  {
    id: "derv1ws0",
    cursos: "Aperfeiçoamento Profissional",
    turmas: "SA.LIDTM.I-3",
    docentes: "Luciana Fugita",
    turno: "N",
    matriculas: "30/40",
    quorum: 80,
    cargaHoraria: "30 horas",
    diaSemana: ["Segunda", "Sexta"],
    dataInicio: "15/09/2024",
    dataFim: "15/10/2024",
  },
  {
    id: "derv1ws0",
    cursos: "Aperfeiçoamento Profissional",
    turmas: "SA.LIDTM.I-3",
    docentes: "Luciana Fugita",
    turno: "N",
    matriculas: "30/40",
    quorum: 80,
    cargaHoraria: "30 horas",
    diaSemana: ["Segunda", "Sexta"],
    dataInicio: "15/09/2024",
    dataFim: "15/10/2024",
  },
  {
    id: "5kma53ae",
    cursos: "Pacote Office",
    turmas: "ARA.OFFICE.N-1",
    docentes: "Robson Shimit",
    turno: "T",
    matriculas: "18/40",
    quorum: 40,
    cargaHoraria: "20 horas",
    diaSemana: ["Quarta", "Sexta"],
    dataInicio: "01/07/2024",
    dataFim: "30/08/2024",
  },
  {
    id: "bhqecj4p",
    cursos: "Torneiro Mecânico",
    turmas: "SA.TOR.MEC.N-2",
    docentes: "Luciana Fugita",
    turno: "M",
    matriculas: "33/40",
    quorum: 60,
    cargaHoraria: "60 horas",
    diaSemana: ["Segunda", "Quarta"],
    dataInicio: "10/10/2024",
    dataFim: "10/12/2024",
  },
];

export const diasSemana = [
  "Domingo",
  "Segunda",
  "Terça",
  "Quarta",
  "Quinta",
  "Sexta",
  "Sábado",
];

export const iniciaisDias = ["D", "S", "T", "Q", "Q", "S", "S"];

export const courseDetails = {
  turno: "Noturno",
  cargaHoraria: "40 horas",
  diaSemana: "Segunda e Quarta",
  dataInicio: "10/11/2024",
  dataFim: "10/12/2024",
  docente: "Prof. João Silva",
  quorum: "40",
};
