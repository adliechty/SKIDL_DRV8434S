from skidl import *
from SKIDL_Helpers import *
from SubCircuit_DRV8434S import *

lib_search_paths[KICAD].append('./TI_DRV8434S')

#Start of Auto Generated Net Names (not auto generated at moment, but suggested from SubCircuit definitions
Net('GND', drive=POWER)
Net('VM',  drive=POWER)
Net('VIO', drive=POWER)

Net('CS_n')
Net('SDI')
Net('SCLK')
#End of Auto Generated Net Names (not auto generated at moment, but suggested from SubCircuit definitions

SDI = 'SDI'
#loop from 1 to 4
kNumCircuits = 4
for i in range(1, kNumCircuits + 1):
  #First define output nets for Stepper coils
  Net('AOUT1_' + str(i))
  Net('AOUT2_' + str(i))
  Net('BOUT2_' + str(i))
  Net('BOUT1_' + str(i))

  SDO = 'SDO_' + str(i)
  #Connect last SDO to connector NET
  if i == kNumCircuits:
    SDO = 'SDO'
  Net(SDO)

  SubCircuit_DRV8434S('Driver' + str(i),
        {   'VM'      : 'VM',
            'AOUT1'   : 'AOUT1_' + str(i),
            'AOUT2'   : 'AOUT2_' + str(i),
            'BOUT2'   : 'BOUT2_' + str(i),
            'BOUT1'   : 'BOUT1_' + str(i),
            'GND'     : 'GND',
            'CS_n'    : 'CS_n',
            'SDO'     : SDO,
            'SDI'     : SDI,
            'SCLK'    : 'SCLK',
            'VIO'     : 'VIO'
        }
      )
  #Connect next SDI to previous SDO
  SDI = SDO

InstantiatePart(
        Part("Connector_Generic", "Conn_01x16", footprint="Connector_PinSocket_2.54mm:PinSocket_1x16_P2.54mm_Vertical"),
          {
            'Pin_1'  : 'BOUT1_1',
            'Pin_2'  : 'BOUT2_1',
            'Pin_3'  : 'AOUT2_1',
            'Pin_4'  : 'AOUT1_1',
            'Pin_5'  : 'BOUT1_2',
            'Pin_6'  : 'BOUT2_2',
            'Pin_7'  : 'AOUT2_2',
            'Pin_8'  : 'AOUT1_2',
            'Pin_9'  : 'BOUT1_3',
            'Pin_10' : 'BOUT2_3',
            'Pin_11' : 'AOUT2_3',
            'Pin_12' : 'AOUT1_3',
            'Pin_13' : 'BOUT1_4',
            'Pin_14' : 'BOUT2_4',
            'Pin_15' : 'AOUT2_4',
            'Pin_16' : 'AOUT1_4',
          }
        )

InstantiatePart(
        Part("Connector_Generic", "Conn_01x16", footprint="Connector_PinSocket_2.54mm:PinSocket_1x16_P2.54mm_Vertical"),
          {
            'Pin_1'  : 'VIO',
            'Pin_2'  : 'GND',
            'Pin_3'  : 'SCLK',
            'Pin_4'  : 'GND',
            'Pin_5'  : 'SDI',
            'Pin_6'  : 'GND',
            'Pin_7'  : 'SDO',
            'Pin_8'  : 'CS_n',
            'Pin_9'  : 'GND',
            'Pin_10' : 'GND',
            'Pin_11' : 'GND',
            'Pin_12' : 'GND',
            'Pin_13' : 'VM',
            'Pin_14' : 'VM',
            'Pin_15' : 'VM',
            'Pin_16' : 'VM'
          }
        )

# Output the netlist to a file.
generate_netlist()
ERC()
