
ForbiddenApps := ["HuntGame.exe", "InsurgencyClient-Win64-Shipping.exe", "hl2.exe", "Deathloop.exe"] ;, "Notepad.exe"]

ScriptsDir := "C:\Users\user\Documents\My Documents\scripts\"
ScriptsToClose := ["audioswitch-script\switch-audio-device.ahk", "monitor-contrast-script\monitor-contrast-control.ahk", "monitor-switch-script\monitor-input-source-toggle.ahk"]
; ScriptsToClose = [C:\Users\user\Documents\My Documents\scripts\audioswitch-script\switch-audio-device.ahk]

; for testing use "Notepad.exe"

Loop {
    for index, element in ForbiddenApps {
        If ProcessExist(element) {
            ; MsgBox BOOM

            ExitSingleScript("C:\Users\user\Documents\My Documents\scripts\audioswitch-script\switch-audio-device.ahk")
            ExitSingleScript("C:\Users\user\Documents\My Documents\scripts\monitor-contrast-script\monitor-contrast-control.ahk")
            ExitSingleScript("C:\Users\user\Documents\My Documents\scripts\monitor-switch-script\monitor-input-source-toggle.ahk")
            ; ExitSingleScript()
            ; ExitScripts()
            ; ExitAHK()
            ExitApp
        }      
    }
    Sleep 1000
}

ProcessExist(Name){
	Process,Exist,%Name%
	return Errorlevel
}


ExitSingleScript(script) {
    DetectHiddenWindows, On 
    WinClose, %script% ahk_class AutoHotkey
}

; ExitSingleScript() {
;     fullScriptPath = C:\Users\user\Documents\My Documents\scripts\audioswitch-script\switch-audio-device.ahk  ; edit with your full script path
;     DetectHiddenWindows, On 
;     WinClose, %fullScriptPath% ahk_class AutoHotkey
; }


; ExitSingleScript() {
;     fullScriptPath = C:\Users\user\Documents\My Documents\scripts\audioswitch-script\switch-audio-device.ahk  ; edit with your full script path
;     DetectHiddenWindows, On 
;     WinClose, %fullScriptPath% ahk_class AutoHotkey
; }



; ExitScripts() {
;     for index, element in ScriptsToClose {
;         scriptPath = %ScriptsDir%%element%
;         DetectHiddenWindows, On 
;         WinClose, %scriptPath% ahk_class AutoHotkey  
;     }
;     ; ExitApp
; }

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