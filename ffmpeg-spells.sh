# Increase the volume of a file to 200% of the original
ffmpeg -i input.mkv -vcodec copy -filter:a "volume=2.000000" output.louder.mkv
