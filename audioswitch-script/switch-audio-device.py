import os
import sys


arg_map = {}
arg_map['0'] = 'Speakers'
arg_map['1'] = 'Headphones'
arg_map['2'] = 'TV'

batch_map = {}
batch_map['Speakers'] = 'Speakers.bat'
batch_map['Headphones'] = 'Headphones.bat'
batch_map['TV'] = 'TvSpeakers.bat'

toggle = {}
toggle['Speakers'] = 'Headphones'
toggle['Headphones'] = 'Speakers'
toggle['TV'] = 'Speakers'

current_audio_name_file = 'current-default-audio-device-name'
# nircmd = r'C:\Users\user\Documents\My Documents\Tools\NirCmd\nircmd.exe'
# command_format = '{0} setdefaultsounddevice "{1}" 1'


dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

def main():

    args = sys.argv.copy()
    args.pop(0)
    audio_name = None
    if len(args) > 0 :
        audio_name = arg_map[args[0]]
    else:
        audio_name = get_next_audio_name()

    if(audio_name):
        switch_audio(audio_name)
        set_current_audio_name(audio_name)


# def get_switch_command(audio_name):
#     return command_format.format(nircmd, audio_name)

def get_next_audio_name():
    with open(current_audio_name_file) as f:
        lines = f.readlines()
        current_audio_name = lines[0].strip()
        return toggle[current_audio_name]

def set_current_audio_name(audio_name):
    with open(current_audio_name_file, "w") as f:
        f.write(audio_name)

def switch_audio(audio_name):
    # command = get_switch_command(audio_name)
    # print(command)
    # os.system(command)
    batch_file = batch_map[audio_name]
    if(batch_file):
        os.system(batch_file)

main()