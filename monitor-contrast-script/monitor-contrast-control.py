from monitorcontrol import get_monitors
import re
import sys

# https://stackoverflow.com/questions/16588133/sending-ddc-ci-commands-to-monitor-on-windows-using-python
# https://github.com/newAM/monitorcontrol


VERBOSE = True
CONSTRAST_MAX = 100
CONSTRAST_MIN = 0
STEP_SIZE = 10

# VERBOSE = True
input_sources = ['DVI1' , 'ANALOG1']
input_name_pattern = re.compile(r'InputSource\.(.*)')

args = sys.argv.copy()
args.pop(0)
mode = int(args[0])
if mode == 0:
    mode = -1

for monitor in get_monitors():
    with monitor:
        try:
            current_input_source = input_name_pattern.search(str(monitor.get_input_source())).group(1)
            current_input_source_idx = input_sources.index(current_input_source)
            if(VERBOSE): print(current_input_source_idx)

            curr_constrast = monitor.get_contrast()
            if(VERBOSE): print(curr_constrast)

            delta = STEP_SIZE * mode
            new_contrast = curr_constrast + delta
            if(mode > 0):
                new_contrast = min(new_contrast, CONSTRAST_MAX)
            else:
                new_contrast = max(new_contrast, CONSTRAST_MIN)
            if(VERBOSE): print(new_contrast)
            
            monitor.set_contrast(new_contrast)

            
        except Exception as e: 
            if(VERBOSE): print(e)
            continue

