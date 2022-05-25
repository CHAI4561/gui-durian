# GUI.py

from tkinter import *
from tkinter import ttk, messagebox    # ttk ไฟล์ย่อยในpackage tkinter , messagebox=windows popup 

friend = {'somchai':'สมชาย ดีมาก',
		  'somsak':'สมศักดิ์ เก่งมาก',
		  'somsri':'สมศรี เยี่ยมมาก'}

GUI = Tk()
GUI.title('โปรแกรมของฉัน')    # ชื่อ windows
GUI.geometry('500x300')     # ขนาด

L = Label(GUI,text='กรุณากรอกรหัสชื่อ',font=('Angsana New',20)).pack(pady=20)

v_text = StringVar()        #StringVar ตัวแปรสำหรับเก็บข้อมูลที่อยู่ใน GUI
E1 = ttk.Entry(GUI, textvariable=v_text,font=('Angsana New',20)) #entry=ช่องให้กรอก
E1.pack()   

def Click():                # คำสั่ง func 
	
	text = v_text.get()  #ดึงข้อความที่ user พิมพ์ออกมา
	print('Text:' ,text)
	if text in friend:
		result = friend[text]
		print(friend[text])
		messagebox.showinfo('Result','รหัส: {} คือชื่อ: {}'.format(text,result))
	else:
		print('ไม่มีข้อมูลคนนี้')
		messagebox.showwarning('Result: Error','ไม่มีข้อมูลในระบบ กรุณากรอกใหม่ หรือเพิ่มเติมข้อมูลในระบบ')

B1 = ttk.Button(GUI, text='Search!',command=Click)     # ปุ่มกดใน ttk , command=ดึงfunc Clickให้ทำงาน
#B1.place(x=150 ,y=200)   place = ตำแหน่ง
B1.pack(ipadx=50,ipady=30,pady=30)    # pack=ปุ่มกดแล้วยุบ,ipad=ขนาด,pady=ระยะขอบแกน y,ปุ่มกดใส่fontไม่ได้

GUI.mainloop()    # ทำให้โปรแกรมรันได้ตลอดเวลา
