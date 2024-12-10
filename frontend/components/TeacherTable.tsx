"use client";

import * as React from "react";
import {
  flexRender,
  getCoreRowModel,
  getFilteredRowModel,
  getPaginationRowModel,
  useReactTable,
  ColumnDef,
  ColumnFiltersState,
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
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog";
import {
  fetchTeachers,
  createTeacher,
  updateTeacher,
  deleteTeacher,
} from "@/utils/fetch/instructor";

export type Teacher = {
  id: string;
  name: string;
  source: "user";
};

export function TeacherTable() {
  const [teachers, setTeachers] = React.useState<Teacher[]>([]);
  const [columnFilters, setColumnFilters] = React.useState<ColumnFiltersState>(
    []
  );

  const columns: ColumnDef<Teacher>[] = [
    {
      accessorKey: "name",
      header: "Nome",
      cell: ({ row }) => (
        <div className="first-letter:uppercase">{row.getValue("name")}</div>
      ),
    },
    {
      header: "Ações",
      cell: ({ row }) => {
        const teacher = row.original;
        return (
          <div className="flex space-x-2 justify-end">
            <EditTeacherModal teacher={teacher} onRefresh={loadTeachers} />
            <DeleteTeacherModal teacher={teacher} onRefresh={loadTeachers} />
          </div>
        );
      },
    },
  ];

  const loadTeachers = async () => {
    try {
      const data = await fetchTeachers();
      setTeachers(data);
    } catch (error) {
      console.error("Erro ao carregar professores:", error);
    }
  };

  React.useEffect(() => {
    loadTeachers();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const table = useReactTable({
    data: teachers,
    columns,
    getCoreRowModel: getCoreRowModel(),
    getFilteredRowModel: getFilteredRowModel(),
    getPaginationRowModel: getPaginationRowModel(),
    onColumnFiltersChange: setColumnFilters,
    state: { columnFilters },
    initialState: { pagination: { pageSize: 7 } },
  });

  return (
    <div className="w-full px-4 py-2">
      <div className="flex items-center py-4 justify-between">
        <Input
          placeholder="Pesquisar professores..."
          value={(table.getColumn("name")?.getFilterValue() as string) ?? ""}
          onChange={(event) =>
            table.getColumn("name")?.setFilterValue(event.target.value)
          }
          className="max-w-sm"
        />
        <AddTeacherModal onRefresh={loadTeachers} />
      </div>

      <div className="rounded-md border flex flex-col">
        <Table>
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
                <TableRow key={row.id}>
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
                  Nenhum professor encontrado.
                </TableCell>
              </TableRow>
            )}
          </TableBody>
        </Table>
      </div>

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

function AddTeacherModal({ onRefresh }: { onRefresh: () => void }) {
  const [name, setName] = React.useState("");

  const handleAdd = async () => {
    try {
      await createTeacher({ name: name, source: "user" });
      setName("");
      onRefresh();
    } catch (error) {
      console.error("Erro ao adicionar professor:", error);
    }
  };

  return (
    <Dialog>
      <DialogTrigger asChild>
        <Button variant="default">Adicionar Docente</Button>
      </DialogTrigger>
      <DialogContent>
        <DialogHeader>
          <DialogTitle>Adicionar Docente</DialogTitle>
        </DialogHeader>
        <Input
          placeholder="Nome do professor"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
        <DialogFooter>
          <Button onClick={handleAdd}>Salvar</Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
}

function EditTeacherModal({
  teacher,
  onRefresh,
}: {
  teacher: Teacher;
  onRefresh: () => void;
}) {
  const [name, setName] = React.useState(teacher.name);

  const handleEdit = async () => {
    try {
      await updateTeacher(teacher.id, { name: name, source: "user" });
      onRefresh(); // Atualiza a lista de professores
    } catch (error) {
      console.error("Erro ao atualizar professor:", error);
    }
  };

  return (
    <Dialog>
      <DialogTrigger asChild>
        <Button variant="outline">Editar</Button>
      </DialogTrigger>
      <DialogContent>
        <DialogHeader>
          <DialogTitle>Editar Docente</DialogTitle>
        </DialogHeader>
        <Input
          placeholder="Nome do professor"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
        <DialogFooter>
          <Button onClick={handleEdit}>Salvar</Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
}

function DeleteTeacherModal({
  teacher,
  onRefresh,
}: {
  teacher: Teacher;
  onRefresh: () => void;
}) {
  const handleDelete = async () => {
    try {
      await deleteTeacher(teacher.id);
      onRefresh(); // Atualiza a lista de professores
    } catch (error) {
      console.error("Erro ao deletar professor:", error);
    }
  };

  return (
    <Dialog>
      <DialogTrigger asChild>
        <Button variant="destructive">Excluir</Button>
      </DialogTrigger>
      <DialogContent>
        <DialogHeader>
          <DialogTitle>Confirmar Exclusão</DialogTitle>
          <DialogDescription>
            Tem certeza que deseja excluir {teacher.name}?
          </DialogDescription>
        </DialogHeader>
        <DialogFooter>
          <Button variant="destructive" onClick={handleDelete}>
            Excluir
          </Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
}
