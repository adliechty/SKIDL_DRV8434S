from skidl import *

def addPassive(passiveType, size, value, Radial = False):
  if passiveType == 'C':
    if Radial == True:
      newPart = Part("Device", passiveType, footprint='Capacitor_THT:CP_Radial_D10.0mm_P5.00mm')
    else:
      newPart = Part("Device", passiveType, footprint='Capacitor_SMD:C_0402_1005Metric_Pad0.74x0.62mm_HandSolder')
  elif passiveType == 'R':
    newPart = Part("Device", passiveType, footprint='Resistor_SMD:R_0402_1005Metric_Pad0.72x0.64mm_HandSolder')
  newPart.value = value
  return newPart

def addBypassCap(size, value, net1, net2):
    cap = addPassive('C', size, value)
    Net.get(net1) & cap & Net.get(net2)
#example size value list is as follows:
#[['0402', '0.1uF'],
# ['0805', '10.0uF']]
def addBypassCaps(sizeValueList, net1, net2):
  for sizeValuePair in sizeValueList:
    addBypassCap(sizeValuePair[0], sizeValuePair[1], net1, net2)

def addPull(size, value, net1, net2):
    pull = addPassive('R', size, value)
    Net.get(net1) & pull & Net.get(net2)
