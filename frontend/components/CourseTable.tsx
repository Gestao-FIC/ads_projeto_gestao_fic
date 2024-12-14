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
import { CoursesType } from "@/mocks/mock";
import { fetchCourseClasses } from "@/utils/fetch/class";

export const columns: ColumnDef<CoursesType>[] = [
  {
    accessorKey: "course",
    header: "Nome do Curso",
    cell: ({ row }) => <div>{row.getValue("course")}</div>,
  },
  {
    accessorKey: "code",
    header: "Turma",
    cell: ({ row }) => <div>{row.getValue("code")}</div>,
  },
  {
    accessorKey: "teacher",
    header: "Docente",
    cell: ({ row }) => <div>{row.getValue("teacher")}</div>,
  },
  {
    accessorKey: "actual_enrollments",
    header: "Matrículas",
    cell: ({ row }) => <div>{row.getValue("actual_enrollments")}</div>,
  },
  {
    accessorKey: "estimated_enrollments",
    header: "Vagas",
    cell: ({ row }) => <div>{row.getValue("estimated_enrollments")}</div>,
  },
  {
    accessorKey: "quorum",
    header: "Quorum",
    cell: ({ row }) => <div>{row.getValue("estimated_enrollments")}</div>,
  },
  {
    accessorKey: "quorum",
    header: "Quorum",
    cell: ({ row }) => {
      const quorum = row.getValue<number>("quorum");
      const students = row.getValue<number>("actual_enrollments");

      const quorumAchieved = quorum && students >= quorum;

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
          {quorum}
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
  const [courseData, setCourseData] = React.useState<CoursesType[]>([]);
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

  const loadCoursesClasses = async () => {
    try {
      const data = await fetchCourseClasses();
      setCourseData(data);
    } catch (error) {
      console.error("Erro ao carregar turmas:", error);
    }
  };

  React.useEffect(() => {
    loadCoursesClasses();
  }, []);

  return (
    <div className="w-full p-4 h-[500px] flex flex-col">
      {/* Filtro de pesquisa */}
      <div className="flex items-center py-4">
        <Input
          placeholder="Pesquisar cursos..."
          value={(table.getColumn("course")?.getFilterValue() as string) ?? ""}
          onChange={(event) =>
            table.getColumn("course")?.setFilterValue(event.target.value)
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
