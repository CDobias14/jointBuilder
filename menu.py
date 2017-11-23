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
    widgets['jointBuilderWindow'] = cmds.window('jointBuilderUI', title = 'Joint Builder', w = 300, h = 300, mnb = False, mxb = False, sizeable = False)
    
    # Create the main layout
    widgets['mainLayout'] = cmds.columnLayout('mainLayout', w = 300, h = 300)
    
    # Add banner image
    widgets['imagePath'] = cmds.internalVar(upd = True) + 'icons/jointBuilderBanner.jpg'
    cmds.image(w = 300, h = 90, image = widgets['imagePath'])
    
    # Create the Settings divider
    cmds.frameLayout('settings', l = 'Settings', w = 298)
    
    # Create the rowColumn layout
    widgets['rowColumnLayout'] = cmds.rowColumnLayout('rowColumnLayout', w = 300, h = 300, nc = 2, cw = [(1, 95),(2, 195)], co = [(1, 'left', 5), (2, 'right', 5)])
    
    # Create down axis menu
    cmds.text(l = 'Down Axis')    
    cmds.optionMenu('downAxisMenu', w = 195)
    cmds.menuItem(l = 'X')
    cmds.menuItem(l = 'Y')
    cmds.menuItem(l = 'Z')
    
    # Create up axis loc selector
    cmds.button(l = 'Up Axis Locator', c = 'getObj(widgets["upAxisLocTextField"])', w = 85, h = 22)
    widgets['upAxisLocTextField'] = cmds.textField('upAxisLocTextField', w = 195)
    
    # Create joint suffix string entry box
    cmds.text(l = 'Joint Suffix')
    widgets['jointSuffix'] = cmds.textField('jointSuffix', w = 195)
    
    # Create intermediate column layout
    widgets['dividerLayout'] = cmds.columnLayout('dividerLayout', w = 300)
    
    # Create the Locators divider
    cmds.frameLayout('locators', l = 'Locators', w = 300, h = 20, parent = widgets['mainLayout'])
    
    # Show the window
    cmds.showWindow(widgets['jointBuilderWindow'])

def getObj(caller, *args):
    # Get selected object and put it in the caller's field
    if len(cmds.ls(sl = True)) == 1:
        sel = cmds.ls(sl = True)[0]
        cmds.textField('{}'.format(caller), e = True, tx = sel)
    elif len(cmds.ls(sl = True)) == 0:
        print('No targets selected.')
        cmds.textField('{}'.format(caller), e = True, tx = '')
    else:
        print('Too many targets selected.')

jointBuilderUI()
