cd %~dp0

copy /Y newxl.xlsx curfunc.xlsx
copy /Y newxl.xlsx curprop.xlsx
del /s func.txt
del /s prop.txt

pause