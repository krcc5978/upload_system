import cv2
import shutil
from tqdm import tqdm

start_time = 10
skip_frame = 10


def save_img(image_path, save_path):
    shutil.copy(image_path, save_path)


def load_movie(movie_path, save_path, file_name):
    cap = cv2.VideoCapture(movie_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    end = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))

    # 最初何秒飛ばすか
    for _ in tqdm(range(0, fps * start_time)):
        ret = cap.grab()
        if ret is False:
            break

    for i in tqdm(range(fps * start_time, end)):  # フレーム数分回す

        if i % skip_frame is 0:
            ret, frame = cap.read()
            cv2.imwrite(f'{save_path}/{file_name}_{str(i).zfill(digit)}.jpg', frame)
            if ret is False:
                break
        else:
            ret = cap.grab()
            if ret is False:
                break
