# !/bin/python3

import os
import sys

right_init = sys.argv[1]
right_cur = sys.argv[2]
right_vector = " ".join(sys.argv[3].split('_'))
right_angle = sys.argv[4]

left_init = sys.argv[5]
left_cur = sys.argv[6]
left_vector = " ".join(sys.argv[7].split('_'))
left_angle = sys.argv[8]


os.system("surfaceTransformPoints -rotate-angle '(("+ str(right_vector) +")" + right_angle + ")' " + right_init + " " + right_cur)
os.system("surfaceTransformPoints -rotate-angle '(("+ str(left_vector) +")" + left_angle + ")' " + left_init + " " + left_cur)