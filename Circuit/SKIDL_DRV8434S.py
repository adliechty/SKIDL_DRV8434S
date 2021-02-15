from skidl import *
from SKIDL_Helpers import *
from SubCircuit_DRV8434S import *

lib_search_paths[KICAD].append('./TI_DRV8434S')

#Auto Generated Net Names (not auto generated at moment, but suggested from SubCircuit definitions
Net('GND')
Net('VM')
Net('VIO')

Net('CS_n')
Net('SDO')
Net('SDO_1')
Net('SDI')
Net('SCLK')

Net('AOUT1_1')
Net('AOUT2_1')
Net('BOUT2_1')
Net('BOUT1_1')

Net('AOUT1_2')
Net('AOUT2_2')
Net('BOUT2_2')
Net('BOUT1_2')
#Auto Generated Net Names (not auto generated at moment, but suggested from SubCircuit definitions

SubCircuit_DRV8434S('Driver1',
        {   'VM'      : 'VM',
            'AOUT1'   : 'AOUT1_1',
            'AOUT2'   : 'AOUT2_1',
            'BOUT2'   : 'BOUT2_1',
            'BOUT1'   : 'BOUT1_1',
            'GND'     : 'GND',
            'CS_n'    : 'CS_n',
            'SDO'     : 'SDO_1',
            'SDI'     : 'SDI',
            'SCLK'    : 'SCLK',
            'VIO'     : 'VIO'
        }
      )

SubCircuit_DRV8434S('Driver2',
        {   'VM'      : 'VM',
            'AOUT1'   : 'AOUT1_2',
            'AOUT2'   : 'AOUT2_2',
            'BOUT2'   : 'BOUT2_2',
            'BOUT1'   : 'BOUT1_2',
            'GND'     : 'GND',
            'CS_n'    : 'CS_n',
            'SDO'     : 'SDO',
            'SDI'     : 'SDO_1',
            'SCLK'    : 'SCLK',
            'VIO'     : 'VIO'
        }
      )

InstantiatePart(
        Part("Connector_Generic", "Conn_01x14", footprint="Connector_PinSocket_2.54mm:PinSocket_1x14_P2.54mm_Vertical"),
          {
            'Pin_1'  : 'GND',
            'Pin_2'  : 'BOUT1_1',
            'Pin_3'  : 'BOUT2_1',
            'Pin_4'  : 'AOUT2_1',
            'Pin_5'  : 'AOUT1_1',
            'Pin_6'  : 'GND',
            'Pin_7'  : 'BOUT1_2',
            'Pin_8'  : 'BOUT2_2',
            'Pin_9'  : 'AOUT2_2',
            'Pin_10' : 'AOUT1_2',
            'Pin_11' : 'GND',
            'Pin_12' : 'VM',
            'Pin_13' : 'VM',
            'Pin_14' : 'GND',
          }
        )

InstantiatePart(
        Part("Connector_Generic", "Conn_01x09", footprint="Connector_PinSocket_2.54mm:PinSocket_1x09_P2.54mm_Vertical"),
          {
            'Pin_1' : 'VIO',
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

# Output the netlist to a file.
generate_netlist()
ERC()
