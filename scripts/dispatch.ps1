<#
  Local stopgap dispatcher.

  GitHub's scheduler is throttling this repo hard: in the first 16 hours it ran the
  5-minute watch 3 times instead of ~190, and the hourly brief twice instead of ~16.
  Runs landed hours apart, so the plan went stale and triggers were never checked.

  This script nudges the workflows from a machine that is actually awake. It is
  idempotent: it skips the watch when a run is already queued, and only dispatches
  the brief when the published plan is older than a threshold.

  Run once:   powershell -NoProfile -ExecutionPolicy Bypass -File scripts\dispatch.ps1
  Register:   schtasks /Create /TN "HL-ETH-Brief dispatcher" /SC MINUTE /MO 5 /F /TR "powershell -NoProfile -ExecutionPolicy Bypass -File C:\Users\hp\Toolbox\HL-ETH-Brief\scripts\dispatch.ps1"
  Remove:     schtasks /Delete /TN "HL-ETH-Brief dispatcher" /F
#>
param(
    [string]$Repo = "posu303-tech/hl-eth-brief",
    [string]$Site = "https://posu303-tech.github.io/hl-eth-brief/levels.json",
    [int]$BriefStaleMinutes = 60,
    [switch]$DryRun
)

$ErrorActionPreference = "Continue"

$logDir = Join-Path $env:LOCALAPPDATA "hl-eth-brief"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null
$logPath = Join-Path $logDir "dispatch.log"

function Write-Log([string]$Message) {
    $stamp = (Get-Date).ToUniversalTime().ToString("yyyy-MM-dd HH:mm:ss")
    Add-Content -Path $logPath -Value "$stamp UTC  $Message"
}

# keep the log bounded
if (Test-Path $logPath) {
    $lines = Get-Content $logPath
    if ($lines.Count -gt 5000) { $lines[-2000..-1] | Set-Content $logPath }
}

# --- watch: one queued/running run is enough ---------------------------------
try {
    $raw = & gh run list -R $Repo --workflow watch.yml --limit 10 --json status 2>&1
    if ($LASTEXITCODE -ne 0) { throw ($raw -join " ") }
    $runs = $raw | ConvertFrom-Json
    $pending = @($runs | Where-Object { $_.status -ne "completed" }).Count
} catch {
    Write-Log "cannot list runs ($_) - is gh authenticated?"
    exit 1
}

if ($pending -gt 0) {
    Write-Log "watch already pending ($pending); skip"
} elseif ($DryRun) {
    Write-Log "DRY: would dispatch watch.yml"
} else {
    & gh workflow run watch.yml -R $Repo 2>&1 | Out-Null
    if ($LASTEXITCODE -eq 0) { Write-Log "dispatched watch.yml" }
    else { Write-Log "failed to dispatch watch.yml (gh exit $LASTEXITCODE)" }
}

# --- brief: only when the published plan is going stale ----------------------
$ageMinutes = $null
try {
    $levels = Invoke-RestMethod -Uri ("{0}?t={1}" -f $Site, (Get-Random)) -TimeoutSec 20
    $asOf = [datetimeoffset]::FromUnixTimeMilliseconds([int64]$levels.as_of).UtcDateTime
    $ageMinutes = ((Get-Date).ToUniversalTime() - $asOf).TotalMinutes
} catch {
    Write-Log "cannot read published levels ($_)"
}

if ($null -eq $ageMinutes) {
    Write-Log "skip brief (unknown plan age)"
    exit 0
}

if ($ageMinutes -le $BriefStaleMinutes) {
    Write-Log ("brief fresh ({0:N0} min old); skip" -f $ageMinutes)
} elseif ($DryRun) {
    Write-Log ("DRY: would dispatch brief.yml (plan {0:N0} min old)" -f $ageMinutes)
} else {
    & gh workflow run brief.yml -R $Repo 2>&1 | Out-Null
    if ($LASTEXITCODE -eq 0) { Write-Log ("dispatched brief.yml (plan {0:N0} min old)" -f $ageMinutes) }
    else { Write-Log "failed to dispatch brief.yml (gh exit $LASTEXITCODE)" }
}
