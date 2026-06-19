@echo off
echo Mise a jour de la galerie photo...

where python >nul 2>nul
if %errorlevel%==0 (
    python "mise_a_jour_site.py"
) else (
    "C:\Users\User\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" "mise_a_jour_site.py"
)

echo.
echo Terminee. Les photos du dossier images\galerie sont maintenant integrees a galerie.html.
pause
