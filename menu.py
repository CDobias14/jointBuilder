import maya.cmds as cmds
import maya.api.OpenMaya as om
import math


### VARIABLES
widgets = {}

### FUNCTIONS

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
    cmds.optionMenu('downAxisMenu', w = 45)
    cmds.menuItem(l = 'X')
    cmds.menuItem(l = 'Y')
    cmds.menuItem(l = 'Z')
    
    cmds.setParent(widgets['mainLayout'])
    cmds.separator(h = 5)
    
    
    # Create the upAxisLoc layout
    widgets['upAxisLocRow'] = cmds.rowLayout('upAxisLocRow', nc = 3, cw = [(1,100),(2,20),(3,180)], ct3 = ['both', 'both', 'right'], co3 = [5, 2, 12])
    
    # Create up axis loc selector
    cmds.text(l = 'Up Axis Locator')
    cmds.button(l = '>', c = 'getObj(widgets["upAxisLocTextField"])', w = 20, h = 22)
    widgets['upAxisLocTextField'] = cmds.textField('upAxisLocTextField', w = 158)
    
    cmds.setParent(widgets['mainLayout'])
    cmds.separator(h = 5)
    
    
    # Create the Locators divider
    cmds.frameLayout('locators', l = 'Locators', w = 300, h = 20)
    
    cmds.setParent(widgets['mainLayout'])
    cmds.separator(h = 5)
    
    
    # Create the jointLoc1 layout
    widgets['jointLoc1Row'] = cmds.rowLayout('jointLoc1Row', nc = 3, cw = [(1,100),(2,20),(3,180)], ct3 = ['both', 'both', 'right'], co3 = [5, 2, 12])
    
    # Create jointLoc1 selector
    cmds.text(l = 'Joint Locator 1')
    cmds.button(l = '>', c = 'getObj(widgets["jointLoc1TextField"])', w = 20, h = 22)
    widgets['jointLoc1TextField'] = cmds.textField('jointLoc1TextField', w = 158)
    
    cmds.setParent(widgets['mainLayout'])
    cmds.separator(h = 5)
    
    
    # Create the jointLoc2 layout
    widgets['jointLoc2Row'] = cmds.rowLayout('jointLoc2Row', nc = 3, cw = [(1,100),(2,20),(3,180)], ct3 = ['both', 'both', 'right'], co3 = [5, 2, 12])
    
    # Create jointLoc2 selector
    cmds.text(l = 'Joint Locator 2')
    cmds.button(l = '>', c = 'getObj(widgets["jointLoc2TextField"])', w = 20, h = 22)
    widgets['jointLoc2TextField'] = cmds.textField('jointLoc2TextField', w = 158)
    
    cmds.setParent(widgets['mainLayout'])
    cmds.separator(h = 5)
    
        
    # Create the jointLoc3 layout
    widgets['jointLoc3Row'] = cmds.rowLayout('jointLoc3Row', nc = 3, cw = [(1,100),(2,20),(3,180)], ct3 = ['both', 'both', 'right'], co3 = [5, 2, 12])
    
    # Create jointLoc3 selector
    cmds.text(l = 'Joint Locator 3')
    cmds.button(l = '>', c = 'getObj(widgets["jointLoc3TextField"])', w = 20, h = 22)
    widgets['jointLoc3TextField'] = cmds.textField('jointLoc3TextField', w = 158)
    
    cmds.setParent(widgets['mainLayout'])
    cmds.separator(h = 5)
    
    
    # Create the BUILD layout
    widgets['buildJointsRow'] = cmds.rowLayout('buildJointsRow', nc = 1, cw = [(1, 300)], ct1 = 'left', co1 = 5)
    
    # Create the BUILD button
    widgets['buildJointsButton'] = cmds.button('buildJoints', w = 286)
    
    
    # Show the window
    cmds.showWindow(widgets['jointBuilderWindow'])


def getObj(caller, *args):
    # Get selected object and put it in the caller's field
    if len(cmds.ls(sl = True)) >= 1:
        sel = cmds.ls(sl = True)[0]
        cmds.textField('{}'.format(caller), e = True, tx = sel)
    elif len(cmds.ls(sl = True)) == 0:
        print('No targets selected.')
        cmds.textField('{}'.format(caller), e = True, tx = '')


jointBuilderUI()
