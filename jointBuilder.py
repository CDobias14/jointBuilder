import maya.cmds as cmds
import maya.api.OpenMaya as om
import math
from functools import partial


# VARIABLES
widgets = {}

def jointBuilderUI():
    # Check to see if the window already exists
    if cmds.window('jointBuilderUI', exists = True):
        cmds.deleteUI('jointBuilderUI')
    
    # Create the window
    widgets['jointBuilderWindow'] = cmds.window('jointBuilderUI', title = 'Joint  Builder', w = 300, h = 50, rtf = True, mnb = False, mxb = False, sizeable = False)
    
    # Create the main layout
    widgets['mainLayout'] = cmds.columnLayout('mainLayout', w = 300, h = 50)
    
    # Add banner image
    widgets['imagePath'] = cmds.internalVar(upd = True) + 'icons/jointBuilderBanner.jpg'
    cmds.image(w = 300, h = 90, image = widgets['imagePath'])
    
    
    # Create the Settings divider
    cmds.frameLayout('settings', l = 'Settings', w = 298)
    cmds.separator(h = 5, st = 'none')
    
    cmds.setParent(widgets['mainLayout'])
    
    
    # Create the downAxisRow layout
    widgets['downAxisRow'] = cmds.rowLayout('downAxisRow', nc = 2, cw = [(1,100),(2,200)], ct2 = ['both', 'left'])
    
    # Create down axis menu
    cmds.text(l = 'Down Axis')
    widgets['downAxisMenu'] = cmds.optionMenu('downAxisMenu', w = 45, cc = 'populateUpAxis()')
    cmds.menuItem(l = 'X')
    cmds.menuItem(l = 'Y')
    cmds.menuItem(l = 'Z')
    
    cmds.setParent(widgets['mainLayout'])
    cmds.separator(h = 5)
    
    
    # Create the upAxisRow layout
    widgets['upAxisLocRow'] = cmds.rowLayout('upAxisLocRow', nc = 2, cw = [(1,100),(2,200)], ct2 = ['both', 'left'])
    
    # Create up axis menu
    cmds.text(l = 'Up Axis')
    cmds.optionMenu('upAxisMenu', w = 45)
    populateUpAxis()
    
    cmds.setParent(widgets['mainLayout'])
    cmds.separator(h = 5)
    
    
    # Create the Locators divider
    cmds.frameLayout('locators', l = 'Locators', w = 300, h = 20)
    
    cmds.setParent(widgets['mainLayout'])
    cmds.separator(h = 5)
    
    
    # Create the jointLoc1Row layout
    widgets['jointLoc1Row'] = cmds.rowLayout('jointLoc1Row', nc = 3, cw = [(1,100),(2,20),(3,180)], ct3 = ['both', 'both', 'right'], co3 = [0, 2, 12])
    
    # Create jointLoc1 selector
    cmds.text(l = 'Start Joint Locator')
    cmds.button(l = '>', c = 'getObj(widgets["jointLoc1TextField"])', w = 20, h = 22)
    widgets['jointLoc1TextField'] = cmds.textField('jointLoc1TextField', w = 158)
    
    cmds.setParent(widgets['mainLayout'])
    cmds.separator(h = 5)
    
    
    # Create the jointLoc2Row layout
    widgets['jointLoc2Row'] = cmds.rowLayout('jointLoc2Row', nc = 3, cw = [(1,100),(2,20),(3,180)], ct3 = ['both', 'both', 'right'], co3 = [0, 2, 12])
    
    # Create jointLoc2 selector
    cmds.text(l = 'Mid Joint Locator')
    cmds.button(l = '>', c = 'getObj(widgets["jointLoc2TextField"])', w = 20, h = 22)
    widgets['jointLoc2TextField'] = cmds.textField('jointLoc2TextField', w = 158)
    
    cmds.setParent(widgets['mainLayout'])
    cmds.separator(h = 5)
    
        
    # Create the jointLoc3Row layout
    widgets['jointLoc3Row'] = cmds.rowLayout('jointLoc3Row', nc = 3, cw = [(1,100),(2,20),(3,180)], ct3 = ['both', 'both', 'right'], co3 = [0, 2, 12])
    
    # Create jointLoc3 selector
    cmds.text(l = 'End Joint Locator')
    cmds.button(l = '>', c = 'getObj(widgets["jointLoc3TextField"])', w = 20, h = 22)
    widgets['jointLoc3TextField'] = cmds.textField('jointLoc3TextField', w = 158)
    
    cmds.setParent(widgets['mainLayout'])
    cmds.separator(h = 5)
    
    
    # Create the buildJointsRow layout
    widgets['buildJointsRow'] = cmds.rowLayout('buildJointsRow', nc = 1, cw = [(1, 300)], ct1 = 'left', co1 = 5)
    
    # Create the buildJoints button
    widgets['buildJointsButton'] = cmds.button('Build Joints', w = 286, c = 'buildJoints("{}".format(cmds.optionMenu("downAxisMenu", q = True, v = True)), cmds.optionMenu("upAxisMenu", q = True, v = True))')
    
    
    # Show the window
    cmds.showWindow(widgets['jointBuilderWindow'])

def populateUpAxis(*args):
    
    widgets['upAxisMenuItems'] = cmds.optionMenu('upAxisMenu', q = True, itemListLong = True)
    
    if widgets['upAxisMenuItems'] != None:
        for item in widgets['upAxisMenuItems']:
            cmds.deleteUI(item)
    
    # Get the current value of the down axis menu
    widgets['selectedDownAxis'] = cmds.optionMenu('downAxisMenu', q = True, v = True)
    
    widgets['upAxisOptions'] = ['+X', '-X', '+Y', '-Y', '+Z', '-Z']
    widgets['upAxisOptionsReference'] = ['X', 'X', 'Y', 'Y', 'Z', 'Z']
    
    # Add upAxisOptions based on selectedDownAxis
    for idx, upAxis in enumerate(widgets['upAxisOptions']):
        if widgets['selectedDownAxis'] == widgets['upAxisOptionsReference'][idx]:
            pass
        else:
            cmds.menuItem(l = widgets['upAxisOptions'][idx]) 
    
    
def getObj(caller, *args):
    # Get selected object and put it in the caller's field
    if len(cmds.ls(sl = True)) >= 1:
        sel = cmds.ls(sl = True)[0]
        cmds.textField('{}'.format(caller), e = True, tx = sel)
    elif len(cmds.ls(sl = True)) == 0:
        print('No targets selected.')
        cmds.textField('{}'.format(caller), e = True, tx = '')

def buildJoints(downAxis, upAxis, *args):
    # Create list of locator names
    widgets['buildLocators'] = [cmds.textField('jointLoc1TextField', q = True, tx = True), cmds.textField('jointLoc2TextField', q = True, tx = True), cmds.textField('jointLoc3TextField', q = True, tx = True)]
    
    # Get necessary vectors based on locators
    for vecIdx, loc in enumerate(widgets['buildLocators']):
        # Get the raw position of each locator and make a vector out of it
        widgets['vec{}Raw'.format(vecIdx)] = cmds.xform('{}'.format(loc), q = True, ws = True, t = True)
        widgets['vec{}Pos'.format(vecIdx)] = om.MVector(widgets['vec{}Raw'.format(vecIdx)][0], widgets['vec{}Raw'.format(vecIdx)][1], widgets['vec{}Raw'.format(vecIdx)][2])
        
        # Get a vector equal to the difference of each vector pair, and get the angle of that new vector.
        if vecIdx >= 1:
            widgets['vecDiff{}'.format(vecIdx - 1)] = (widgets['vec{}Pos'.format(vecIdx)] - widgets['vec{}Pos'.format(vecIdx - 1)])
            widgets['orient{}'.format(vecIdx - 1)] = cmds.angleBetween(er = True, v1 = [0,1,0], v2 = widgets['vecDiff{}'.format(vecIdx - 1)])
    
    print(downAxis)
    
    # Convert the downAxis and upAxis variables into usable flags
    if downAxis is 'X':
        downAxis = 'xyz'
    elif downAxis is 'Y':
        downAxis = 'yxz'
    else:
        downAxis = 'zyx'
    
    if upAxis is '+X':
        upAxis = 'xup'
    elif upAxis is '-X':
        upAxis = 'xdown'
    elif upAxis is '+Y':
        upAxis = 'yup'
    elif upAxis is '-Y':
        upAxis = 'ydown'
    elif upAxis is '+Z':
        upAxis = 'zup'
    else:
        upAxis = 'zdown'
    
    # Create the joints
    for jntIdx, jnt in enumerate(widgets['buildLocators']):
        if jntIdx <= 1:
            cmds.joint(a = True, p = widgets['vec{}Raw'.format(jntIdx)], o = widgets['orient{}'.format(jntIdx)], n = 'loc{}Joint'.format(jntIdx + 1))
            cmds.joint('loc{}Joint'.format(jntIdx + 1), e = True, oj = '{}'.format(downAxis), sao = '{}'.format(upAxis))
        else:
            cmds.joint(a = True, p = widgets['vec{}Raw'.format(jntIdx)], n = 'loc3Joint')

jointBuilderUI()
