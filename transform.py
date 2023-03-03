# !/bin/python3

import os
import sys

right_init = sys.argv[1]
right_cur = sys.argv[2]
right_center = " ".join(sys.argv[3].split('_'))
right_vector = " ".join(sys.argv[4].split('_'))
right_angle = sys.argv[5]

left_init = sys.argv[6]
left_cur = sys.argv[7]
left_center = " ".join(sys.argv[8].split('_'))
left_vector = " ".join(sys.argv[9].split('_'))
left_angle = sys.argv[10]

os.system(f"surfaceTransformPoints  -rotate-angle '(({right_vector}) {right_angle})' {right_init} {right_cur}")
os.system(f"surfaceTransformPoints  -rotate-angle '(({left_vector}) {left_angle})' {left_init} {left_cur}")


#os.system(f"surfaceTransformPoints -centre '({right_center})' -rotate-angle '(({right_vector}) {right_angle})' {right_init} {right_cur}")
#os.system(f"surfaceTransformPoints -centre '({left_center})' -rotate-angle '(({left_vector}) {left_angle})' {left_init} {left_cur}")