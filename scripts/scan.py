from zapv2 import ZAPv2
import time
zap = ZAPv2(apikey='',proxies={'http': 'http://127.0.0.1:8888','http':'http://127.0.0.1:8888'})
target = 'http://127.0.0.1/DVWA/'
print(f"starting sacn on {target}")
zap.urlopen(target)
time.sleep(2)
scan_id=zap.spider.scan(target)
while int(zap.spider.status(scan_id))<100:
     print("spider progress:"+zap.spider.status(scan_id)+"%")
     time.sleep(2)


print("spider complete")
scan_id= zap.ascan.scan(target)
while int(zap.ascan.status(scan_id))<100:
    print("active scan progress:"+zap.ascan.status(scan_id)+"%")
    time.sleep(5)


print("active scan complete")
alerts=zap.core.alerts()
with open ('vuln_report.txt','w') as f:
    for alert in alerts:
        f.write(f"{alert['alert']}-{alert['risk']}\n")
print("report saved")
