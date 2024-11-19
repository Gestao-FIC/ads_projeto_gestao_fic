"use client"

import * as React from "react"
import { useState } from "react"
import { Input } from "@/components/ui/input"
import { Button } from "@/components/ui/button"

// Define o tipo para a lista de pessoas
type Person = {
  name: string
}

// Dados estáticos da lista de pessoas
const data: Person[] = [
  { name: "ANDRÉ CASSULINO" },
  { name: "CAINÃ ANTUNES" },
  { name: "GABRIEL CLARO" },
  { name: "ROBSON SHIMIT" },
  { name: "EDILSON SOUZA" },
  { name: "EDINALDO SANTOS" },
  { name: "CARLOS AUGUSTO" },
  { name: "LUCIANA FUGITA" },
  { name: "ALEXANDRE ANDRADE" },
  { name: "ALESSANDRO OLIVEIRA" },
  { name: "ANA PAULA GOES" },
  { name: "RAFAEL MARTINS" },
]

// Função para ordenar a lista de pessoas em ordem alfabética
function sortDataAsc(data: Person[]): Person[] {
  return [...data].sort((a, b) => a.name.localeCompare(b.name))
}

// Função para ordenar a lista de pessoas em ordem decrescente
function sortDataDesc(data: Person[]): Person[] {
  return [...data].sort((a, b) => b.name.localeCompare(a.name))
}

// Função para resetar o campo de pesquisa
function resetSearch(setSearchTerm: React.Dispatch<React.SetStateAction<string>>): void {
  setSearchTerm("")
  console.log("Search term reset.")
}

// Componente principal da tabela de docentes
export function DocentesTable() {
  const [searchTerm, setSearchTerm] = useState<string>("")
  const [isSortedAsc, setIsSortedAsc] = useState<boolean>(true)

  // Filtra os dados de acordo com o termo de pesquisa inserido
  const filteredData = data.filter((person) => {
    const match = person.name.toLowerCase().includes(searchTerm.toLowerCase())
    console.log(`Filtering: ${person.name}, Match: ${match}`) // Log para verificar cada pessoa sendo filtrada
    return match
  })

  // Ordena os dados filtrados conforme o estado de ordenação
  const sortedData = isSortedAsc ? sortDataAsc(filteredData) : sortDataDesc(filteredData)

  console.log(`Search Term: ${searchTerm}`) // Log para acompanhar o termo de pesquisa
  console.log(`Filtered Data:`, sortedData) // Log para acompanhar os dados filtrados

  return (
    <div className="w-full max-w-2xl mx-auto p-8 bg-gradient-to-r from-white via-gray-100 to-white backdrop-blur-lg rounded-2xl shadow-2xl border border-gray-300">
      {/* Campo de pesquisa para filtrar os docentes */}
      <div className="flex items-center mb-8 bg-white/90 rounded-full shadow-md overflow-hidden">
        <Input
          placeholder="Pesquisar docente..."
          value={searchTerm}
          onChange={(e) => {
            console.log(`Input Changed: ${e.target.value}`) // Log para acompanhar mudanças no input
            setSearchTerm(e.target.value)
          }}
          className="flex-grow h-14 px-6 border-none focus:ring-0 bg-transparent placeholder-gray-500 text-gray-900"
        />
        {/* Botão de pesquisa com ícone de lupa */}
        <Button className="h-14 w-14 bg-gradient-to-r from-blue-500 to-indigo-500 text-white flex items-center justify-center hover:opacity-80 transition-opacity rounded-full">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            className="h-6 w-6"
            viewBox="0 0 20 20"
            fill="currentColor"
          >
            <path
              fillRule="evenodd"
              d="M12.9 14.32a8 8 0 111.414-1.415l4.387 4.387-1.414 1.414-4.387-4.387zM8 14a6 6 0 100-12 6 6 0 000 12z"
              clipRule="evenodd"
            />
          </svg>
        </Button>
        {/* Botão para resetar o campo de pesquisa */}
        <Button
          onClick={() => resetSearch(setSearchTerm)}
          className="h-14 w-14 ml-2 bg-red-500 text-white flex items-center justify-center hover:opacity-80 transition-opacity rounded-full"
        >
          Reset
        </Button>
      </div>
      {/* Botão para alternar a ordenação da lista */}
      <div className="flex justify-end mb-4">
        <Button
          onClick={() => setIsSortedAsc(!isSortedAsc)}
          className="bg-gray-800 text-white px-4 py-2 rounded-lg hover:bg-gray-700 transition-colors"
        >
          {isSortedAsc ? "Ordenar Decrescente" : "Ordenar Crescente"}
        </Button>
      </div>
      {/* Lista de docentes filtrados com rolagem */}
      <div className="rounded-lg bg-white shadow-xl border border-gray-300 max-h-96 overflow-y-auto">
        <ul className="divide-y divide-gray-200">
          {sortedData.length > 0 ? (
            sortedData.map((person, index) => (
              <li
                key={index}
                className="cursor-pointer p-4 bg-gradient-to-r from-gray-50 via-white to-gray-50 hover:bg-blue-100 text-gray-900 rounded-lg shadow-sm transition-transform transform hover:scale-105 duration-300 ease-in-out flex justify-center items-center font-semibold"
              >
                {person.name}
              </li>
            ))
          ) : (
            // Mensagem exibida quando nenhum resultado é encontrado
            <li className="p-4 text-center text-gray-500 font-medium">
              Nenhum resultado encontrado.
            </li>
          )}
        </ul>
      </div>
    </div>
  )
}
