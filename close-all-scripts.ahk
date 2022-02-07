
ForbiddenApps := ["HuntGame.exe", "InsurgencyClient-Win64-Shipping.exe", "hl2.exe", "Deathloop.exe"]

ScriptsDire := "C:\Users\user\Documents\My Documents\scripts\"
ScriptsToClose := ["audioswitch-script\switch-audio-device.ahk", "monitor-contrast-script\monitor-contrast-control.ahk", "monitor-switch-script\monitor-input-source-toggle.ahk"]


; for testing use "Notepad.exe"

Loop {
    for index, element in ForbiddenApps {
        If ProcessExist(element) {
            ; MsgBox BOOM
            ExitAHK()
            ; ExitApp
        }      
    }
    Sleep 1000
}

ProcessExist(Name){
	Process,Exist,%Name%
	return Errorlevel
}


ExitScripts() {
    for index, element in ScriptsToClose {
        scriptPath = %ScriptsDire%%element%
        DetectHiddenWindows, On 
        WinClose, %scriptPath% ahk_class AutoHotkey  
    }
    ExitApp
}

; Doesnt work as intended
ExitAHK(){
	Loop {
        Process, Close, Autohotkey.exe
        If (ErrorLevel = 0)
        Break     ;No [more] matching processes found
    }
}

^+F1::
    ExitApp  ; Assign a hotkey to terminate this script.
return