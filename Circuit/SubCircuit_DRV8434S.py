from skidl import *
from SKIDL_Helpers import *

lib_search_paths[KICAD].append('./TI_DRV8434S')

class SubCircuit_DRV8434S(SubCircuit):
    def __init__(self, name, PortConnections):
      #When creating your own subcircuit, replace this with actual ports on your sub circuit.
      Ports = (['VM',
                'AOUT1',
                'AOUT2',
                'BOUT1',
                'BOUT2',
                'GND',
                'VIO',
                'SCLK',
                'SDI',
                'SDO',
                'CS_n'])
      #Call the parent class with list of ports and net connections to those ports
      super().__init__(name, Ports, PortConnections)
      #Define the sub circuit
      self.DefineSubCircuit()


    #Modify this function for your desired sub circuit
    def DefineSubCircuit(self):
      VD     = self.CreateNet('+5VD', drive=POWER)
      NFAULT = self.CreateNet('NFAULT')
      VREF   = self.CreateNet('VREF')
      CPL    = self.CreateNet('CPL', drive=POWER)
      CPH    = self.CreateNet('CPH', drive=POWER)
      VCP    = self.CreateNet('VCP', drive=POWER)
      
      InstantiatePart(
      Part("TI_DRV8434S", "DRV8434SRGER", footprint="StepperLibrary:DRV8434SRGER"),
        {   'VM'      : self.PortConnections['VM'],
            'AOUT1'   : self.PortConnections['AOUT1'],
            'AOUT2'   : self.PortConnections['AOUT2'],
            'BOUT2'   : self.PortConnections['BOUT2'],
            'BOUT1'   : self.PortConnections['BOUT1'],
            'PAD'     : self.PortConnections['GND'],
            'GND'     : self.PortConnections['GND'],
            'PGND'    : self.PortConnections['GND'],
            'DVDD'    : VD,
            'NFAULT'  : NFAULT,
            'VREF'    : VREF,
            'NSCS'    : self.PortConnections['CS_n'],
            'SDO'     : self.PortConnections['SDO'],
            'SDI'     : self.PortConnections['SDI'],
            'SCLK'    : self.PortConnections['SCLK'],
            'STEP'    : self.PortConnections['GND'],
            'DIR'     : self.PortConnections['GND'],
            'ENABLE'  : self.PortConnections['VIO'],
            'VSDO'    : self.PortConnections['VIO'],
            'NSLEEP'  : self.PortConnections['VIO'],
            'CPL'     : CPL,
            'CPH'     : CPH,
            'VCP'     : VCP
        }
      )

      #decouple VM pin
      C('0402', '0.1uF', VCP, self.PortConnections['VM'])

      #Add external charge pump capacitor
      C('0402', '0.1uF', CPH, CPL)

      #Decouple VIO pin
      C('0402', '0.1uF', self.PortConnections['GND'], self.PortConnections['VIO']) #one cap for VSDO pin
      C('0402', '0.1uF', self.PortConnections['GND'], self.PortConnections['VIO']) #one cap for ENABLE and NSLEEP pins that are close to each other.

      #Pull up for open drain FAULT pin
      R('0402', '10k', NFAULT, VD)

      #Voltage divider and decoupling for VREF pin
      R('0402', '10k', VREF, VD)
      R('0402', '10k', VREF, self.PortConnections['GND'])
      C('0402', '0.1uF', self.PortConnections['GND'], VREF)



              
