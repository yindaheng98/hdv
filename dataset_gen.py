import cv2
import os
import subprocess

root = "videos"
train_root = "train"
valid_root = "valid"
ffmpeg = "ffmpeg"

train_rate = 3
valid_clip_length = 30
min_clip_length = valid_clip_length

for name in os.listdir(root):

    path = os.path.join(root, name)
    cap = cv2.VideoCapture(path)
    if not cap.isOpened():
        print("cannot open", path)
        continue
    rate = int(cap.get(5))
    frame_num = int(cap.get(7))

    clip_num = frame_num // valid_clip_length
    print(rate, frame_num, clip_num)

    valid_idx = list(range(0, clip_num, train_rate + 1))
    valid_ranges = [(idx * valid_clip_length, (idx + 1) * valid_clip_length) for idx in valid_idx]

    for i in range(len(valid_ranges)):

        frame_start, frame_end = valid_ranges[i]
        clip_name = os.path.splitext(name)[0]+f"-{frame_start}_{frame_end}" + os.path.splitext(name)[-1]
        clip_path = os.path.join(valid_root, clip_name)
        print("valid", clip_name, clip_path)
        os.makedirs(os.path.dirname(clip_path), exist_ok=True)
        cmd = [ffmpeg, '-i', path, '-vf', f'select=between(n\,{frame_start}\,{frame_end})', '-y', clip_path]
        subprocess.run(cmd)

        if i+1 < len(valid_ranges):
            frame_start, frame_end = frame_end, valid_ranges[i+1][0]
        else:
            frame_start, frame_end = frame_end, frame_num
        if frame_end - frame_start < min_clip_length:
            continue
        clip_name = os.path.splitext(name)[0]+f"-{frame_start}_{frame_end}" + os.path.splitext(name)[-1]
        clip_path = os.path.join(train_root, clip_name)
        print("train", clip_name, clip_path)
        os.makedirs(os.path.dirname(clip_path), exist_ok=True)
        cmd = [ffmpeg, '-i', path, '-vf', f'select=between(n\,{frame_start}\,{frame_end})', '-y', clip_path]
        subprocess.run(cmd)
