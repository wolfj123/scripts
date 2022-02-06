
If ProcessExist("explorer.exe")
	MsgBox 0 exists.

If ProcessExist("Notepad.exe")
	MsgBox 0 exists.

If ProcessExist("HuntGame.exe")
	MsgBox 1 exists.

If ProcessExist("InsurgencyClient-Win64-Shipping.exe")
	MsgBox 2 exists.

If ProcessExist("hl2.exe")
	MsgBox 3 exists.


If ProcessExist("Deathloop.exe")
	MsgBox 4 exists.
    

ProcessExist(Name){
	Process,Exist,%Name%
	return Errorlevel
}


^+F1::
    MsgBox boop
return