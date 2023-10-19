import speedtest 
internetSpeed = speedtest.Speedtest()

def bytesToMb(bytes):
    KB =1024
    MB = KB*1024
    return (bytes/MB)

downloadSpeed = bytesToMb(internetSpeed.download())
uploadSpeed = bytesToMb(internetSpeed.upload())

print("Download speed: ",downloadSpeed,"MB")
print("Upload speed: ",uploadSpeed,"MB")