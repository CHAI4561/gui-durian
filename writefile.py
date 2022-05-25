# writefile.py
from datetime import datetime

# ฟังค์ชั่นบันทึกข้อมูลลงไฟล์ txt
#filename = 'data.txt' 
#with open(filename,'a',encoding='utf-8') as file:  # encoding='utf-8' ภาษาที่ไม่ใช่ภาษาอังกฤษ
#	file.write('\n' + 'วัน-เวลา: {} ทุเรียน: {} กก. รวมยอดทั้งหมด: {:,.2f} บาท'.format(stamp,quantity,cal))

def writetext(quantity,total):
	stamp = datetime.now()
	stamp = stamp.replace(year=stamp.year+543) # ปี พ.ศ.
	stamp = stamp.strftime('%Y-%m-%d %H:%M:%S')
	filename = 'data.txt'
	with open(filename,'a',encoding='utf-8') as file:  # encoding='utf-8' ภาษาที่ไม่ใช่ภาษาอังกฤษ
		file.write('\n' + 'วัน-เวลา: {} ทุเรียน: {} กก. รวมยอดทั้งหมด: {:,.2f} บาท'.format(stamp,quantity,total))

writetext(90,9000)
writetext(91,9100)
writetext(92,9200)
writetext(93,9300)