from skidl import *
from SKIDL_Helpers import *

lib_search_paths[KICAD].append('./TI_DRV8434S')

# Create NETs
Net('VM')
Net('AOUT1')
Net('AOUT2')
Net('BOUT1')
Net('BOUT2')
Net('GND')
Net('+5VD')
Net('NFAULT')
Net('VREF')
Net('VDD')
Net('POWER')
Net('SCLK')
Net('SDI')
Net('SDO')
Net('CS_n')


LeftConnector = Part("Connector_Generic", "Conn_01x09", footprint="Connector_PinSocket_2.54mm:PinSocket_1x09_P2.54mm_Vertical")
RightConnector = Part("Connector_Generic", "Conn_01x09", footprint="Connector_PinSocket_2.54mm:PinSocket_1x09_P2.54mm_Vertical")

StepperDriver = Part("TI_DRV8434S", "DRV8434SRGER", footprint="StepperLibrary:DRV8434SRGER")

#Hook up pins of Stepper Driver to local passives
StepperDriver['VM'] += Net.get('VM')
StepperDriver['AOUT1'] += Net.get('AOUT1')
StepperDriver['AOUT2'] += Net.get('AOUT2')
StepperDriver['BOUT1'] += Net.get('BOUT1')
StepperDriver['BOUT2'] += Net.get('BOUT2')
StepperDriver['GND'] += Net.get('GND')
StepperDriver['PGND'] += Net.get('GND')
StepperDriver['PAD'] += Net.get('GND')
StepperDriver['VCP'] & addPassive('C', '0402', '0.1uF') & StepperDriver['VM']
StepperDriver['CPH'] & addPassive('C', '0402', '0.1uF') & StepperDriver['CPL']
StepperDriver['NSLEEP'] += Net.get('VDD')
StepperDriver['ENABLE'] += Net.get('VDD')
StepperDriver['VSDO'] += Net.get('VDD')
addBypassCaps([['0402', '0.1uF'],
               ['0402', '0.1uF']], 
              'GND', 'VDD')

StepperDriver['DIR'] += Net.get('GND')
StepperDriver['STEP'] += Net.get('GND')
StepperDriver['SCLK'] += Net.get('SCLK')
StepperDriver['SDI'] += Net.get('SDI')
StepperDriver['SDO'] += Net.get('SDO')
StepperDriver['NSCS'] += Net.get('CS_n')
StepperDriver['NFAULT'] += Net.get('NFAULT')
addPull('0402', '10k', 'NFAULT', '+5VD')

StepperDriver['VREF'] += Net.get('VREF')
StepperDriver['DVDD'] += Net.get('+5VD')
addPull     ('0402', '10k', 'VREF', '+5VD')
addPull     ('0402', '10k', 'VREF', 'GND')
addBypassCap('0402', '0.1uF', 'GND', 'VREF')


#Hook up pins of Stepper Driver externally
LeftConnector[1] += Net.get('GND')
LeftConnector[2] += Net.get('BOUT1')
LeftConnector[3] += Net.get('BOUT2')
LeftConnector[4] += Net.get('AOUT2')
LeftConnector[5] += Net.get('AOUT1')
LeftConnector[6] += Net.get('GND')
LeftConnector[7] += Net.get('POWER')
LeftConnector[8] += Net.get('POWER')
LeftConnector[9] += Net.get('GND')

RightConnector[1] += Net.get('VDD')
RightConnector[2] += Net.get('GND')
RightConnector[3] += Net.get('SCLK')
RightConnector[4] += Net.get('GND')
RightConnector[5] += Net.get('SDI')
RightConnector[6] += Net.get('GND')
RightConnector[7] += Net.get('SDO')
RightConnector[8] += Net.get('GND')
RightConnector[9] += Net.get('CS_n')
# Connect the nets and resistors.


# Or you could do it with a single line of code:
# vin && r1 && vout && r2 && gnd

# Output the netlist to a file.
generate_netlist()
ERC()
