@echo off 
echo ?? QUANTUM ENTERPRISE PLATFORM 
echo ?? Starting Quantum Business Solutions... 
echo. 
start http://localhost:8000 
python -m http.server 8000 
pause 
