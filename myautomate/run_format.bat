@echo off
cd %~dp0

echo run func
xlformat_func curfunc.xlsx
echo run prop
xlformat_prop curprop.xlsx

pause