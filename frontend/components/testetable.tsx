"use client";

import * as React from "react";
import {
  ColumnDef,
  ColumnFiltersState,
  SortingState,
  VisibilityState,
  flexRender,
  getCoreRowModel,
  getFilteredRowModel,
  getPaginationRowModel,
  getSortedRowModel,
  useReactTable,
} from "@tanstack/react-table";
import {
  ArrowUpDown,
  ChevronDown,
  MoreHorizontal,
  CheckCircle,
  XCircle,
  X,
} from "lucide-react";

import { Button } from "@/components/ui/button";
import { Checkbox } from "@/components/ui/checkbox";
import {
  DropdownMenu,
  DropdownMenuCheckboxItem,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { Input } from "@/components/ui/input";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";

const data: Payment[] = [
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


export type Payment = {
  id: string;
  cursos: string;
  turmas: string;
  docentes: string;
  turno: "M" | "T" | "N";
  matriculas: string;
  quorum: number;
  cargaHoraria: string;
  diaSemana: string;
  dataInicio: string;
  dataFim: string;
};

export const columns: ColumnDef<Payment>[] = [
  {
    accessorKey: "cursos",
    header: "Curso",
    cell: ({ row }) => (
      <div className="font-semibold truncate">{row.getValue("cursos")}</div>
    ),
  },
  {
    accessorKey: "turmas",
    header: "Turma",
    cell: ({ row }) => <div className="truncate">{row.getValue("turmas")}</div>,
  },
  {
    accessorKey: "docentes",
    header: "Docente",
    cell: ({ row }) => (
      <div className="truncate">{row.getValue("docentes")}</div>
    ),
  },
  {
    accessorKey: "turno",
    header: "Turno",
    cell: ({ row }) => (
      <div className="text-center uppercase">{row.getValue("turno")}</div>
    ),
  },
  {
    accessorKey: "matriculas",
    header: "Matrículas",
    cell: ({ row }) => (
      <div className="text-center">{row.getValue("matriculas")}</div>
    ),
  },
  {
    accessorKey: "quorum",
    header: "Quórum",
    cell: ({ row }) => {
      const quorum = row.getValue("quorum");
      return (
        <div className="flex items-center justify-center space-x-2">
          <span>{quorum}%</span>
          {quorum >= 50 ? (
            <CheckCircle className="text-green-500" size={20} />
          ) : (
            <XCircle className="text-gray-500" size={20} />
          )}
        </div>
      );
    },
  },
];

export function DataTableDemo({ onCourseSelect }) {
  const [sorting, setSorting] = React.useState<SortingState>([]);
  const [columnFilters, setColumnFilters] = React.useState<ColumnFiltersState>(
    []
  );
  const [columnVisibility, setColumnVisibility] =
    React.useState<VisibilityState>({});
  const [rowSelection, setRowSelection] = React.useState({});

  const handleRowClick = (row: Payment) => {
    if (onCourseSelect) {
      onCourseSelect(row);
    }
  };

  const table = useReactTable({
    data,
    columns,
    onSortingChange: setSorting,
    onColumnFiltersChange: setColumnFilters,
    getCoreRowModel: getCoreRowModel(),
    getPaginationRowModel: getPaginationRowModel(),
    getSortedRowModel: getSortedRowModel(),
    getFilteredRowModel: getFilteredRowModel(),
    onColumnVisibilityChange: setColumnVisibility,
    onRowSelectionChange: setRowSelection,
    state: {
      sorting,
      columnFilters,
      columnVisibility,
      rowSelection,
    },
  });

  return (
      <div className="w-full flex">
        <div className="flex-1">
          <div className="flex items-center py-4">
            <Input
              placeholder="Filtrar turmas..."
              value={
                (table.getColumn("turmas")?.getFilterValue() as string) ?? ""
              }
              onChange={(event) =>
                table.getColumn("turmas")?.setFilterValue(event.target.value)
              }
              className="max-w-sm"
            />
            <DropdownMenu>
              <DropdownMenuTrigger asChild>
                <Button variant="outline" className="ml-auto">
                  Colunas <ChevronDown className="ml-2 h-4 w-4" />
                </Button>
              </DropdownMenuTrigger>
              <DropdownMenuContent align="end">
                {table
                  .getAllColumns()
                  .filter((column) => column.getCanHide())
                  .map((column) => {
                    return (
                      <DropdownMenuCheckboxItem
                        key={column.id}
                        className="capitalize"
                        checked={column.getIsVisible()}
                        onCheckedChange={(value) =>
                          column.toggleVisibility(!!value)
                        }
                      >
                        {column.id}
                      </DropdownMenuCheckboxItem>
                    );
                  })}
              </DropdownMenuContent>
            </DropdownMenu>
          </div>
          <div className="rounded-md border bg-gray-50 p-2">
            <Table>
              <TableHeader className="bg-gray-200">
                {table.getHeaderGroups().map((headerGroup) => (
                  <TableRow key={headerGroup.id}>
                    {headerGroup.headers.map((header) => {
                      return (
                        <TableHead key={header.id} className="px-2 py-4">
                          {header.isPlaceholder
                            ? null
                            : flexRender(
                                header.column.columnDef.header,
                                header.getContext()
                              )}
                        </TableHead>
                      );
                    })}
                  </TableRow>
                ))}
              </TableHeader>
              <TableBody>
                {table.getRowModel().rows?.length ? (
                  table.getRowModel().rows.map((row) => (
                    <TableRow
                      key={row.id}
                      data-state={row.getIsSelected() && "selected"}
                      className="hover:bg-gray-100 cursor-pointer"
                      onClick={() => handleRowClick(row.original)}
                    >
                      {row.getVisibleCells().map((cell) => (
                        <TableCell key={cell.id} className="px-2 py-4">
                          {flexRender(
                            cell.column.columnDef.cell,
                            cell.getContext()
                          )}
                        </TableCell>
                      ))}
                    </TableRow>
                  ))
                ) : (
                  <TableRow>
                    <TableCell
                      colSpan={columns.length}
                      className="h-24 text-center"
                    >
                      Sem resultados.
                    </TableCell>
                  </TableRow>
                )}
              </TableBody>
            </Table>
          </div>
          <div className="flex items-center justify-end space-x-2 py-4">
            <div className="flex-1 text-sm text-muted-foreground">
              {table.getFilteredSelectedRowModel().rows.length} de{" "}
              {table.getFilteredRowModel().rows.length} linha(s) selecionada(s).
            </div>
            <div className="space-x-2">
              <Button
                variant="outline"
                size="sm"
                onClick={() => table.previousPage()}
                disabled={!table.getCanPreviousPage()}
              >
                Anterior
              </Button>
              <Button
                variant="outline"
                size="sm"
                onClick={() => table.nextPage()}
                disabled={!table.getCanNextPage()}
              >
                Próximo
              </Button>
            </div>
          </div>
        </div>
      </div>
  );
}
