import cv2

def main():
    class_file = "coco.names"
    config_path = "ssd.pbtxt"
    weights_path = "file.pb"

    # Charger les noms de classes
    with open(class_file, "rt") as f:
        class_names = f.read().rstrip("\n").split("\n")

    # Charger le modèle
    net = cv2.dnn_DetectionModel(weights_path, config_path)
    net.setInputSize(320, 320)
    net.setInputScale(1.0 / 127.5)
    net.setInputMean((127.5, 127.5, 127.5))
    net.setInputSwapRB(True)

    thres = 0.45

    # Caméra
    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)
    cap.set(10, 70)

    if not cap.isOpened():
        print("Erreur: impossible d'ouvrir la caméra.")
        return

    while True:
        success, frame = cap.read()
        if not success:
            print("Erreur: impossible de lire une frame.")
            break

        # Détection
        class_ids, confs, bbox = net.detect(frame, confThreshold=thres)

        # Dessin des résultats (si détection)
        if class_ids is not None and len(class_ids) > 0:
            for class_id, confidence, box in zip(class_ids.flatten(), confs.flatten(), bbox):
                cv2.rectangle(frame, box, (0, 255, 0), 2)

                label = class_names[class_id - 1].upper()
                conf_txt = f"{confidence * 100:.2f}%"

                cv2.putText(frame, label, (box[0] + 10, box[1] + 30),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                cv2.putText(frame, conf_txt, (box[0] + 10, box[1] + 65),
                            cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)

        cv2.imshow("Object Detection (OpenCV)", frame)

        # Quitter avec 'q'
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
