# Script to search for a specified file pattern in all S3 buckets,
# excluding specified buckets.

# Check if a search string is provided
param(
    [string]$SearchString
)

if (-not $SearchString) {
    Write-Host "Usage: $PSCommandPath <search-string>"
    exit
}

# Enumerate all S3 buckets
$buckets = aws s3 ls | ForEach-Object {
    $_.Split(' ')[2]
}

foreach ($bucket in $buckets) {
    # Check if the bucket name matches any of the exclusion patterns
    if ($bucket -notmatch "cloudtrail" -and $bucket -notmatch "logs" -and $bucket -notmatch "backup") {
        Write-Host "Searching in bucket: $bucket"
        aws s3 ls "s3://$bucket/" --recursive --human-readable | Select-String $SearchString
    } else {
        Write-Host "Skipping excluded bucket: $bucket"
    }
}
