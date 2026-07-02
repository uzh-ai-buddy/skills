:::artifact{identifier="weekly-timetable-columns" type="application/vnd.react" title="Weekly Timetable (Compact Columns)"}
```react
import React, { useMemo } from "react";
import { Alert, AlertDescription, AlertTitle } from "./components/ui/alert";
import { Badge } from "./components/ui/badge";
import { Card, CardContent, CardHeader, CardTitle } from "./components/ui/card";
import { AlertTriangle } from "lucide-react";

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
    id: "stats",
    day: "Fri",
    start: "09:00",
    end: "11:00",
    label: "Statistik",
    location: "KOL-F-117",
    category: "Lecture",
  },
];

const categoryColors = {
  Lecture: "#bfdbfe",
  Work: "#fde68a",
  Tutorial: "#bbf7d0",
};

const days = ["Mon", "Tue", "Wed", "Thu", "Fri"];

const toMinutes = (time) => {
  const [hours, minutes] = time.split(":").map(Number);
  return hours * 60 + minutes;
};

const overlaps = (first, second) =>
  toMinutes(first.start) < toMinutes(second.end) &&
  toMinutes(second.start) < toMinutes(first.end);

export default function WeeklyTimetableColumns() {
  const { grouped, conflicts } = useMemo(() => {
    const groupedEvents = events.reduce((acc, event) => {
      acc[event.day] = [...(acc[event.day] ?? []), event];
      return acc;
    }, {});

    const conflictIds = new Set();
    const conflictMessages = [];

    Object.values(groupedEvents).forEach((dayEvents) => {
      const sorted = [...dayEvents].sort(
        (a, b) => toMinutes(a.start) - toMinutes(b.start)
      );
      for (let i = 0; i < sorted.length; i += 1) {
        for (let j = i + 1; j < sorted.length; j += 1) {
          if (overlaps(sorted[i], sorted[j])) {
            conflictIds.add(sorted[i].id);
            conflictIds.add(sorted[j].id);
            conflictMessages.push(
              `${sorted[i].day}: ${sorted[i].label} (${sorted[i].start}-${sorted[i].end}) overlaps ${sorted[j].label} (${sorted[j].start}-${sorted[j].end})`
            );
          }
        }
      }
    });

    return {
      grouped: groupedEvents,
      conflicts: { ids: conflictIds, messages: conflictMessages },
    };
  }, []);

  return (
    <div className="p-6 font-sans space-y-4">
      <Card>
        <CardHeader>
          <CardTitle>Weekly Timetable</CardTitle>
          <p className="text-sm text-slate-600">
            Compact overview with conflict badges.
          </p>
          <div className="flex flex-wrap gap-2 text-sm text-slate-600">
            <Badge className="bg-blue-100 text-blue-900">Lecture</Badge>
            <Badge className="bg-yellow-200 text-yellow-900">Work</Badge>
            <Badge className="bg-red-100 text-red-700">Conflict</Badge>
          </div>
        </CardHeader>
        <CardContent>
          <div className="grid grid-cols-1 gap-4 md:grid-cols-5">
            {days.map((day) => (
              <div key={day} className="rounded-lg border bg-white p-3">
                <p className="text-sm font-semibold text-slate-700">{day}</p>
                <div className="mt-2 space-y-2">
                  {(grouped[day] ?? []).map((event) => {
                    const isConflict = conflicts.ids.has(event.id);
                    const color =
                      categoryColors[event.category] ?? categoryColors.Lecture;
                    return (
                      <div
                        key={event.id}
                        className="rounded-md border p-2 text-xs"
                        style={{
                          backgroundColor: color,
                          borderColor: isConflict ? "#ef4444" : "#e2e8f0",
                        }}
                      >
                        <div className="flex items-center justify-between gap-2">
                          <span className="font-semibold text-slate-900">
                            {event.start}–{event.end}
                          </span>
                          {isConflict ? (
                            <Badge className="bg-red-100 text-red-700">
                              Conflict
                            </Badge>
                          ) : null}
                        </div>
                        <p className="text-slate-700">{event.label}</p>
                        {event.location ? (
                          <p className="text-[11px] text-slate-500">
                            {event.location}
                          </p>
                        ) : null}
                        <Badge variant="secondary" className="mt-2">
                          {event.category}
                        </Badge>
                      </div>
                    );
                  })}
                  {(grouped[day] ?? []).length === 0 ? (
                    <p className="text-xs text-slate-500">No events</p>
                  ) : null}
                </div>
              </div>
            ))}
          </div>
        </CardContent>
      </Card>

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
