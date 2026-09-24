export interface Persona { id:number; nombre:string; email:string; activo:boolean; created_at:string; }
export interface RecognitionResult { success?:boolean; persona_id:number|null; nombre:string|null; similitud:number; distancia:number; umbral:number; coincide:boolean; probabilidad_calibrada:number|null; }
export interface ProbabilityInput { similitud:number; distancia:number; calidad_imagen:number; iluminacion:number; }
export interface MLMetrics { precision:number|null; recall:number|null; f1:number|null; false_positive_rate:number|null; false_negative_rate:number|null; confusion_matrix:number[][]|null; modelo?:string|null; muestras?:number; }
export interface DashboardData {
  personas: number;
  reconocimientos: number;
  coincidencias: number;
  modelo_entrenado: boolean;

  registros_por_fecha: {
    fecha: string;
    cantidad: number;
  }[];
}