from monitorcontrol import get_monitors
import re

# https://stackoverflow.com/questions/16588133/sending-ddc-ci-commands-to-monitor-on-windows-using-python
# https://github.com/newAM/monitorcontrol


# VERBOSE = False
VERBOSE = True
# input_sources = ['DVI1' , 'ANALOG1']
# input_sources = ['DVI1' , 'DVI2']
#dont know why but for some reason from DV1 we need to jump to HDMI1 and then from HDMI1 we need to jump to DVI2
input_sources = [{'from':'DP1' , 'to':'HDMI1'},{'from':'HDMI1' , 'to':'DP1'}]
input_name_pattern = re.compile(r'InputSource\.(.*)')

main_monitor_input_source = 'InputSource.DP1'
for monitor in get_monitors():
    with monitor:
        try:
            # print(str(monitor.get_input_source()))
            val = input_name_pattern.search(str(monitor.get_input_source())).group(1)
            if(VERBOSE): print(val)
            # idx = input_sources.index(val)
            # size = len(input_sources)
            # next_idx = (idx + 1) % size
            next_input = next((x for x in input_sources if x['from'] == val), None)['to']
            if(VERBOSE): print(next_input)
            monitor.set_input_source(next_input)
        except Exception as e: 
            if(VERBOSE): print(e)
            continue




