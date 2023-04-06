#==========================================COVID 19 DATA ANALYSIS=========================================

#====================================================Modules====================================================================

import tkinter as tk
from tkinter.ttk import *
 
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import tkinter.font as font
from tkcalendar import *
from ttkthemes import themed_tk as tk1
#===============================================Frame Design===============================================================
root = tk1.ThemedTk()
root.get_themes()
root.set_theme('breeze')

def __init__(root):
             titlespace=""
             root.title(102*titlespace + 'COVID 19 Database')
             root.geometry("1000x900+300+0")
             root.resizable(width=False,height=False)

Mainframe=Frame(root,bd=10,width=1000,height=700,bg='crimson',relief=GROOVE)
Mainframe.grid()

Titleframe=Frame(Mainframe,bd=7,width=770,height=100,bg='crimson',relief= RIDGE)
Titleframe.grid(row=0,column=0)
Topframe=Frame(Mainframe,bd=5,width=770,height=500,bg='crimson',relief=RIDGE)
Topframe.grid(row=1,column=0)

Leftframe=Frame(Topframe,bd=5,width=770,height=400,padx=2,bg='crimson',relief=RIDGE)
Leftframe.pack(side=LEFT)
Leftframe1=Frame(Leftframe,bd=5,width=600,height=400,padx=2,bg='crimson',relief=RIDGE)
Leftframe1.pack(side=TOP,padx=0,pady=0)

Rightframe=Frame(Topframe,bd=5,width=200,height=400,padx=2,bg='crimson',relief=RIDGE)
Rightframe.pack(side=RIGHT)
Rightframe1=Frame(Rightframe,bd=5,width=200,height=300,padx=2,pady=2,bg='crimson',relief=GROOVE)
Rightframe1.pack(side=TOP)


lbltitle=Label(Titleframe,text="COVID 19 DATABASE",font='helvetica 30 bold',bg='crimson',fg='white',bd=7)
lbltitle.grid(row=0,column=0,padx=132)
font=font.Font(size=20)
lbltitle['font']=font

root.title("COVID 19 DATABASE")

root.resizable(0,0)

#================================================Assigning Variables============================================================
sno=int()
name=StringVar()
age=StringVar()
gender=StringVar()
phone=StringVar()
temp=StringVar()
atb=StringVar()
date=StringVar()
time=StringVar()
loc=StringVar()

#==================================Labels and Entry for data=============================================================

sno= tk.Entry(Leftframe1,textvariable=sno,bd=5,width=44,justify='left')
sno.grid(row=0,column=1,padx=5)
sno_label=tk.Label(Leftframe1, text='Enter Serial No : ',font='helvetica 13 bold',bg='crimson',fg='white')
sno_label.grid(row=0,column=0)

name= tk.Entry(Leftframe1,textvariable=name,bd=5,width=44,justify='left')
name.grid(row=1,column=1,padx=5)
name_label=tk.Label(Leftframe1, text='Enter name : ',font='helvetica 13 bold',bg='crimson',fg='white')
name_label.grid(row=1,column=0)

age_label=tk.Label(Leftframe1,text='Age : ',font='helvetica 13 bold',bg='crimson',fg='white')
age_label.grid(row=2,column=0)
age=ttk.Combobox(Leftframe1,textvariable=age,width=42,state='readonly')
age['values']=('Select','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100')                  
age.current(0)
age.grid(row=2,column=1,padx=5)


gender_label=tk.Label(Leftframe1,text='Gender :',font='helvetica 13 bold',bg='crimson',fg='white')
gender_label.grid(row=3,column=0)
gender=ttk.Combobox(Leftframe1,textvariable=gender,width=42,state='readonly')
gender['values']=('Select','Male','Female')
gender.current(0)
gender.grid(row=3,column=1,padx=5)

phone_label=tk.Label(Leftframe1,text='Enter phone no : ',font='helvetica 13 bold',bg='crimson',fg='white')
phone_label.grid(row=4,column=0)
phone=tk.Entry(Leftframe1,textvariable=phone,bd=5,width=44,justify='left')
phone.grid(row=4,column=1,padx=5)

temp=tk.Entry(Leftframe1,textvariable=temp,bd=5,width=44,justify='left')
temp.grid(row=5,column=1,padx=5)
temp_label=tk.Label(Leftframe1,text='Enter temperature recorded :',font='helvetica 13 bold',bg='crimson',fg='white')
temp_label.grid(row=5,column=0)

atb=ttk.Combobox(Leftframe1,textvariable=atb,width=42,state='readonly')
atb['values']=('Select','Positive','Negative')
atb.current(0)
atb.grid(row=6,column=1,padx=5)
atb_label=tk.Label(Leftframe1,text='Enter Antibody Test Result : ',font='helvetica 13 bold',bg='crimson',fg='white')
atb_label.grid(row=6,column=0)


date=DateEntry(Leftframe1,bd=5,width=42, background='crimson',
                    foreground='white', borderwidth=2,date_pattern='yyyy/mm/dd',state='readonly')
date.grid(row=7,column=1,padx=5)
date_label=tk.Label(Leftframe1,text='Enter date of entering : ',font='helvetica 13 bold',bg='crimson',fg='white')
date_label.grid(row=7,column=0)

time=tk.Entry(Leftframe1,textvariable=time,bd=5,width=44,justify='left')
time.grid(row=8,column=1,padx=5)
time_label=tk.Label(Leftframe1,text='Enter time of entering : ',font='helvetica 13 bold',bg='crimson',fg='white')
time_label.grid(row=8,column=0)

loc_label=tk.Label(Leftframe1,text='Enter location of entering :',font='helvetica 13 bold',bg='crimson',fg='white')
loc_label.grid(row=9,column=0)
loc=ttk.Combobox(Leftframe1,textvariable=loc,width=42,state='readonly')
loc['values']=('Select','Mall','Temple','Theatre','Hotel','Park')
loc.current(0)
loc.grid(row=9,column=1,padx=5)








#======================================Functions used in Buttons =============================================================

def Exit():
             Exit=tkinter.messagebox.askyesno("COVID 19 Database","Are you sure you want to exit??")
             if Exit>0:
                         root.destroy()
                         return
def Reset():
             sno.delete(0,END)
             name.delete(0, END)
             age.current(0)
             gender.current(0)
             phone.delete(0, END)
             temp.delete(0, END)
             atb.current(0)
             time.delete(0, END)
             loc.current(0)
             for record in covid_data.get_children():
                          covid_data.delete(record)
            
def addData():
            if sno.get() ==""or name.get()=="":
                          tkinter.messagebox.showerror('COVID 19 Database','Enter correct details')
            else:
                         try:
                                      import mysql.connector as mys
                                      mycon=mys.connect(host='localhost',user='root',passwd='gr8ani123',database='coviddata')
                                      cursor=mycon.cursor()
                                      query="insert into covid19 values({0},'{1}',{2},'{3}','{4}',{5},'{6}','{7}','{8}','{9}')".format(sno.get(),name.get(),age.get(),gender.get(),phone.get(),temp.get(),atb.get(),date.get(),time.get(),loc.get())
                                      cursor.execute(query)
                                      mycon.commit()
                                      mycon.close()
                         except:
                                       import mysql.connector as mys
                                       mycon=mys.connect(host='localhost',user='root',passwd='gr8ani123',database='coviddata')
                                       cursor=mycon.cursor()
                                       query="select * from covid19"
                                       cursor.execute(query)
                                       mydata=cursor.fetchall()
                                       for row in mydata:
                                                    if sno.get()==row[0]:
                                                                 tkinter.messagebox.showerror('COVID 19 Database','This serial no already exists')  
                                                                  
                                       
                         
                                     
                         
def DisplayData():
             import mysql.connector as mys
             mycon=mys.connect(host='localhost',user='root',passwd='gr8ani123',database='coviddata')
             cursor=mycon.cursor()
             query="select*from covid19"
             cursor.execute(query)
             result=cursor.fetchall()
             if len(result)!=0:
                          for row in result:
                                       covid_data.insert('',END,values=row)
                                      
             mycon.commit()
             mycon.close()
def Stat():
             root1 = tk1.ThemedTk()
             root1.get_themes()
             root1.set_theme('breeze')
             titlespace=""
             root1.title(102*titlespace + 'COVID 19 Database')
             root1.geometry("480x440+10+0")
             root1.resizable(width=False,height=False)
             Mainframe1=Frame(root1,bd=7,width=1000,height=700,bg='crimson',relief=GROOVE)
             Mainframe1.grid()
             locstat_label=tk.Label(Mainframe1,text='For report based on Location click the button below ',font='helvetica 13 bold',bg='crimson',fg='white')
             locstat_label.grid(row=0,column=0)
             locstat_btn=tk.Button(Mainframe1, text='Click for report based on location',bd=10,pady=1,padx=24,width=20,height=10,command=LocStat)
             locstat_btn.grid(row=1,column=0,padx=10)
             atbstat_label=tk.Label(Mainframe1,text='For report based on ANTIBODY test click the button below',font='helvetica 13 bold',bg='crimson',fg='white')
             atbstat_label.grid(row=2,column=0)
             atbstat_btn=tk.Button(Mainframe1, text='Report based on ANTIBODY test',bd=10,pady=1,padx=24,width=20,height=10,command=atbstat)
             atbstat_btn.grid(row=3,column=0,padx=10)


             
             
                          
#Buttons


addnew_btn=tk.Button(Rightframe1, text='ADD RECORD',bd=4,pady=1,padx=24,width=8,height=2,command=addData)
addnew_btn.grid(row=0,column=0,padx=1)

reset_btn=tk.Button(Rightframe1, text='RESET',bd=4,pady=1,padx=24,width=8,height=2,command=Reset)
reset_btn.grid(row=1,column=0,padx=1)

display_btn=tk.Button(Rightframe1, text='DISPLAY',bd=4,pady=1,padx=24,width=8,height=2,command=DisplayData)
display_btn.grid(row=2,column=0,padx=1)

exit_btn=tk.Button(Rightframe1, text='EXIT',bd=4,pady=1,padx=24,width=8,height=2,command=Exit)
exit_btn.grid(row=4,column=0,padx=1)

stat_btn=tk.Button(Rightframe1, text='STATS',bd=4,pady=1,padx=24,width=8,height=2,command=Stat)
stat_btn.grid(row=3,column=0,padx=1)





scroll_x=Scrollbar(Leftframe,orient=VERTICAL)

covid_data=ttk.Treeview(Leftframe,height=12,columns=('sno','name','age','gender','phone','temp','atb','date','time','loc'),yscrollcommand=scroll_x.set)
scroll_x.pack(side=RIGHT,fill=Y)

covid_data.heading('sno',text='S NO')
covid_data.heading('name',text='NAME')
covid_data.heading('age',text='AGE')
covid_data.heading('gender',text='GENDER')
covid_data.heading('phone',text='MOBILE')
covid_data.heading('temp',text='TEMPERATURE')
covid_data.heading('atb',text='ANTIBODY TEST')
covid_data.heading('date',text='DATE')
covid_data.heading('time',text='TIME')
covid_data.heading('loc',text='LOCATION')

covid_data['show']='headings'

covid_data.column('sno',width=50)
covid_data.column('name',width=70)
covid_data.column('age',width=50)
covid_data.column('gender',width=70)
covid_data.column('phone',width=100)
covid_data.column('temp',width=100)
covid_data.column('atb',width=100)
covid_data.column('date',width=70)
covid_data.column('time',width=60)
covid_data.column('loc',width=70)
covid_data.pack(fill=BOTH,expand=1)



             

def LocStat():
             import mysql.connector as mys
             mycon=mys.connect(host='localhost',user='root',passwd='gr8ani123',database='coviddata')
             cursor=mycon.cursor()
             result1=0
             query1="select * from covid19 where location='mall'"
             cursor.execute(query1)
             mydata1=cursor.fetchall()
             for row in mydata1:
                          result1=result1+1
             
             result2=0
             query2="select * from covid19 where location='temple'"
             cursor.execute(query2)
             mydata2=cursor.fetchall()
             for row in mydata2:
                          result2=result2+1

             result3=0
             query3="select * from covid19 where location='hotel'"
             cursor.execute(query3)
             mydata3=cursor.fetchall()
             for row in mydata3:
                          result3=result3+1

             result4=0
             query4="select * from covid19 where location='theatre'"
             cursor.execute(query4)
             mydata4=cursor.fetchall()
             for row in mydata4:
                          result4=result4+1                          


             result5=0
             query5="select * from covid19 where location='park'"
             cursor.execute(query5)
             mydata5=cursor.fetchall()
             for row in mydata5:
                          result5=result5+1


             from matplotlib import pyplot as plt
             import numpy as np
             fig = plt.figure()
             ax = fig.add_axes([0,0,1,1])
             ax.axis('equal')
             locations = ['Mall','Temple','Hotel','Theatre','Park']
             people = [result1,result2,result3,result4,result5]
             ax.pie(people, labels = locations,autopct='%1.2f%%')
             plt.show()

             

def atbstat():
             import mysql.connector as mys
             mycon=mys.connect(host='localhost',user='root',passwd='gr8ani123',database='coviddata')
             cursor=mycon.cursor()
             result1=0
             query1="select * from covid19 where ATB='positive'"
             cursor.execute(query1)
             mydata1=cursor.fetchall()
             for row in mydata1:
                          result1=result1+1
             
             
             result2=0
             query2="select * from covid19 where ATB='negative'"
             cursor.execute(query2)
             mydata2=cursor.fetchall()
             for row in mydata2:
                          result2=result2+1

             
             from matplotlib import pyplot as plt
             import numpy as np
             fig = plt.figure()
             ax = fig.add_axes([0,0,1,1])
             ax.axis('equal')
             locations = ['Positive','Negative']
             people = [result1,result2]
             ax.pie(people, labels = locations,autopct='%1.2f%%')
             plt.show()
