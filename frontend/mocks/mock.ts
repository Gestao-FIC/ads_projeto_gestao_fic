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

export type CoursesType = {
  code: string;
  course?: string;
  shift?: string;
  duration: number;
  modality?: string;
  attendance?: number;
  period_from?: number;
  period_to?: number;
  start_time?: string;
  end_time?: string;
  estimated_enrollments?: string;
  actual_enrollments?: string;
  quorum?: number;
  status?: string;
  income?: string;
  teacher?: string;
};

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
