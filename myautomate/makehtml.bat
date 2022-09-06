@echo off
cd %~dp0
cmd /k ..\docs\make.bat html
pause