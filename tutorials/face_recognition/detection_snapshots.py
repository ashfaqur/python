import datetime
import time

import cv2
import face_recognition

PERIOD_BETWEEN_DETECTION = 2000
VIDEO_DEVICE_ID = 0


def time_ms():
    return time.time() * 1000


def do_process(last_time_stamp):
    return (time_ms() - last_time_stamp) > PERIOD_BETWEEN_DETECTION


def get_image_filename():
    current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
    return current_time + '.jpg'


def main():
    last_process_time = 0
    face_detection_counter = 0
    video_capture = cv2.VideoCapture(VIDEO_DEVICE_ID)
    if not video_capture:
        print(f'No video capture device for id {VIDEO_DEVICE_ID}')
        exit(1)

    while True:
        if not do_process(last_process_time):
            continue
        last_process_time = time_ms()
        _, frame = video_capture.read()

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        rgb_frame = small_frame[:, :, ::-1]
        print('Looking for faces...')
        face_locations = face_recognition.face_locations(rgb_frame)

        if len(face_locations) > 0:
            face_detection_counter += 1
            print(f'FACE detected #{face_detection_counter}')
            file_name = get_image_filename()
            print(file_name)
            cv2.imwrite(file_name, small_frame)

    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('Stopping script with keyboard interrupt')
