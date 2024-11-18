"use client";

import { Bar, BarChart, CartesianGrid, XAxis, YAxis } from "recharts";

import {
  ChartConfig,
  ChartContainer,
  ChartTooltip,
  ChartTooltipContent,
} from "@/components/ui/chart";

import { teacherData } from "@/lib/mock";

const chartData = teacherData;

const chartConfig = {
  barColor: {
    label: "Horas",
    color: "#60a5fa",
  },
} satisfies ChartConfig;

export function ChartComponent() {
  return (
    <ChartContainer config={chartConfig} className="min-h-[200px] w-full">
      <BarChart accessibilityLayer data={chartData}>
        <CartesianGrid vertical={false} />
        <XAxis
          dataKey="nome"
          tickLine={false}
          tickMargin={10}
          axisLine={true}
          tickFormatter={(value) => value.slice(0, 3)}
        />

        <YAxis
          dataKey="horas"
          tickLine={false}
          axisLine={true}
          tickMargin={5}
        />
        <ChartTooltip content={<ChartTooltipContent />} />
        <Bar dataKey="horas" fill="var(--color-barColor)" radius={4} />
      </BarChart>
    </ChartContainer>
  );
}
