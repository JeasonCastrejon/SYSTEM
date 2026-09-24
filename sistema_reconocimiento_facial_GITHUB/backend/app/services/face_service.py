import cv2
import numpy as np
from insightface.app import FaceAnalysis


# Inicializar modelo facial
face_app = FaceAnalysis(
    name="buffalo_l",
    providers=["CPUExecutionProvider"]
)

face_app.prepare(ctx_id=0, det_size=(640, 640))


def validate_image(data: bytes) -> np.ndarray:
    arr = np.frombuffer(data, np.uint8)
    image = cv2.imdecode(arr, cv2.IMREAD_COLOR)

    if image is None:
        raise ValueError("El archivo no es una imagen válida.")

    if image.shape[0] < 120 or image.shape[1] < 120:
        raise ValueError("La imagen es demasiado pequeña.")

    return image


def image_quality(image: np.ndarray) -> float:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    sharp = float(cv2.Laplacian(gray, cv2.CV_64F).var())

    return max(0.0, min(1.0, sharp / 500.0))


def illumination(image: np.ndarray) -> float:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    mean = float(gray.mean()) / 255.0

    return max(0.0, 1.0 - abs(mean - 0.5) * 2)


def get_face_embedding(image: np.ndarray) -> np.ndarray:
    """
    Detecta el rostro y genera su embedding facial.
    """

    faces = face_app.get(image)

    if not faces:
        raise ValueError("No se detectó ningún rostro.")

    # Tomamos el rostro con mayor tamaño
    face = max(
        faces,
        key=lambda f: (f.bbox[2] - f.bbox[0]) *
                      (f.bbox[3] - f.bbox[1])
    )

    return face.embedding
