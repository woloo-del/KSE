param([string]$Config = 'config/research_probes.json')
$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
$targets = Get-Content -LiteralPath (Join-Path $root $Config) -Raw | ConvertFrom-Json
$results = @()
foreach ($target in $targets) {
    $record = [ordered]@{source_id=$target.source_id; url=$target.url; retrieval_date=(Get-Date).ToUniversalTime().ToString('o'); http_status=$null; content_type=$null; bytes=$null; sha256=$null; local_path=$null; error=$null}
    try {
        $response = Invoke-WebRequest -Uri $target.url -TimeoutSec 25 -MaximumRedirection 5
        $record.http_status = [int]$response.StatusCode
        $record.content_type = [string]$response.Headers['Content-Type']
        $bytes = $response.RawContentStream.ToArray()
        $record.bytes = $bytes.Length
        if ($target.save_as) {
            $destination = Join-Path $root ('data/raw/research/2026-09-10/' + $target.save_as)
            if (Test-Path -LiteralPath $destination) { throw 'Existing snapshot preserved; choose a new name.' }
            [System.IO.File]::WriteAllBytes($destination, $bytes)
            $record.sha256 = (Get-FileHash -LiteralPath $destination -Algorithm SHA256).Hash.ToLowerInvariant()
            $record.local_path = 'data/raw/research/2026-09-10/' + $target.save_as
        }
    } catch {
        $record.error = $_.Exception.GetType().Name
        if ($_.Exception.Response) { $record.http_status = [int]$_.Exception.Response.StatusCode }
    }
    $results += [pscustomobject]$record
    Write-Output ($record.source_id + ': HTTP ' + $record.http_status + ', bytes ' + $record.bytes + ', error ' + $record.error)
}
$stamp = (Get-Date).ToUniversalTime().ToString('yyyyMMddTHHmmssfffZ')
$results | ConvertTo-Json -Depth 6 | Set-Content -LiteralPath (Join-Path $root ('data/catalog/probe_results_' + $stamp + '.json')) -Encoding utf8
