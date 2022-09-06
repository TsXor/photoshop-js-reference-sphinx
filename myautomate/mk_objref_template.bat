@echo off
cd %~dp0

set /p n=name: 

mkdir "..\doc\source\JavaScript Object Reference\%n%"
mk_objref_template.py %n% > "..\doc\source\JavaScript Object Reference\%n%\intro.rst"
echo    %n%/intro.rst >> "..\doc\source\JavaScript Object Reference\index.rst"