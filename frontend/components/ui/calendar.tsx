import * as React from "react";
import { ChevronLeft, ChevronRight } from "lucide-react";
import { DayPicker } from "react-day-picker";
import { cn } from "@/lib/utils";
import { buttonVariants } from "@/components/ui/button";

export type CalendarProps = React.ComponentProps<typeof DayPicker>;

function Calendar({
  className,
  classNames,
  showOutsideDays = true,
  ...props
}: CalendarProps) {
  return (
    <DayPicker
      showOutsideDays={showOutsideDays}
      className={cn("p-3 bg-primary-foreground", className)}
      classNames={{
        months: "space-y-4",
        month: "space-y-4",
        caption: "flex justify-center pt-1 relative items-center",
        caption_label: "text-xl font-medium text-primary",
        nav: "space-x-1 flex items-center",
        nav_button: cn(
          buttonVariants({ variant: "outline" }),
          "h-12 w-12 bg-transparent p-0 opacity-50 hover:opacity-100 text-primary"
        ),
        nav_button_previous: "absolute left-1",
        nav_button_next: "absolute right-1",
        table: "w-full border-collapse space-y-1",
        head_row: "flex",
        head_cell: "text-foreground rounded-md w-16 font-normal text-lg",
        row: "flex w-full mt-2",
        cell: "h-16 w-16 text-center text-lg p-0 relative",
        day: cn(
          buttonVariants({ variant: "ghost" }),
          "h-16 w-16 p-0 font-normal aria-selected:opacity-100 text-foreground text-lg"
        ),
        day_selected: "bg-primary/10 text-accent-foreground",
        day_today: "bg-primary/5 text-secondary-foreground",
        day_outside: "day-outside text-muted-foreground opacity-50",
        day_disabled: "text-muted-foreground opacity-50",
        day_hidden: "invisible",
        ...classNames,
      }}
      components={{
        IconLeft: () => <ChevronLeft className="h-5 w-5 text-foreground" />,
        IconRight: () => <ChevronRight className="h-5 w-5 text-foreground" />,
      }}
      {...props}
    />
  );
}
Calendar.displayName = "Calendar";

export { Calendar };
