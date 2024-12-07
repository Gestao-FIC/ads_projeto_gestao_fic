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
  id: string;
  nome: string;
  turma: string;
  docente: string;
  turno: "M" | "T" | "N";
  matriculados: number;
  vagas: number;
  quorum: number;
  cargaHoraria: string;
  diaSemana: string[];
  dataInicio: string;
  dataFim: string;
};

export const courseData: CoursesType[] = [
  {
    id: "m5gr84i9",
    nome: "Costureiro de Máquina",
    turma: "CEP.COS.MAQ.N-2",
    docente: "André Cassulino",
    turno: "N",
    matriculados: 33,
    vagas: 40,
    quorum: 40,
    cargaHoraria: "40 horas",
    diaSemana: ["Segunda", "Quarta"],
    dataInicio: "10/11/2024",
    dataFim: "10/12/2024",
  },
  {
    id: "bhqecj4p",
    nome: "Torneiro Mecânico",
    turma: "SA.TOR.MEC.N-2",
    docente: "Luciana Fugita",
    turno: "M",
    matriculados: 34,
    vagas: 40,
    quorum: 60,
    cargaHoraria: "60 horas",
    diaSemana: ["Segunda", "Quarta"],
    dataInicio: "10/10/2024",
    dataFim: "10/12/2024",
  },
  {
    id: "r9n7t1o2",
    nome: "Eletricista Predial",
    turma: "CEP.ELE.PRD.M-1",
    docente: "Carlos Lima",
    turno: "T",
    matriculados: 20,
    vagas: 30,
    quorum: 66,
    cargaHoraria: "50 horas",
    diaSemana: ["Terça", "Quinta"],
    dataInicio: "15/10/2024",
    dataFim: "15/11/2024",
  },
  {
    id: "h4u1z5t3",
    nome: "Auxiliar de Escritório",
    turma: "CEP.AUX.ESCR.T-3",
    docente: "Patrícia Alves",
    turno: "T",
    matriculados: 28,
    vagas: 30,
    quorum: 90,
    cargaHoraria: "35 horas",
    diaSemana: ["Terça", "Sexta"],
    dataInicio: "01/11/2024",
    dataFim: "30/11/2024",
  },
  {
    id: "n3r8v7a4",
    nome: "Programador Web",
    turma: "CEP.PROG.WEB.M-2",
    docente: "João Fernandes",
    turno: "M",
    matriculados: 40,
    vagas: 40,
    quorum: 100,
    cargaHoraria: "80 horas",
    diaSemana: ["Segunda", "Quarta", "Sexta"],
    dataInicio: "01/10/2024",
    dataFim: "31/10/2024",
  },
  {
    id: "k2m3f6p8",
    nome: "Técnico de Enfermagem",
    turma: "SA.TEC.ENF.N-1",
    docente: "Marcelo Rocha",
    turno: "N",
    matriculados: 22,
    vagas: 30,
    quorum: 73,
    cargaHoraria: "120 horas",
    diaSemana: ["Segunda", "Sexta"],
    dataInicio: "05/10/2024",
    dataFim: "05/12/2024",
  },
  {
    id: "g9h2b7r5",
    nome: "Operador de Máquinas Pesadas",
    turma: "CEP.OP.MAQ.T-1",
    docente: "Ricardo Lima",
    turno: "T",
    matriculados: 12,
    vagas: 20,
    quorum: 60,
    cargaHoraria: "100 horas",
    diaSemana: ["Segunda", "Quinta"],
    dataInicio: "20/09/2024",
    dataFim: "20/12/2024",
  },
  {
    id: "w3e1x9c7",
    nome: "Assistente Administrativo",
    turma: "CEP.ASS.ADM.N-1",
    docente: "Marta Souza",
    turno: "M",
    matriculados: 25,
    vagas: 30,
    quorum: 83,
    cargaHoraria: "40 horas",
    diaSemana: ["Segunda", "Quarta", "Sexta"],
    dataInicio: "15/10/2024",
    dataFim: "15/11/2024",
  },
  {
    id: "t5l1r9i6",
    nome: "Padeiro",
    turma: "CEP.PAD.N-2",
    docente: "Ricardo Melo",
    turno: "T",
    matriculados: 17,
    vagas: 25,
    quorum: 68,
    cargaHoraria: "30 horas",
    diaSemana: ["Terça", "Quinta"],
    dataInicio: "01/11/2024",
    dataFim: "01/12/2024",
  },
  {
    id: "a7d4h2b8",
    nome: "Fotógrafo Profissional",
    turma: "CEP.FOT.M-1",
    docente: "Felipe Costa",
    turno: "M",
    matriculados: 18,
    vagas: 20,
    quorum: 90,
    cargaHoraria: "60 horas",
    diaSemana: ["Segunda", "Sexta"],
    dataInicio: "20/10/2024",
    dataFim: "20/12/2024",
  },
  {
    id: "z9g2u5d3",
    nome: "Designer Gráfico",
    turma: "CEP.DES.M-1",
    docente: "Roberta Tavares",
    turno: "M",
    matriculados: 26,
    vagas: 30,
    quorum: 87,
    cargaHoraria: "40 horas",
    diaSemana: ["Segunda", "Quarta"],
    dataInicio: "05/10/2024",
    dataFim: "05/11/2024",
  },
  {
    id: "j4q3v6o9",
    nome: "Gerente de Projetos",
    turma: "SA.GER.PRJ.T-2",
    docente: "Renata Goulart",
    turno: "T",
    matriculados: 19,
    vagas: 25,
    quorum: 76,
    cargaHoraria: "100 horas",
    diaSemana: ["Terça", "Quinta"],
    dataInicio: "01/11/2024",
    dataFim: "01/12/2024",
  },
  {
    id: "c8s9k4y1",
    nome: "Mestre Cervejeiro",
    turma: "CEP.MEC.CER.M-1",
    docente: "Lucas Almeida",
    turno: "M",
    matriculados: 23,
    vagas: 30,
    quorum: 77,
    cargaHoraria: "60 horas",
    diaSemana: ["Segunda", "Sexta"],
    dataInicio: "15/10/2024",
    dataFim: "15/11/2024",
  },
  {
    id: "d7u6t5p2",
    nome: "Chef de Cozinha",
    turma: "CEP.CHE.CZ.N-2",
    docente: "Gabriela Moraes",
    turno: "N",
    matriculados: 35,
    vagas: 40,
    quorum: 88,
    cargaHoraria: "80 horas",
    diaSemana: ["Segunda", "Quarta", "Sexta"],
    dataInicio: "01/10/2024",
    dataFim: "01/12/2024",
  },
  {
    id: "v9j5w8k3",
    nome: "Técnico em Segurança do Trabalho",
    turma: "CEP.TEC.SEC.M-1",
    docente: "Fernando Santos",
    turno: "M",
    matriculados: 30,
    vagas: 40,
    quorum: 75,
    cargaHoraria: "90 horas",
    diaSemana: ["Segunda", "Terça", "Sexta"],
    dataInicio: "20/09/2024",
    dataFim: "20/11/2024",
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
