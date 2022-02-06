
; CTRL + SHIFT + F9     :   switch audio output to speakers
; CTRL + SHIFT + F10    :   switch audio output to headphones
; CTRL + SHIFT + F11    :   toggle audio output
; CTRL + SHIFT + F1     :   shutdown the script
; CTRL + SHIFT + F2     :   reload the script


^+F9::
    Run, pythonw.exe switch-audio-device.py 0 ,,Hide
    ; run dist\switch-audio-device.exe
return

^+F10::
    Run, pythonw.exe switch-audio-device.py 1 ,,Hide
    ; run dist\switch-audio-device.exe
return

^+F11::
    Run, pythonw.exe switch-audio-device.py ,,Hide
    ; run dist\switch-audio-device.exe
return

^+F1::
    ExitApp  ; Assign a hotkey to terminate this script.
return


^+F2::
    Reload  ; reload script
return



ProcessExist(Name){
	Process,Exist,%Name%
	return Errorlevel
}