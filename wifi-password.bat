@echo off
title wifi-password
echo.
echo WIFI password
echo.
echo Masukkan Nama Wifi
set /p nama="> "
echo.
echo Runinng............
echo Runinng............
echo Runinng............
echo Runinng............
echo.
color 4
netsh wlan show profile %nama% key=clear
echo.
pause>nul
