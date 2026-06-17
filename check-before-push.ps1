# UseCalcFi — Pre-push verification script
# Run: powershell -File check-before-push.ps1
# Purpose: Catch truncated HTML files before they get deployed

$dir = Split-Path -Parent $MyInvocation.MyCommand.Path
$files = Get-ChildItem "$dir\*.html"
$errors = 0

Write-Host "`n=== UseCalcFi Pre-Push Check ===" -ForegroundColor Cyan

foreach ($f in $files) {
    $content = Get-Content $f.FullName -Raw -Encoding UTF8
    $lines = (Get-Content $f.FullName).Count

    # Check ends with </html>
    if ($content.TrimEnd() -notmatch '</html>\s*$') {
        Write-Host "TRUNCATED: $($f.Name) ($lines lines)" -ForegroundColor Red
        $errors++
    }
    # Check has <title>
    elseif ($content -notmatch '<title>') {
        Write-Host "MISSING TITLE: $($f.Name)" -ForegroundColor Yellow
        $errors++
    }
    else {
        Write-Host "OK  $($f.Name) ($lines lines)" -ForegroundColor Green
    }
}

Write-Host ""
if ($errors -gt 0) {
    Write-Host "$errors file(s) have issues — DO NOT PUSH until fixed!" -ForegroundColor Red
    exit 1
} else {
    Write-Host "All $($files.Count) files look good. Safe to push!" -ForegroundColor Green
    Write-Host "Run: git add -A" -ForegroundColor Cyan
    Write-Host 'Run: git commit -m "your message"' -ForegroundColor Cyan
    Write-Host "Run: git push" -ForegroundColor Cyan
}
