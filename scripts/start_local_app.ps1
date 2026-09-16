param([int]$Port = 8787, [string]$PythonPath)
$ErrorActionPreference = 'Stop'
$projectRoot = Split-Path -Parent $PSScriptRoot
if (-not $PythonPath) {
    $localPython = Join-Path $projectRoot '.venv/Scripts/python.exe'
    $bundledPython = Join-Path $env:USERPROFILE '.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe'
    if (Test-Path -LiteralPath $localPython) { $PythonPath = $localPython }
    elseif (Test-Path -LiteralPath $bundledPython) { $PythonPath = $bundledPython }
    else { $PythonPath = (Get-Command python -ErrorAction Stop).Source }
}
& $PythonPath -X utf8 (Join-Path $projectRoot 'backend/local_app.py') --port $Port
if ($LASTEXITCODE -ne 0) { throw 'Nie udalo sie uruchomic aplikacji. Sprawdz, czy port jest wolny.' }
