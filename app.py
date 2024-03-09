import moviepy.editor as mpe

clip = mpe.VideoFileClip("runs/detect/predict/saved_video.avi")
clip.write_videofile("hello.mp4")
