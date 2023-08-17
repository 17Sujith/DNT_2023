import cv2
input_video_path = '22_ccPWL6dq.mp4'
cap = cv2.VideoCapture(input_video_path)
fps = int(cap.get(5))
num_frames = int(cap.get(7))
slow_motion_factor = 2
for frame_index in range(num_frames - 1, -1, -1):
    cap.set(1, frame_index) 
    ret, frame = cap.read()
    if ret:
        for _ in range(slow_motion_factor):
            cv2.imshow('Reverse Slow Motion Video', frame)
            if cv2.waitKey(int(1000 / fps)) & 0xFF == 27: 
                break
    else:
        break
cv2.waitKey(0)
cv2.destroyAllWindows()
