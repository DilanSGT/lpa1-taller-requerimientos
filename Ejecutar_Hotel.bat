@echo off
title Sistema de Reservas de Hotel
echo.
echo ====================================
echo   SISTEMA DE RESERVAS DE HOTEL
echo ====================================
echo.
echo Iniciando aplicacion...
echo.
cd /d "%~dp0dist"
if exist Hotel_Reservations.exe (
    Hotel_Reservations.exe
) else (
    echo ERROR: No se encontro Hotel_Reservations.exe
    echo.
    echo Verifica que el archivo este en la carpeta dist/
    pause
)
