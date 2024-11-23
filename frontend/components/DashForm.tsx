import React, { useState } from "react";
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
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectLabel,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { Textarea } from "@/components/ui/textarea";

export default function DashCalendarForm() {
  // Definindo o estado do formulário
  const [title, setTitle] = useState<string>("");
  const [description, setDescription] = useState<string>("");
  const [startDate, setStartDate] = useState<string>("");
  const [endDate, setEndDate] = useState<string>("");
  const [tag, setTag] = useState<string>("");
  const [error, setError] = useState<string>("");

  // Função para enviar o formulário
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    // Validação básica
    if (!title || !startDate || !endDate || !tag) {
      setError("Por favor, preencha todos os campos.");
      return;
    }

    setError("");
    alert("Formulário enviado com sucesso!");
    console.log({ title, description, startDate, endDate, tag });
  };

  return (
    <Dialog>
      {/* Botão para abrir o modal */}
      <DialogTrigger asChild>
        <Button variant="outline" className="w-full">
          Definir Data
        </Button>
      </DialogTrigger>

      <DialogContent className="sm:max-w-[425px]">
        <DialogHeader>
          <DialogTitle>Formulário de Evento</DialogTitle>
          <DialogDescription>
            Preencha os campos para definir as datas do evento ou curso.
          </DialogDescription>
        </DialogHeader>

        {/* Exibe erro, se houver */}
        {error && (
          <div className="bg-red-100 text-red-700 border border-red-300 rounded-lg p-4 mb-4">
            {error}
          </div>
        )}

        <form onSubmit={handleSubmit} className="space-y-6">
          {/* Título */}
          <div className="grid gap-4 py-4">
            <div className="grid grid-cols-4 items-center gap-4">
              <Label htmlFor="title" className="text-right">
                Título
              </Label>
              <Input
                id="title"
                type="text"
                value={title}
                onChange={(e) => setTitle(e.target.value)}
                placeholder="Digite o título do evento"
                className="col-span-3"
              />
            </div>

            {/* Descrição */}
            <div className="grid grid-cols-4 items-center gap-4">
              <Label htmlFor="description" className="text-right">
                Descrição
              </Label>
              <Textarea
                id="description"
                value={description}
                onChange={(e) => setDescription(e.target.value)}
                placeholder="Descreva o evento (opcional)"
                className="col-span-3"
              />
            </div>

            {/* Data de Início */}
            <div className="grid grid-cols-4 items-center gap-4">
              <Label htmlFor="startDate" className="text-right">
                Data de Início
              </Label>
              <Input
                id="startDate"
                type="date"
                value={startDate}
                onChange={(e) => setStartDate(e.target.value)}
                className="col-span-3"
              />
            </div>

            {/* Data de Término */}
            <div className="grid grid-cols-4 items-center gap-4">
              <Label htmlFor="endDate" className="text-right">
                Data de Término
              </Label>
              <Input
                id="endDate"
                type="date"
                value={endDate}
                onChange={(e) => setEndDate(e.target.value)}
                className="col-span-3"
              />
            </div>

            {/* Categoria (Tag) */}
            <div className="grid grid-cols-4 items-center gap-4">
              <Label htmlFor="tag" className="text-right">
                Categoria
              </Label>
              <Select onValueChange={setTag}>
                <SelectTrigger className="w-[277px]">
                  <SelectValue placeholder="Selecione uma categoria" />
                </SelectTrigger>
                <SelectContent>
                  <SelectGroup>
                    <SelectLabel>Categoria</SelectLabel>
                    <SelectItem value="feriado">Feriado</SelectItem>
                    <SelectItem value="emenda">Emenda</SelectItem>
                    <SelectItem value="evento">Evento</SelectItem>
                    <SelectItem value="outros">Outros</SelectItem>
                  </SelectGroup>
                </SelectContent>
              </Select>
            </div>
          </div>

          <DialogFooter>
            <Button type="submit" className="w-full">
              Salvar
            </Button>
          </DialogFooter>
        </form>
      </DialogContent>
    </Dialog>
  );
}
