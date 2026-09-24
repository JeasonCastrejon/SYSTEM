import axios from "axios";
import type { DashboardData, MLMetrics, Persona, ProbabilityInput, RecognitionResult } from "../types/facial";
export const api=axios.create({baseURL:import.meta.env.VITE_API_URL||"http://127.0.0.1:8000",timeout:30000});
export async function health(){return (await api.get("/api/health")).data}
export async function dashboard():Promise<DashboardData>{return (await api.get("/api/dashboard")).data}
export async function listarPersonas():Promise<Persona[]>{return (await api.get("/api/personas")).data}
export async function crearPersona(p:{nombre:string;email:string}){return (await api.post("/api/personas",p)).data}
export async function guardarRostro(id:number,file:File){const f=new FormData();f.append("file",file);return (await api.post(`/api/personas/${id}/rostro`,f,{headers:{"Content-Type":"multipart/form-data"}})).data}
export async function reconocerRostro(file:File):Promise<RecognitionResult>{const f=new FormData();f.append("file",file);return (await api.post("/api/reconocimiento",f,{headers:{"Content-Type":"multipart/form-data"}})).data}
export async function historial(){return (await api.get("/api/reconocimiento/historial")).data}
export async function predecirProbabilidad(p:ProbabilityInput){return (await api.post("/api/probabilidades/prediccion",p)).data}
export async function obtenerMetricas():Promise<MLMetrics>{return (await api.get("/api/modelos/metricas")).data}
export async function entrenarModelo(){return (await api.post("/api/modelos/entrenar")).data}
