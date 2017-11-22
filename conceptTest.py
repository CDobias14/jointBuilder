import maya.cmds as cmds
import maya.api.OpenMaya as om
import math

# Get vectors of LOC 1 and LOC 2
vec1Raw = cmds.xform('shoulder_R_jointPosition', q=True, ws=True, t=True)
vec1Pos = om.MVector(vec1Raw[0], vec1Raw[1], vec1Raw[2])

vec2Raw = cmds.xform('elbow_R_jointPosition', q=True, ws=True, t=True)
vec2Pos = om.MVector(vec2Raw[0], vec2Raw[1], vec2Raw[2])

# Get difference of the two vectors
vec3 = (vec2Pos - vec1Pos)

# Get the angle of the vector that points from LOC 1 to LOC 2
orient = cmds.angleBetween(er=True, v1=vec1Pos, v2=vec3)

# Test for correct angle by orienting LOC 1
cmds.xform('shoulder_R_jointPosition', a=True, ro=orient)
