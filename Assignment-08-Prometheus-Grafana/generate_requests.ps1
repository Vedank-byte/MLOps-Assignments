# Generate 50 prediction requests against the running API.
$uri = "http://127.0.0.1:8001/predict"
$body = '{"features":[5.1,3.5,1.4,0.2]}'
1..50 | ForEach-Object {
    Invoke-RestMethod -Uri $uri -Method POST -ContentType "application/json" -Body $body | Out-Null
}
Write-Host "Completed 50 prediction requests."
