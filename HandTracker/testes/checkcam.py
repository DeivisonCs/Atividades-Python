import cv2

# Testar índices de 0 a 10
for i in range(10):
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        print(f"Câmera encontrada no índice {i}")
        cap.release()
    else:
        print(f"Nenhuma câmera no índice {i}")
