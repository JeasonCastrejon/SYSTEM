import { useEffect, useState } from "react";
import { Activity, Brain, Fingerprint, Users } from "lucide-react";
import {
  ResponsiveContainer,
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
} from "recharts";

import PageHeader from "../components/PageHeader";
import StatCard from "../components/StatCard";
import { dashboard } from "../services/api";
import type { DashboardData } from "../types/facial";

export default function Dashboard() {
  const [d, setD] = useState<DashboardData | null>(null);

  useEffect(() => {
    dashboard()
      .then(setD)
      .catch(() => {});
  }, []);

  return (
    <div>
      <PageHeader
        title="Dashboard"
        description="Resumen general del sistema inteligente de reconocimiento facial y análisis de probabilidades."
      />

      {/* TARJETAS */}
      <div className="grid gap-4 sm:grid-cols-2 xl:grid-cols-4">
        <StatCard
          label="Personas registradas"
          value={d ? String(d.personas) : "—"}
          note="Desde la base de datos"
          icon={Users}
        />

        <StatCard
          label="Reconocimientos"
          value={d ? String(d.reconocimientos) : "—"}
          note="Historial registrado"
          icon={Fingerprint}
        />

        <StatCard
          label="Coincidencias"
          value={d ? String(d.coincidencias) : "—"}
          note="Resultados aceptados"
          icon={Brain}
        />

        <StatCard
          label="Estado API"
          value={d ? "Conectada" : "—"}
          note={
            d?.modelo_entrenado
              ? "Modelo ML disponible"
              : "Esperando datos/modelo"
          }
          icon={Activity}
        />
      </div>

      {/* GRÁFICO */}
      <div className="card mt-6 p-6">
        <div className="mb-5">
          <h2 className="text-lg font-bold">
            Registros del sistema
          </h2>

          <p className="text-sm text-slate-500">
            Personas registradas por fecha
          </p>
        </div>

        <div className="h-80 w-full">
          {d?.registros_por_fecha?.length ? (
            <ResponsiveContainer width="100%" height="100%">
              <LineChart data={d.registros_por_fecha}>
                <CartesianGrid strokeDasharray="3 3" />

                <XAxis dataKey="fecha" />

                <YAxis allowDecimals={false} />

                <Tooltip />

                <Line
                  type="monotone"
                  dataKey="cantidad"
                  strokeWidth={3}
                  dot={{ r: 4 }}
                />
              </LineChart>
            </ResponsiveContainer>
          ) : (
            <div className="flex h-full items-center justify-center rounded-xl border border-dashed border-slate-300">
              <p className="text-sm text-slate-500">
                Todavía no hay registros para mostrar.
              </p>
            </div>
          )}
        </div>
      </div>

      {/* FLUJO */}
      <div className="card mt-6 p-6">
        <h2 className="font-bold">Flujo del sistema</h2>

        <div className="mt-5 grid gap-3 md:grid-cols-5">
          {[
            "Registro",
            "Captura",
            "Embedding",
            "Comparación",
            "Probabilidad ML",
          ].map((x, i) => (
            <div
              key={x}
              className="rounded-xl border border-slate-200 p-4"
            >
              <b className="text-blue-600">0{i + 1}</b>

              <p className="mt-2 text-sm font-semibold">
                {x}
              </p>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}