
; CTRL + SHIFT + F12     :   toggle monitor input between DVI and ANALOG
; CTRL + SHIFT + F1     :   shutdown the script
; CTRL + SHIFT + F2     :   reload the script


^+F12::
    Run, pythonw.exe monitor-input-source-toggle.py ,,Hide
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