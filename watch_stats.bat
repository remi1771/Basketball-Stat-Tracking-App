@echo off
:loop
cls
type %1
timeout /t 2 >nul
goto loop