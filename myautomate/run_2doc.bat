@echo off
cd %~dp0

echo run func
xl2doc_func curfunc.xlsx > func.txt
echo run prop
xl2doc_prop curprop.xlsx > prop.txt

pause