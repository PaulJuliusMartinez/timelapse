import argparse

parser = argparse.ArgumentParser(description="Resize and rename files using imagemagick")
parser.add_argument("-f", "--filetype", default="jpeg", choices=["all", "jpeg", "jpg", "png", help="Choose filetypes to be resized")
parser.add_argument("-s", "--size", default="1920x1080", help="resolution of resized images")

args = parser.parse_args()

print args.filetype
print args.size
