import maya.cmds as cmds
import maya.api.OpenMaya as om
import math

# Get vectors of LOC 1 and LOC 2
vec1 = cmds.xform('shoulder_R_jointPosition', q=True, ws=True, t=True)

vec2 = cmds.xform('elbow_R_jointPosition', q=True, ws=True, t=True)

# Get the angle of the vector that points from LOC 1 to LOC 2
orient = cmds.angleBetween(er=True, v1=vec2, v2=vec1)

# Test for correct angle by orienting LOC 1
cmds.xform('shoulder_R_jointPosition', a=True, ro=orient)
