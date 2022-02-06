
ForbiddenApps := ["HuntGame.exe", "InsurgencyClient-Win64-Shipping.exe", "hl2.exe", "Deathloop.exe"]

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