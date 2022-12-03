import cv2
import os

root = "videos"
train_root = "train"
valid_root = "valid"
ffmpeg = "ffmpeg"
clip_length = 30

train_rate = 3

for name in os.listdir(root):

    path = os.path.join(root, name)
    cap = cv2.VideoCapture(path)
    if not cap.isOpened():
        print("cannot open", path)
        continue
    rate = int(cap.get(5))
    frame_num = int(cap.get(7))

    clip_num = frame_num // clip_length
    print(rate, frame_num, clip_num)

    valid_idx = list(range(0, clip_num, train_rate + 1))
    train_idx = 0
    for idx in range(clip_num):
        frame_start = idx * clip_length
        frame_end = frame_start+clip_length
        clip_name = os.path.splitext(name)[0]+f"-{frame_start}_{frame_end}" + os.path.splitext(name)[-1]
        if idx in valid_idx:
            clip_path = os.path.join(valid_root, clip_name)
            print("valid", clip_name, clip_path)
            train_idx += 1
        else:
            clip_path = os.path.join(train_root, str(train_idx), clip_name)
            print("train", clip_name, clip_path)
        cmd = [ffmpeg, '-i', path, '-vf', f'select=between(n\,{frame_start}\,{frame_end})', '-y', 'copy', clip_path]
        print(cmd)
