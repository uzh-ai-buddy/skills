:::artifact{identifier="navigation-card" type="application/vnd.react" title="Navigation Card"}
```react
import React from "react";
import { Badge } from "./components/ui/badge";
import { Card, CardContent, CardHeader, CardTitle } from "./components/ui/card";
import { Separator } from "./components/ui/separator";
import { MapPin, Train, Clock, ExternalLink, Accessibility } from "lucide-react";

/* ── Data constants (agent fills from tool results) ── */

const building = { code: "KOL", name: "Kollegiengebäude", address: "Rämistrasse 71, 8006 Zürich", campus: "Zentrum" };

const googleMapsUrl = "https://www.google.com/maps/search/?api=1&query=Rämistrasse+71+8006+Zürich";
const campusMapUrl = "https://www.plaene.uzh.ch/KOL";

const accessibility = null;
/* Example: { wheelchair_entrance: "Main entrance", has_ramp: true, has_elevator: true, has_automatic_doors: false } */

const transitConnections = [];
/* Example: [{ departure: "14:05", arrival: "14:28", duration_min: 23, transfers: 1, from_location: "Zürich HB", to_location: "ETH/Universitätsspital", legs: [{ line: "Tram 9", category: "T", from_station: "Zürich HB", to_station: "ETH/Universitätsspital", departure: "14:05", arrival: "14:28" }] }] */

const departures = [];
/* Example: [{ line: "Tram 9", category: "T", destination: "Hirzenbach", departure: "14:05", platform: null }] */

const stopName = "";

/* ── Helpers ── */

const lineBadgeColor = (category) => {
  const map = {
    T: "bg-blue-100 text-blue-800",
    B: "bg-green-100 text-green-800",
    S: "bg-purple-100 text-purple-800",
    train: "bg-indigo-100 text-indigo-800",
    walk: "bg-slate-100 text-slate-600",
  };
  return map[category] || "bg-slate-100 text-slate-700";
};

const formatTime = (iso) => {
  if (!iso) return "";
  try {
    const d = new Date(iso);
    if (isNaN(d.getTime())) return iso;
    return d.toLocaleTimeString("de-CH", { hour: "2-digit", minute: "2-digit" });
  } catch {
    return iso;
  }
};

/* ── Component ── */

export default function NavigationCard() {
  return (
    <div className="p-6 font-sans space-y-6">
      {/* Building header */}
      <Card>
        <CardHeader>
          <CardTitle className="flex items-center gap-2">
            <MapPin className="h-5 w-5 text-slate-500" />
            {building.name}
          </CardTitle>
          <div className="flex flex-wrap gap-2 mt-1">
            <Badge variant="outline">{building.code}</Badge>
            <Badge className="bg-slate-100 text-slate-700">{building.campus}</Badge>
          </div>
          <p className="text-sm text-slate-600 mt-2">{building.address}</p>
        </CardHeader>
        <CardContent className="flex flex-wrap gap-3">
          <a
            href={googleMapsUrl}
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center gap-2 rounded-md bg-blue-600 px-4 py-2 text-sm font-medium text-white hover:bg-blue-700 transition-colors"
          >
            <ExternalLink className="h-4 w-4" />
            Open in Google Maps
          </a>
          <a
            href={campusMapUrl}
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center gap-2 rounded-md border border-slate-300 bg-white px-4 py-2 text-sm font-medium text-slate-700 hover:bg-slate-50 transition-colors"
          >
            <ExternalLink className="h-4 w-4" />
            Open Campus Map
          </a>
        </CardContent>
      </Card>

      {/* Transit connections */}
      {transitConnections.length > 0 && (
        <>
          <Separator />
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center gap-2 text-lg">
                <Train className="h-5 w-5 text-slate-500" />
                Transit Connections
              </CardTitle>
            </CardHeader>
            <CardContent className="space-y-4">
              {transitConnections.map((conn, idx) => (
                <div key={idx} className="rounded-lg border p-4 space-y-3">
                  <div className="flex flex-wrap items-center gap-3">
                    <span className="font-medium text-slate-800">
                      {formatTime(conn.departure)} → {formatTime(conn.arrival)}
                    </span>
                    {conn.duration_min != null && (
                      <Badge className="bg-amber-100 text-amber-800">
                        {conn.duration_min} min
                      </Badge>
                    )}
                    <Badge variant="outline">
                      {conn.transfers === 0
                        ? "Direct"
                        : `${conn.transfers} transfer${conn.transfers > 1 ? "s" : ""}`}
                    </Badge>
                  </div>
                  <div className="space-y-2">
                    {conn.legs.map((leg, legIdx) => (
                      <div
                        key={legIdx}
                        className="flex flex-wrap items-center gap-2 text-sm text-slate-600"
                      >
                        {leg.line && (
                          <Badge className={lineBadgeColor(leg.category)}>
                            {leg.line}
                          </Badge>
                        )}
                        <span>
                          {leg.from_station} → {leg.to_station}
                        </span>
                        <span className="text-slate-400">
                          {formatTime(leg.departure)} – {formatTime(leg.arrival)}
                        </span>
                      </div>
                    ))}
                  </div>
                </div>
              ))}
            </CardContent>
          </Card>
        </>
      )}

      {/* Departure board */}
      {departures.length > 0 && (
        <>
          <Separator />
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center gap-2 text-lg">
                <Clock className="h-5 w-5 text-slate-500" />
                Departures{stopName ? ` — ${stopName}` : ""}
              </CardTitle>
            </CardHeader>
            <CardContent>
              <div className="overflow-x-auto">
                <table className="w-full text-sm">
                  <thead>
                    <tr className="border-b text-left text-slate-500">
                      <th className="pb-2 pr-4 font-medium">Line</th>
                      <th className="pb-2 pr-4 font-medium">Direction</th>
                      <th className="pb-2 pr-4 font-medium">Departs</th>
                      <th className="pb-2 font-medium">Platform</th>
                    </tr>
                  </thead>
                  <tbody>
                    {departures.map((dep, idx) => (
                      <tr key={idx} className="border-b last:border-0">
                        <td className="py-2 pr-4">
                          <Badge className={lineBadgeColor(dep.category)}>
                            {dep.line || "—"}
                          </Badge>
                        </td>
                        <td className="py-2 pr-4 text-slate-700">{dep.destination}</td>
                        <td className="py-2 pr-4 font-medium text-slate-800">
                          {formatTime(dep.departure)}
                        </td>
                        <td className="py-2 text-slate-600">{dep.platform || "—"}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </CardContent>
          </Card>
        </>
      )}

      {/* Accessibility */}
      {accessibility != null && (
        <>
          <Separator />
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center gap-2 text-lg">
                <Accessibility className="h-5 w-5 text-slate-500" />
                Accessibility
              </CardTitle>
            </CardHeader>
            <CardContent>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 text-sm">
                {accessibility.wheelchair_entrance && (
                  <div>
                    <span className="font-medium text-slate-700">Wheelchair entrance:</span>{" "}
                    <span className="text-slate-600">{accessibility.wheelchair_entrance}</span>
                  </div>
                )}
                {accessibility.has_ramp != null && (
                  <div>
                    <span className="font-medium text-slate-700">Ramp:</span>{" "}
                    <span className="text-slate-600">{accessibility.has_ramp ? "Yes" : "No"}</span>
                  </div>
                )}
                {accessibility.has_elevator != null && (
                  <div>
                    <span className="font-medium text-slate-700">Elevator:</span>{" "}
                    <span className="text-slate-600">{accessibility.has_elevator ? "Yes" : "No"}</span>
                  </div>
                )}
                {accessibility.has_automatic_doors != null && (
                  <div>
                    <span className="font-medium text-slate-700">Automatic doors:</span>{" "}
                    <span className="text-slate-600">{accessibility.has_automatic_doors ? "Yes" : "No"}</span>
                  </div>
                )}
                {accessibility.wheelchair_parking && (
                  <div>
                    <span className="font-medium text-slate-700">Wheelchair parking:</span>{" "}
                    <span className="text-slate-600">{accessibility.wheelchair_parking}</span>
                  </div>
                )}
                {accessibility.door_width_cm != null && (
                  <div>
                    <span className="font-medium text-slate-700">Door width:</span>{" "}
                    <span className="text-slate-600">{accessibility.door_width_cm} cm</span>
                  </div>
                )}
              </div>
            </CardContent>
          </Card>
        </>
      )}
    </div>
  );
}
```
:::
