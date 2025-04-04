# create.ps1 - Creates a file with a padded 4-digit name from input
param([string]$filename)

if ($filename -match '^[0-9]+$') {
    $parsed = [int]::Parse($filename)
    $padded = $parsed.ToString("D4") + ".py"
    Copy-Item template.py $padded
} else {
    Write-Output "Error: Please provide a valid integer filename."
}
