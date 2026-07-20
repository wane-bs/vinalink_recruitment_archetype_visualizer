# Script đăng ký tác vụ tự động chạy fetch-feedback.py lúc 20:00 hàng ngày trên Windows

$taskName = "Sihub_Vinalink_Sync_Task"
$scriptPath = "d:\DebianBackup\source_code\lop_sihub\03-Projects\vinalink\visualizer_deploy\fetch-feedback.py"
$pythonPath = (Get-Command python.exe -ErrorAction SilentlyContinue).Source

if (-not $pythonPath) {
    # Thử tìm python từ Registry hoặc đường dẫn mặc định nếu không thấy trên PATH
    $pythonPath = "python"
}

Write-Host "Đường dẫn Python: $pythonPath"
Write-Host "Đường dẫn Script: $scriptPath"

# Cấu hình Trigger: Hàng ngày lúc 20:00 (8:00 PM)
$trigger = New-ScheduledTaskTrigger -Daily -At 8:00PM

# Cấu hình Action: Chạy Python thực thi script
$action = New-ScheduledTaskAction -Execute $pythonPath -Argument "`"$scriptPath`""

# Cấu hình Settings: Chạy ngay cả khi máy dùng pin, cho phép chạy bù nếu bị lỡ lịch, v.v.
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable

# Đăng ký tác vụ
Register-ScheduledTask -TaskName $taskName -Trigger $trigger -Action $action -Settings $settings -Force

Write-Host "Đăng ký thành công Scheduled Task '$taskName' chạy vào lúc 20:00 hàng ngày."
