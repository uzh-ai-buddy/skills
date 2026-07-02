:::artifact{identifier="weekly-timetable-grid" type="application/vnd.react" title="Weekly Timetable (Calendar Grid)"}
```react
import React, { useMemo } from "react";
import { Alert, AlertDescription, AlertTitle } from "./components/ui/alert";
import { Badge } from "./components/ui/badge";
import { Card, CardContent, CardHeader, CardTitle } from "./components/ui/card";
import { Separator } from "./components/ui/separator";
import { AlertTriangle } from "lucide-react";

const startHour = 8;
const endHour = 20;
const rowHeight = 44;

const categoryColors = {
  Lecture: "#bfdbfe",
  Work: "#fde68a",
  Tutorial: "#bbf7d0",
};

const events = [
  {
    id: "math-1",
    day: "Mon",
    start: "08:15",
    end: "10:00",
    label: "Mathematik I",
    location: "KOH-B-10",
    category: "Lecture",
  },
  {
    id: "micro-eco",
    day: "Mon",
    start: "09:00",
    end: "11:45",
    label: "Mikrooekonomie",
    location: "KOH-B-10",
    category: "Lecture",
  },
  {
    id: "job",
    day: "Wed",
    start: "17:00",
    end: "20:00",
    label: "Werkstudentenjob",
    category: "Work",
  },
  {
    id: "poc",
    day: "Thu",
    start: "14:00",
    end: "17:00",
    label: "People-Oriented Computing",
    location: "BIN-1-E.01",
    category: "Lecture",
  },
];

const days = ["Mon", "Tue", "Wed", "Thu", "Fri"];

const toMinutes = (time) => {
  const [hours, minutes] = time.split(":").map(Number);
  return hours * 60 + minutes;
};

const hasOverlap = (first, second) =>
  toMinutes(first.start) < toMinutes(second.end) &&
  toMinutes(second.start) < toMinutes(first.end);

export default function WeeklyTimetableGrid() {
  const { grouped, conflicts } = useMemo(() => {
    const groupedEvents = events.reduce((acc, event) => {
      acc[event.day] = [...(acc[event.day] ?? []), event];
      return acc;
    }, {});

    const conflictSet = new Set();
    const conflictMessages = [];

    Object.entries(groupedEvents).forEach(([day, dayEvents]) => {
      const sorted = [...dayEvents].sort(
        (a, b) => toMinutes(a.start) - toMinutes(b.start)
      );
      for (let i = 0; i < sorted.length; i += 1) {
        for (let j = i + 1; j < sorted.length; j += 1) {
          const first = sorted[i];
          const second = sorted[j];
          if (hasOverlap(first, second)) {
            conflictSet.add(first.id);
            conflictSet.add(second.id);
            conflictMessages.push(
              `${day}: ${first.label} (${first.start}-${first.end}) overlaps ${second.label} (${second.start}-${second.end})`
            );
          }
        }
      }
    });

    return {
      grouped: groupedEvents,
      conflicts: { ids: conflictSet, messages: conflictMessages },
    };
  }, []);

  const timeLabels = Array.from(
    { length: endHour - startHour },
    (_, index) => startHour + index
  );

  return (
    <div className="p-6 font-sans space-y-6">
      <Card>
        <CardHeader>
          <CardTitle>Weekly Timetable</CardTitle>
          <div className="flex flex-wrap gap-2 text-sm text-slate-600">
            <Badge className="bg-blue-100 text-blue-900">Lecture</Badge>
            <Badge className="bg-yellow-200 text-yellow-900">Work</Badge>
            <Badge className="bg-emerald-100 text-emerald-900">Tutorial</Badge>
            <Badge className="bg-red-100 text-red-700">Conflict</Badge>
          </div>
        </CardHeader>
        <CardContent>
          <div className="grid grid-cols-[72px_repeat(5,minmax(0,1fr))] gap-3">
            <div className="flex flex-col text-xs text-slate-500">
              {timeLabels.map((hour) => (
                <div
                  key={hour}
                  className="flex items-start justify-end pr-2"
                  style={{ height: rowHeight }}
                >
                  {hour}:00
                </div>
              ))}
            </div>

            {days.map((day) => (
              <div key={day} className="space-y-2">
                <p className="text-sm font-semibold text-slate-700">{day}</p>
                <div
                  className="relative border rounded-lg bg-slate-50"
                  style={{ height: rowHeight * (endHour - startHour) }}
                >
                  {grouped[day]?.map((event) => {
                    const offset = (toMinutes(event.start) - startHour * 60) / 60;
                    const duration =
                      (toMinutes(event.end) - toMinutes(event.start)) / 60;
                    const isConflict = conflicts.ids.has(event.id);
                    const color =
                      categoryColors[event.category] ?? categoryColors.Lecture;

                    return (
                      <div
                        key={event.id}
                        className="absolute left-2 right-2 rounded-md border px-2 py-1 text-xs"
                        style={{
                          top: offset * rowHeight,
                          height: Math.max(duration * rowHeight, 28),
                          backgroundColor: color,
                          borderColor: isConflict ? "#ef4444" : "#e2e8f0",
                        }}
                      >
                        <div className="font-semibold text-slate-900">
                          {event.start}–{event.end}
                        </div>
                        <div className="text-slate-700">{event.label}</div>
                        {event.location ? (
                          <div className="text-[11px] text-slate-500">
                            {event.location}
                          </div>
                        ) : null}
                        {isConflict ? (
                          <div className="mt-1">
                            <Badge className="bg-red-100 text-red-700">
                              Conflict
                            </Badge>
                          </div>
                        ) : null}
                      </div>
                    );
                  })}
                </div>
              </div>
            ))}
          </div>
        </CardContent>
      </Card>

      <Separator />

      <Alert>
        <AlertTriangle className="h-4 w-4" />
        <AlertTitle>Conflicts</AlertTitle>
        <AlertDescription>
          {conflicts.messages.length === 0 ? (
            <p>No overlaps detected.</p>
          ) : (
            <ul className="list-disc pl-5 space-y-1">
              {conflicts.messages.map((message) => (
                <li key={message}>{message}</li>
              ))}
            </ul>
          )}
        </AlertDescription>
      </Alert>
    </div>
  );
}
```
:::
