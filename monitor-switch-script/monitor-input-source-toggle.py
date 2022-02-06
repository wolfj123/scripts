from monitorcontrol import get_monitors
import re

# https://stackoverflow.com/questions/16588133/sending-ddc-ci-commands-to-monitor-on-windows-using-python
# https://github.com/newAM/monitorcontrol


VERBOSE = False
# VERBOSE = True
input_sources = ['DVI1' , 'ANALOG1']
input_name_pattern = re.compile(r'InputSource\.(.*)')

main_monitor_input_source = 'InputSource.DVI1'
for monitor in get_monitors():
    with monitor:
        try:
            val = input_name_pattern.search(str(monitor.get_input_source())).group(1)
            idx = input_sources.index(val)
            if(VERBOSE): print(val)
            size = len(input_sources)
            next_idx = (idx + 1) % size
            if(VERBOSE): print(input_sources[next_idx])
            monitor.set_input_source(input_sources[next_idx])
        except Exception as e: 
            if(VERBOSE): print(e)
            continue





# for monitor in get_monitors():
#     with monitor:
#         print(monitor)


# for monitor in get_monitors():
#     with monitor:
#         print(monitor.get_input_source())



# for monitor in get_monitors():
#     with monitor:
#         print(monitor.get_contrast())


# for monitor in get_monitors():
#     with monitor:
#         print(monitor.get_luminance())

