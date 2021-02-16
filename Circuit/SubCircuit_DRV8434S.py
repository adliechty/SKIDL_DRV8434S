from skidl import *
from SKIDL_Helpers import *

lib_search_paths[KICAD].append('./TI_DRV8434S')

class SubCircuit_DRV8434S:
    def __init__(self, name, pinsToNets):
      self.name = name
      self.DefineRequiredPins()
      self.pinsToNets = pinsToNets
      self.CheckAllPinsAssigned()
      self.DefineSubCircuit()

    #Modify this to define pins of the sub circuit
    def DefineRequiredPins(self):
      print("InDefineRequiredPins")
      self.requiredPins = ['VM',
                   'AOUT1',
                   'AOUT2',
                   'BOUT1',
                   'BOUT2',
                   'GND',
                   'VIO',
                   'SCLK',
                   'SDI',
                   'SDO',
                   'CS_n'
                   ]

    #Modify this function for your desired sub circuit
    def DefineSubCircuit(self):
      VD     = self.CreateNet('+5VD')
      NFAULT = self.CreateNet('NFAULT')
      VREF   = self.CreateNet('VREF')
      CPL    = self.CreateNet('CPL')
      CPH    = self.CreateNet('CPH')
      VCP    = self.CreateNet('VCP')
      
      InstantiatePart(
      Part("TI_DRV8434S", "DRV8434SRGER", footprint="StepperLibrary:DRV8434SRGER"),
        {   'VM'      : self.pinsToNets['VM'],
            'AOUT1'   : self.pinsToNets['AOUT1'],
            'AOUT2'   : self.pinsToNets['AOUT2'],
            'BOUT2'   : self.pinsToNets['BOUT2'],
            'BOUT1'   : self.pinsToNets['BOUT1'],
            'PAD'     : self.pinsToNets['GND'],
            'GND'     : self.pinsToNets['GND'],
            'PGND'    : self.pinsToNets['GND'],
            'DVDD'    : VD,
            'NFAULT'  : NFAULT,
            'VREF'    : VREF,
            'NSCS'    : self.pinsToNets['CS_n'],
            'SDO'     : self.pinsToNets['SDO'],
            'SDI'     : self.pinsToNets['SDI'],
            'SCLK'    : self.pinsToNets['SCLK'],
            'STEP'    : self.pinsToNets['GND'],
            'DIR'     : self.pinsToNets['GND'],
            'ENABLE'  : self.pinsToNets['VIO'],
            'VSDO'    : self.pinsToNets['VIO'],
            'NSLEEP'  : self.pinsToNets['VIO'],
            'CPL'     : CPL,
            'CPH'     : CPH,
            'VCP'     : VCP
        }
      )

      #decouple VM pin
      C('0402', '0.1uF', VCP, self.pinsToNets['VM'])

      #Add external charge pump capacitor
      C('0402', '0.1uF', CPH, CPL)

      #Decouple VIO pin
      C('0402', '0.1uF', self.pinsToNets['GND'], self.pinsToNets['VIO']) #one cap for VSDO pin
      C('0402', '0.1uF', self.pinsToNets['GND'], self.pinsToNets['VIO']) #one cap for ENABLE and NSLEEP pins that are close to each other.

      #Pull up for open drain FAULT pin
      R('0402', '10k', NFAULT, VD)

      #Voltage divider and decoupling for VREF pin
      R('0402', '10k', VREF, VD)
      R('0402', '10k', VREF, self.pinsToNets['GND'])
      C('0402', '0.1uF', self.pinsToNets['GND'], VREF)

    def CreateNet(self, NetName):
      Net(self.name + "_" + NetName)
      return self.name + "_" + NetName
    def GetNetName(self, NetName):
      return self.name + "_" + NetName

    #Random helper functions.  No need to modify these
    def CheckAllPinsAssigned(self):
      missingPinToNetMappings = []
      for pin in self.requiredPins:
        if pin not in self.pinsToNets:
          missingPinToNetMappings.append(pin)

      if missingPinToNetMappings:
        maxStrLength = max(len(x) for x in missingPinToNetMappings) 
        print("WARNING:  Add these mapings to the part instantiation, if mapping is 1:1 with pin name to net name:")
        for pin in missingPinToNetMappings:
          print('    \'' + pin + '\'' + ' ' * (maxStrLength - len(pin) + 1) + ': \'' + pin + '\',')

              
