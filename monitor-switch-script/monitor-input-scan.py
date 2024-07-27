from monitorcontrol import get_monitors


for monitor in get_monitors():
    with monitor:
        print(monitor)
        print(monitor.get_input_source())
        print(monitor.get_contrast())
        print(monitor.get_luminance())

