# Increase the volume of a file to 200% of the original
ffmpeg -i input.mkv -vcodec copy -filter:a "volume=2.000000" output.louder.mkv

# Convert a file to a format that iMovie can import
ffmpeg -i input.avi -pix_fmt yuv420p output.mp4
