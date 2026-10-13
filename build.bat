@echo off
rem Tek dosyalik tasinabilir exe uretir: dist\SVG-Varyant-Uretici.exe
python -m pip install --upgrade pyinstaller openpyxl || exit /b 1
python -m PyInstaller --noconfirm --clean --onefile --windowed --exclude-module numpy --exclude-module pandas --exclude-module PIL --exclude-module lxml --exclude-module matplotlib --exclude-module scipy --name SVG-Varyant-Uretici svg_varyant.pyw || exit /b 1
echo.
echo Hazir: dist\SVG-Varyant-Uretici.exe
