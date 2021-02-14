from skidl import *
from SKIDL_Helpers import *

lib_search_paths[KICAD].append('./TI_DRV8434S')

#Auto Generated Net Names
Net('VM')
Net('+5VD')
Net('NFAULT')
Net('VREF')
Net('CS_n')
Net('VDD')
Net('SDO')
Net('SDI')
Net('SCLK')
Net('GND')
Net('CPL')
Net('CPH')
Net('VCP')
Net('AOUT1')
Net('AOUT2')
Net('BOUT2')
Net('BOUT1')
#End auto Generated Net Names

StepperDriver = InstantiatePart(
        Part("TI_DRV8434S", "DRV8434SRGER", footprint="StepperLibrary:DRV8434SRGER"),
        {   'VM'      : 'VM',
            'AOUT1'   : 'AOUT1',
            'AOUT2'   : 'AOUT2',
            'BOUT2'   : 'BOUT2',
            'BOUT1'   : 'BOUT1',
            'PAD'     : 'GND',
            'GND'     : 'GND',
            'PGND'    : 'GND',
            'DVDD'    : '+5VD',
            'NFAULT'  : 'NFAULT',
            'VREF'    : 'VREF',
            'NSCS'    : 'CS_n',
            'SDO'     : 'SDO',
            'SDI'     : 'SDI',
            'SCLK'    : 'SCLK',
            'STEP'    : 'GND',
            'DIR'     : 'GND',
            'ENABLE'  : 'VDD',
            'VSDO'    : 'VDD',
            'NSLEEP'  : 'VDD',
            'CPL'     : 'CPL',
            'CPH'     : 'CPH',
            'VCP'     : 'VCP'
        }
      )

addBypassCap('0402', '0.1uF', 'VCP', 'VM')
addBypassCap('0402', '0.1uF', 'CPH', 'CPL')
addBypassCaps([['0402', '0.1uF'],
               ['0402', '0.1uF']], 
              'GND', 'VDD')

addPull('0402', '10k', 'NFAULT', '+5VD')
addPull     ('0402', '10k', 'VREF', '+5VD')
addPull     ('0402', '10k', 'VREF', 'GND')
addBypassCap('0402', '0.1uF', 'GND', 'VREF')

LeftConnector = InstantiatePart(
        Part("Connector_Generic", "Conn_01x09", footprint="Connector_PinSocket_2.54mm:PinSocket_1x09_P2.54mm_Vertical"),
          {
            'Pin_1' : 'GND',
            'Pin_2' : 'BOUT1',
            'Pin_3' : 'BOUT2',
            'Pin_4' : 'AOUT2',
            'Pin_5' : 'AOUT1',
            'Pin_6' : 'GND',
            'Pin_7' : 'VM',
            'Pin_8' : 'VM',
            'Pin_9' : 'GND',
          }
        )

RighConnector = InstantiatePart(
        Part("Connector_Generic", "Conn_01x09", footprint="Connector_PinSocket_2.54mm:PinSocket_1x09_P2.54mm_Vertical"),
          {
            'Pin_1' : 'VDD',
            'Pin_2' : 'GND',
            'Pin_3' : 'SCLK',
            'Pin_4' : 'GND',
            'Pin_5' : 'SDI',
            'Pin_6' : 'GND',
            'Pin_7' : 'SDO',
            'Pin_8' : 'GND',
            'Pin_9' : 'CS_n',
          }
        )

# Or you could do it with a single line of code:
# vin && r1 && vout && r2 && gnd

# Output the netlist to a file.
generate_netlist()
ERC()
