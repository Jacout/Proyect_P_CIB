<#
.synopsis
Collect Hash and Filenames from specified folder

- User Specifies the target computer 
- User Specifies the target folder

The script will produce a simple ascii output file containing 
SHA-256Hash and FilePath

.Description
This script collects Hash and Filenames from specified computer and folder

.parameter TargetFolder
Folder where we are going to explore the files and get he hashes

.parameter ResultFile
File where all the hash and complete file names will be explored

.example

HashAcquire 
Collects the File Hashes on the target Computer
#>


# Parameter Definition Section
param(  
    [string]$TargetFolder="C:/Windows/System32/drivers/",
    [string]$ResultFile="baseline.txt"
)


Get-ChildItem $TargetFolder | Get-FileHash | Select-Object -Property Hash, Path | Format-Table -HideTableHeaders | Out-File $ResultFile -Encoding ascii

