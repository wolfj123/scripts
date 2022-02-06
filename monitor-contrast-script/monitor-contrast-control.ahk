
; CTRL + SHIFT + F7     :   decrease contrast
; CTRL + SHIFT + F8     :   increase contrast
; CTRL + SHIFT + F1     :   shutdown the script
; CTRL + SHIFT + F2     :   reload the script


^+F7::
    Run, pythonw.exe monitor-contrast-control.py 0,,Hide
return

^+F8::
    Run, pythonw.exe monitor-contrast-control.py 1,,Hide
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