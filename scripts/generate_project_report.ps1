param([string]$RuntimeRoot, [switch]$SkipPreviews)
$ErrorActionPreference = 'Stop'
$projectRoot = Split-Path -Parent $PSScriptRoot
if (-not $RuntimeRoot) {
    $RuntimeRoot = Join-Path $env:USERPROFILE '.cache/codex-runtimes/codex-primary-runtime/dependencies'
}
$nodeBinary = Join-Path $RuntimeRoot 'node/bin/node.exe'
$bundledModules = Join-Path $RuntimeRoot 'node/node_modules'
if (-not (Test-Path -LiteralPath $nodeBinary) -or -not (Test-Path -LiteralPath (Join-Path $bundledModules '@oai/artifact-tool/package.json'))) {
    throw 'Brak srodowiska Node.js / artifact-tool. Wskaz -RuntimeRoot zgodnie z docs/project_reporting.md.'
}
$runtimeDirectory = Join-Path $projectRoot '.report_runtime'
New-Item -ItemType Directory -Force -Path $runtimeDirectory | Out-Null
$junction = Join-Path $runtimeDirectory 'node_modules'
if (-not (Test-Path -LiteralPath $junction)) {
    New-Item -ItemType Junction -Path $junction -Target $bundledModules | Out-Null
} else {
    $existing = Get-Item -LiteralPath $junction
    if ($existing.LinkType -ne 'Junction' -or [IO.Path]::GetFullPath([string]@($existing.Target)[0]) -ne [IO.Path]::GetFullPath($bundledModules)) {
        throw 'Istniejace dowiazanie zaleznosci wskazuje inne miejsce; nie zostalo zmienione.'
    }
}
$arguments = @((Join-Path $PSScriptRoot 'generate_project_report.mjs'))
if ($SkipPreviews) { $arguments += '--skip-previews' }
$reportPath = $null
& $nodeBinary @arguments | ForEach-Object {
    Write-Host $_
    if ($_ -like 'XLSX: *') { $reportPath = $_.Substring(6) }
}
if ($LASTEXITCODE -ne 0) { throw 'Generowanie raportu nie powiodlo sie; sprawdz komunikat powyzej.' }
if (-not $reportPath) { throw 'Generator nie zwrocil sciezki raportu.' }
$pythonBinary = Join-Path $RuntimeRoot 'python/python.exe'
& $pythonBinary (Join-Path $PSScriptRoot 'validate_project_report.py') $reportPath
if ($LASTEXITCODE -ne 0) { throw 'Raport nie przeszedl kontroli; nie traktuj go jako gotowego.' }
