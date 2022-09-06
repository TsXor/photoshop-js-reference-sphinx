@echo off
cd %~dp0
cmd /k ..\doc\make.bat html
pause