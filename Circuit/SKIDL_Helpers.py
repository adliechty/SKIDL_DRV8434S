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

def C(size, value, net1, net2):
    cap = addPassive('C', size, value)
    Net.get(net1) & cap & Net.get(net2)
#example size value list is as follows:
#[['0402', '0.1uF'],
# ['0805', '10.0uF']]
def addBypassCaps(sizeValueList, net1, net2):
  for sizeValuePair in sizeValueList:
    C(sizeValuePair[0], sizeValuePair[1], net1, net2)

def R(size, value, net1, net2):
    pull = addPassive('R', size, value)
    Net.get(net1) & pull & Net.get(net2)

def InstantiatePart(part, pinToNetMapping):
    pins = part.get_pins()
    missingPinToNetMappings = []
    newNets = []
    pinNames = []
    for pin in pins:
      if pin.name not in pinNames:
        pinNames.append(pin.name)

    for pin in pins:
      #Check if net name is in the net name mapping
      if pin.name in pinToNetMapping:
        NetName = pinToNetMapping[pin.name]
      else:
        NetName = pin.name
        missingPinToNetMappings.append(NetName)
      #Net already exists
      if Net.get(NetName):
        pin += Net.get(NetName)
        #print("Existing net: " + NetName)
      #Create a new net
      else:
        pin += Net(NetName)
        newNets.append(NetName)
        print("New net:      " + NetName)

    if missingPinToNetMappings:
      maxStrLength = max(len(x) for x in missingPinToNetMappings) 
      print("WARNING:  Add these mapings to the part instantiation, if mapping is 1:1 with pin name to net name:")
      for pin in missingPinToNetMappings:
        print('    \'' + pin + '\'' + ' ' * (maxStrLength - len(pin) + 1) + ': \'' + pin + '\',')

    if newNets:
      print("WARNING:  Add these Net name definitions:")
      for net in newNets:
        print('Net(\'' + net + '\')')

    print("Possible FEATURE:  May be good to change this function to enforce you to state pin number as well as name to ensure that mapping is correct or at least to see that mapping in the code")
    return part
