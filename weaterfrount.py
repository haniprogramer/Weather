from tkinter import *
import requests
root=Tk()
root.title('Weather')
root.geometry('350x225')
root.resizable(0,0)

apikey='c93dbb3bda903b724e8c4d661e8075cd'
base_url='https://api.openweathermap.org/data/2.5/weather?q='


fram=LabelFrame(root,font=('Arial',15,'bold'),bg='chartreuse',bd=5,fg='white')
fram.place(x=0,y=2,width=350,height=125)

r = Label(fram,bg='chartreuse')
rt=Label(fram,bg='chartreuse')
rp=Label(fram,bg='chartreuse')
rh=Label(fram,bg='chartreuse')
rw=Label(fram,bg='chartreuse')
rd=Label(fram,bg='chartreuse')
def send():
    cityname=e1.get()
    url = base_url + cityname + '&appid=' + apikey
    result = requests.get(url)
    data = result.json()
    if data['cod'] == '404':
        r.config(text="City Not Found")
        # configبرای این است که یک بار خروجی نشان دهد
        r.pack()
    else:
        a = data['main']
        t = a['temp']
        tc = t - 273.15
        p = a['pressure']
        h = a['humidity']
        w = data['wind']['speed']
        d = data['weather'][0]['description']



        rt.config(text='temp '+str(round(tc))+' c')
        rp.config(text='pressure '+str(str(p)+' hpa'))
        rh.config(text='humidity '+str(h)+' %')
        rw.config(text=str(w)+' kts')
        rd.config(text='wind speed '+d)

        rt.pack()
        rp.pack()
        rh.pack()
        rw.pack()
        rd.pack()



trackfram=LabelFrame(root,font=('Arial',15,'bold'),bg='chartreuse',bd=5,fg='white')
trackfram.place(x=0,y=125,width=350,height=50)
l1=Label(trackfram,text="Please Enter The Name Of The City :",bg='chartreuse')
l1.place(x=0,y=5)

e1=Entry(trackfram)
e1.place(x=200,y=6)


fram2=LabelFrame(root,font=('Arial',15,'bold'),bg='chartreuse',bd=5,fg='white')
fram2.place(x=0,y=175,width=350,height=50)
b1=Button(fram2,text='Search',width=10,bg='yellow',command=send)
b1.place(x=75,y=5)
b2=Button(fram2,text='Close',width=10,bg='red',command=root.destroy)
b2.place(x=175,y=5)



root.mainloop()