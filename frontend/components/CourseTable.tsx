import * as React from "react";
import {
  flexRender,
  getCoreRowModel,
  getFilteredRowModel,
  getPaginationRowModel,
  useReactTable,
  ColumnDef,
  ColumnFiltersState,
  VisibilityState,
} from "@tanstack/react-table";
import { Input } from "@/components/ui/input";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import { Button } from "@/components/ui/button";
import {
  DropdownMenu,
  DropdownMenuCheckboxItem,
  DropdownMenuContent,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { CheckCircle, Circle } from "lucide-react";
import { courseData, CoursesType } from "@/mocks/mock";

export const columns: ColumnDef<CoursesType>[] = [
  {
    accessorKey: "nome",
    header: "Nome do Curso",
    cell: ({ row }) => <div>{row.getValue("nome")}</div>,
  },
  {
    accessorKey: "turma",
    header: "Turma",
    cell: ({ row }) => <div>{row.getValue("turma")}</div>,
  },
  {
    accessorKey: "docente",
    header: "Docente",
    cell: ({ row }) => <div>{row.getValue("docente")}</div>,
  },
  {
    accessorKey: "matriculados",
    header: "Matrículas",
    cell: ({ row }) => <div>{row.getValue("matriculados")}</div>,
  },
  {
    accessorKey: "vagas",
    header: "Vagas",
    cell: ({ row }) => <div>{row.getValue("vagas")}</div>,
  },
  {
    accessorKey: "quorum",
    header: "Quorum (%)",
    cell: ({ row }) => {
      const quorum = row.getValue<number>("quorum");
      const students = row.getValue<number>("matriculados");
      const vacancy = row.getValue<number>("vagas");
      const quorumAchieved =
        vacancy > 0 && (students / vacancy) * 100 >= quorum;

      return (
        <Button
          variant="ghost"
          className="flex items-center gap-2"
          onClick={() => {
            if (quorumAchieved) {
              alert("clicado");
            }
          }}
          disabled={!quorumAchieved}
        >
          {quorumAchieved ? (
            <CheckCircle className="text-green-500" />
          ) : (
            <Circle className="text-muted-foreground" />
          )}
          {quorum}%
        </Button>
      );
    },
  },
];

export function CourseTable({
  setSelectedCourse,
}: {
  setSelectedCourse: React.Dispatch<React.SetStateAction<CoursesType | null>>;
}) {
  const [columnFilters, setColumnFilters] = React.useState<ColumnFiltersState>(
    []
  );
  const [columnVisibility, setColumnVisibility] =
    React.useState<VisibilityState>({});

  const table = useReactTable({
    data: courseData,
    columns,
    getCoreRowModel: getCoreRowModel(),
    getFilteredRowModel: getFilteredRowModel(),
    getPaginationRowModel: getPaginationRowModel(),
    onColumnFiltersChange: setColumnFilters,
    onColumnVisibilityChange: setColumnVisibility,
    state: { columnFilters, columnVisibility },
    initialState: { pagination: { pageSize: 7 } },
  });

  return (
    <div className="w-full p-4 h-[500px] flex flex-col">
      {/* Filtro de pesquisa */}
      <div className="flex items-center py-4">
        <Input
          placeholder="Pesquisar cursos..."
          value={(table.getColumn("nome")?.getFilterValue() as string) ?? ""}
          onChange={(event) =>
            table.getColumn("nome")?.setFilterValue(event.target.value)
          }
          className="max-w-sm"
        />
        <DropdownMenu>
          <DropdownMenuTrigger asChild>
            <Button variant="outline" className="ml-auto">
              Colunas
            </Button>
          </DropdownMenuTrigger>
          <DropdownMenuContent align="end">
            {table
              .getAllColumns()
              .filter((column) => column.getCanHide())
              .map((column) => (
                <DropdownMenuCheckboxItem
                  key={column.id}
                  className="capitalize"
                  checked={column.getIsVisible()}
                  onCheckedChange={(value) => column.toggleVisibility(!!value)}
                >
                  {column.id}
                </DropdownMenuCheckboxItem>
              ))}
          </DropdownMenuContent>
        </DropdownMenu>
      </div>

      {/* Tabela */}
      <div className="rounded-md border flex-grow">
        <Table style={{ tableLayout: "fixed" }}>
          <TableHeader>
            {table.getHeaderGroups().map((headerGroup) => (
              <TableRow key={headerGroup.id}>
                {headerGroup.headers.map((header) => (
                  <TableHead key={header.id}>
                    {header.isPlaceholder
                      ? null
                      : flexRender(
                          header.column.columnDef.header,
                          header.getContext()
                        )}
                  </TableHead>
                ))}
              </TableRow>
            ))}
          </TableHeader>
          <TableBody>
            {table.getRowModel().rows?.length ? (
              table.getRowModel().rows.map((row) => (
                <TableRow
                  key={row.id}
                  onClick={() => {
                    const course = row.original as CoursesType;
                    setSelectedCourse(course); // Atualiza o curso selecionado
                  }}
                  className="cursor-pointer hover:bg-gray-100"
                >
                  {row.getVisibleCells().map((cell) => (
                    <TableCell key={cell.id}>
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
                  Nenhum curso encontrado.
                </TableCell>
              </TableRow>
            )}
          </TableBody>
        </Table>
      </div>

      {/* Botões de paginação */}
      <div className="flex items-center justify-end space-x-2 py-4">
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
  );
}
