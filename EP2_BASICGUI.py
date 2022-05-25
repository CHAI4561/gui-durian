from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime
import csv
######################################
def timestamp(thai=True):
	if thai ==True:
		stamp = datetime.now()
		stamp = stamp.replace(year=stamp.year+543) # ปี พ.ศ.
		stamp = stamp.strftime('%Y-%m-%d %H:%M:%S')
	else:
		stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	return stamp


def writetext(quantity,total):
	stamp = timestamp()
	filename = 'data.txt'   # ฟังค์ชั่นบันทึกข้อมูลลงไฟล์ txt
	with open(filename,'a',encoding='utf-8') as file:  # encoding='utf-8' ภาษาที่ไม่ใช่ภาษาอังกฤษ
		file.write('\n' + 'วัน-เวลา: {} ทุเรียน: {} กก. รวมยอดทั้งหมด: {:,.2f} บาท'.format(stamp,quantity,total))

def writecsv(data):
	with open('data.csv','a',newline='',encoding='utf-8') as file:
		fw = csv.writer(file)      # fw = file writer
		fw.writerow(data)          # listเดียว บรรทัดเดียว
	print('Success')

def readcsv():
	with open('data.csv',newline='',encoding='utf-8') as file:
		fr = csv.reader(file)
		#print(list(fr))   # result ออกมามี single quote (string) จะนำไปใช้ ต้องแปลงกลับเป็นตัวเลขก่อน
		data = list(fr)
	return data  # นำ data ไปใช้งาน ต้อง return data ทุกครั้ง

def sumdata():
	# ฟังค์ชั่นนี้ใช้สำหรับรวมค่าที่ได้จาก csv ไฟล์สรุปออกมาเป็น 2 อย่าง
	result = readcsv()
	sumlist_quan = []
	sumlist_total = []
	for d in result:   
		sumlist_quan.append(float(d[1]))
		sumlist_total.append(float(d[2]))
	sumquan = sum(sumlist_quan)
	sumtotal = sum(sumlist_total)

	return (sumquan,sumtotal)

##################

GUI = Tk()
GUI.geometry('700x600')
GUI.title('โปรแกรมสำหรับแม่ค้าทุเรียน v.0.0.1')

file = PhotoImage(file='durian.png')
IMG = Label(GUI,image=file,text='')
IMG.pack()

L1 = Label(GUI,text='โปรแกรมคำนวณทุเรียน',font=('Angsana New',30,'bold'),fg='green')
L1.pack() #place(x,y) , grid(row=0,column=0)

L2 = Label(GUI,text='กรุณากรอกจำนวนทุเรียน (กิโลกรัม)',font=('Angsana New New',20))
L2.pack()

v_quantity = StringVar()  #ตำแหน่งตัวแปรที่ใช้เก็บข้อมูลของช่องกรอก

E1 = ttk.Entry(GUI,textvariable=v_quantity,font=('impact',30))
E1.pack()

def Calculate(event=None):   # เมื่อไม่มี event ออกไปจากการกดปุ่ม enter (กด click) ต้องระบุ event=None เพื่อให้ฟังค์ชั่นทำงาน 
	quantity = v_quantity.get()
	price = 100
	print('จำนวน', float(quantity) * price)
	cal = float(quantity) * price
	
	# writetext(quantity,cal)
	data = [timestamp(),quantity,cal]
	writecsv(data)

	# ฟังค์ชั่นบันทึกข้อมูลลงไฟล์ txt
	#filename = 'data.txt' 
	#with open(filename,'a',encoding='utf-8') as file:  # encoding='utf-8' ภาษาที่ไม่ใช่ภาษาอังกฤษ
	#	file.write('\n' + 'วัน-เวลา: {} ทุเรียน: {} กก. รวมยอดทั้งหมด: {:,.2f} บาท'.format(stamp,quantity,cal))

	title = 'ยอดที่ลูกค้าต้องจ่าย'
	text = 'ทุเรียนจำนวน {} กิโลกรัม ราคาทั้งหมด: {:,.2f} บาท'.format(quantity,cal)
	messagebox.showinfo(title,text)

	v_quantity.set('') # clear data
	E1.focus()

B1 = ttk.Button(GUI, text='คำนวณ',command=Calculate)
B1.pack(ipadx=30,ipady=20,pady=20)

E1.bind('<Return>',Calculate)   # กดปุุ่ม enter เรียกให้ ฟังค์ชั่น Calculate ทำงาน ตั้งใส่ event ให้ func Calculate ด้วย

def SummaryData(event):  
	# pop up
	sm = sumdata()
	title = 'ยอดสรุปรวมทั้งหมด'
	text = 'จำนวนที่ขายได้:{} กก.\nยอดขาย: {:,.2f} บาท'.format(sm[0],sm[1])
	messagebox.showinfo(title,text)


GUI.bind('<F2>',SummaryData)	# ตรวจสอบ event ว่ามีการกด keyboard อะไร เพื่อให้ฟังค์ชั่นทำงาน
GUI.bind('<F1>',SummaryData)	
E1.focus()  # ให้ cursor ไปยังตำแหน่งของ E1
GUI.mainloop()