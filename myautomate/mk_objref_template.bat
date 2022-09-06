@echo off
cd %~dp0

set /p n=name: 

mkdir "..\docs\source\JavaScript Object Reference\%n%"
mk_objref_template.py %n% > "..\docs\source\JavaScript Object Reference\%n%\intro.rst"
echo    %n%/intro.rst >> "..\docs\source\JavaScript Object Reference\index.rst"