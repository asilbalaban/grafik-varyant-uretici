@echo off
rem Tek dosyalik tasinabilir exe uretir: dist\Grafik-Varyant-Uretici.exe
python -m pip install --upgrade pyinstaller -r requirements.txt || exit /b 1
python -m PyInstaller --noconfirm --clean --onefile --windowed --icon assets\app.ico --add-data "assets\app.ico;assets" --exclude-module numpy --exclude-module pandas --exclude-module PIL --exclude-module lxml --exclude-module matplotlib --exclude-module scipy --name Grafik-Varyant-Uretici grafik_varyant.pyw || exit /b 1
echo.
echo Hazir: dist\Grafik-Varyant-Uretici.exe
