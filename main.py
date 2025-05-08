import cv2
import torch
import numpy as np
import matplotlib.path as mplPath

ZONAPRINCIPAL = np.array([
    [289, 587],
    [807, 591],
    [685, 104],
    [560, 105],
])

ZONAFLECHA = np.array([
    [812, 590],
    [1065, 585],
    [749, 100],
    [684, 100],
])


def get_center(bbox):
    center = ((bbox[0] + bbox[2]) // 2, (bbox[1] + bbox[3]) // 2)
    return center


def load_model():
    model = torch.hub.load("ultralytics/yolov5", model="yolov5n", pretrained=True)
    return model


def get_bboxes(preds: object):
    df = preds.pandas().xyxy[0]
    df = df[df["confidence"] >= 0.1]
    df = df[df["name"] == "car"]

    return df[["xmin", "ymin", "xmax", "ymax"]].values.astype(int)


def is_valid_detection_main(xc, yc):
    return mplPath.Path(ZONAPRINCIPAL).contains_point((xc, yc))


def is_valid_detection_arrow(xc, yc):
    return mplPath.Path(ZONAFLECHA).contains_point((xc, yc))


def detector(cap: object):
    model = load_model()

    while cap.isOpened():
        status, frame = cap.read()
        if not status:
            break

        preds = model(frame)
        bboxes = get_bboxes(preds)

        detectionsmain = 0
        detectionarrow = 0

        for box in bboxes:
            xc, yc = get_center(box)

            if is_valid_detection_main(xc, yc):
                detectionsmain += 1

            if is_valid_detection_arrow(xc, yc):
                detectionarrow += 1

            cv2.circle(img=frame, center=(xc, yc), radius=5, color=(0, 0, 255), thickness=2)
            cv2.rectangle(img=frame, pt1=(box[0], box[1]), pt2=(box[2], box[3]), color=(255, 0, 0), thickness=2)

        cv2.putText(img=frame, text=f"RECTO: {detectionsmain}", org=(100, 100), fontFace=cv2.FONT_HERSHEY_PLAIN,
                    fontScale=3, color=(0, 0, 0), thickness=3)
        cv2.putText(img=frame, text=f"FLECHA: {detectionarrow}", org=(850, 100), fontFace=cv2.FONT_HERSHEY_PLAIN,
                    fontScale=3, color=(0, 0, 0), thickness=3)

        cv2.polylines(img=frame, pts=[ZONAPRINCIPAL], isClosed=True, color=(255, 0, 0), thickness=3)
        cv2.polylines(img=frame, pts=[ZONAFLECHA], isClosed=True, color=(0, 255, 0), thickness=2)

        cv2.imshow('frame', frame)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()


if __name__ == '__main__':
    cap = cv2.VideoCapture("data/video.mp4")
    detector(cap)
