import maya.cmds as cmds
import maya.api.OpenMaya as om
import math

# Get world position of LOC 1
wst = cmds.xform('shoulder_R_jointPosition', q=True, ws=True, t=True)

wst

# Get vector from LOC 1 to LOC 2
vec1Raw = cmds.xform('shoulder_R_jointPosition', q=True, ws=True, t=True)
vec1Raw
#vec1Pos = om.MVector(vec1Raw[0], vec1Raw[1], vec1Raw[2])
#vec1Pos

vec2Raw = cmds.xform('elbow_R_jointPosition', q=True, ws=True, t=True)
vec2Raw
#vec2Pos = om.MVector(vec2Raw[0], vec2Raw[1], vec2Raw[2])
#vec2Pos

vecTotal = (vec2Pos - vec1Pos)

# 
orient = cmds.angleBetween(er=True, v1=vec2Raw, v2=vec1Raw)

print(orient)

cmds.xform('shoulder_R_jointPosition', a=True, ro=orient,)
