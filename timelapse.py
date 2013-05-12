import argparse

parser = argparse.ArgumentParser(description="Create a timelapse video of all the files in a given directory with a given framerate")
parser.add_argument("-s", "--source", default="./", help="source directory containing images")
parser.add_argument("-f", "--framerate", type=int, default=15, help="framerate of produced video")
args = parser.parse_args()

print args.source
print args.framerate
