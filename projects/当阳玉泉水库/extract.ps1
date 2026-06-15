$OutputEncoding = [Console]::OutputEncoding = [System.Text.Encoding]::UTF8
Add-Type -AssemblyName System.IO.Compression.FileSystem

$docxFiles = Get-ChildItem -Path $PSScriptRoot -Filter "*.docx"
if ($docxFiles.Count -eq 0) {
    Write-Host "No docx file found"
    exit
}
$zipPath = $docxFiles[0].FullName
$txtPath = Join-Path $PSScriptRoot "report_text.txt"

$zip = [System.IO.Compression.ZipFile]::OpenRead($zipPath)
$entry = $zip.Entries | Where-Object { $_.FullName -eq 'word/document.xml' }
$stream = $entry.Open()
$reader = New-Object System.IO.StreamReader($stream)
$xmlStr = $reader.ReadToEnd()
$reader.Close()
$zip.Dispose()

$xmlStr = $xmlStr -replace '</w:p>', "`n</w:p>"
$xmlStr = $xmlStr -replace '<[^>]+>', ''
$xmlStr | Out-File -FilePath $txtPath -Encoding UTF8
