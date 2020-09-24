from tkinter import *
from PIL import Image, ImageTk 
from os import *

window = Tk()
window.title("Pune Food Guide")
window.geometry('900x710')
window.resizable(width=0, height=0)
window.configure(background = "#ffffff")

def buttonPresssed():
    l.destroy()
    l2.destroy()
    e1.destroy()
    b.destroy()
#    print('Journey Started')

    #Get Font
    window.geometry('890x700')
        
    Lbl1=Label(window,text='Food Item List',font=('Times New Roman Bold',32),fg="red",bg="#ffffff")
    Lbl1.pack()
    
    Lbl2=Label(window,text='select food item You want to Eat',font=('Calibri',18),fg="black",bg="#ffffff")
    Lbl2.pack()

    def fun(food):
        window.geometry('500x510')
        vals = {1:"Bhel",2:"Bhakharwadi",3:"Misal",4:"Pav_Bhaji",5:"Puran_Poli",6:"Momos"}
        #print(food,vals[food])
        foods=vals[food]
        
        Lbl1.destroy()
        Lbl2.destroy()
        b1.destroy()
        b2.destroy()
        b3.destroy()
        b4.destroy()
        b5.destroy()
        b6.destroy()

        Lbl3=Label(window,text='Place List',font=('Times New Roman Bold',37),fg="red",bg="#ffffff")
        Lbl3.pack()
        Lbl4=Label(window,text='select place where you want to eat',font=('Calibri',20),fg="blue",bg="#ffffff")
        Lbl4.pack()

        values = {101:"Baner",102:"Deccan",103:"Kothrud",104:"Aundh"}
        
        def end(p):
            place = values[p]
            #print(p,place)

            Lbl3.destroy()
            Lbl4.destroy()
            rb1.destroy()
            rb2.destroy()
            rb3.destroy()
            rb4.destroy()

            window.geometry('800x500')
            Lbl5=Label(window,text='List of Places',font=('Times New Roman Bold',40),fg="red",bg="#ffffff")
            Lbl5.pack()

            location={"Baner":{"Bhel":["Balaji Bhel \n  Baner Rd, Near Shri Balaji Co-operative Housing Society",
                                       "Kalyan Bhel \n  Baner Rd, near Ganraj Mangal karyalay",
                                       "Ganesh Bhel Farsan House\n  Shop No. 3, Kapil Classic, Opposite To Bikane"
                                       ],
                               "Bhakharwadi":["Chitale Bandhu Mithaiwale \n  265, Baner Rd, Varsha Park Society,\n  Baner, Pune",
                                              "The K Factory \n  SNo 288/1A/2, Level 1&2, Ground Floor, IQS Tower,\n  opposite Kapil Malhar, Building, Baner, Pune"
                                              ],
                               "Misal":["Khasbag Misal \n  Sr No 134 Mhetre Corner, opp. to Shri Ganesh Datta Mandir,\n  Balewadi Phata, Baner, Pune",
                                            "Satej Misal \n  17, Baner Rd, Baner Gaon, Baner, Pune"
                                            ],
                               "Pav_Bhaji":["MH12 Pav Bhaji Baner \n  183/2, Baner Road, Karan Park Society, Baner, Pune",
                                            "Mumbaian Pav Bhaji \n  Atharva Residency, shop no 1, food court, Baner Rd,\n  in front of Axis Bank, Baner, Pune"
                                            ],
                               "Puran_Poli":["Maha Khavaiyye \n   Shop No. 4 & 5, Shiva Heights II, opposite State Bank of India,\n  Pimple Saudagar, Pune"],
                               "Momos":["Yalla Momos \n  Shop No. 8, Vastu Nirvana, Baner - Pashan Link Rd, Pune",
                                        "North East Momos \n  Nandan Acura Rd, Laxman Nagar, Baner, Pune"
                                        ]
                               },
                      "Deccan":{"Bhel":["Sangeeta Bhel And Pani Puri\n  Deccan Gymkhana, Pune",
                                       "Anil Bhel And Panipuri \n  Deccan Gymkhana Rd, near Roopam corner, Deccan Gymkhana, Pune",
                                        ],
                               "Bhakharwadi":["Chitale Bandhu Mithaiwale \n   Opp Gharware Chowk, near Roopam Corner, Deccan Gymkhana, Pune"
                                              ],
                               "Misal":["Peshwai Misal \n  goodluck chowk, Asmani Plaza, Pulachi Wadi,\n  Deccan Gymkhana, Pune",
                                            "Wadeshwar FC \n  1229/A, Fergusson College Rd, Ganeshwadi, Deccan Gymkhana, Pune"
                                            ],
                               "Pav_Bhaji":["Wadeshwar FC \n  1229/A, Fergusson College Rd, Ganeshwadi, Deccan Gymkhana, Pune",
                                            "Chaat Bazaar \n  Sagar Arcade, Fergusson College Rd, Deccan Gymkhana, Pune"
                                            ],
                               "Puran_Poli":["Soaham Dining Hall and Food Zone \n  Prabhat Kiran, 1259/1, Jangali Maharaj Rd, Shivajinagar, Pune"],
                               "Momos":["The Quick Wok \n  Shop No 4, Rameshwar apartment opposite to stay well hotel,\n  Pulachi Wadi Rd, behind Sai petrol Pump, Deccan Gymkhana, Pune",
                                        "Hot Momos & Burgers \n 103, Bahiratwadi, Behind ICC Trade Tower, Senapati Bapat Rd, Pune"
                                        ]
                                },
                      "Kothrud":{"Bhel":["Shri Ganesh Bhel & Panipuri\n  Sno 120, Plot no 52, Mhetre Soc. Shop no 3,\n  Shivtirthnagar, Paud Rd, Kothrud, Pune",
                                         "Manisha Bhel\n  Baburao Padwal Rd, Madhusanchay Society, Tejonidhi Housing Society,\n  Ganesh Nagar, Karve Nagar, Pune"
                                         ],
                               "Bhakharwadi":["Chitale Bandhu Mithaiwale \n   Shop No. 1&2, Bus depot, 128, Omkar, Patel Icon, 1,Paud Rd, near Kothrud,\n   Left Bhusari Colony, Kothrud, Pune",
                                              "Chitale Bandhu Mithaiwale \n   Shop No 5, Punit Yash Arcade, Near, Kothrud Bus Stand Rd,\n   Dahanukar A, Dahanukar Colony, Kothrud, Pune",
                                              "Harsh Foods \n   94/2, Shivdatta Plaza, Shop No.1, Opposite P.M.T Bus depo,\n   Paud Rd, Bhusari Colony, Kothrud, Pune"
                                              ],
                               "Misal":["Masti Misal \n   Shop no. 4, Damodar Villa, Opp Kothrud Bus Stand, Karve Rd, Pune",
                                        "Medhekar Misal\n   Shop No. 3, Shrividya Apartments, Yamaha Showroom Lane, Parmahans Nagar, Kothrud, Pune"
                                            ],
                               "Pav_Bhaji":["Aakash Pavbhaji \n  Swami Vivekanad Chowk,Azad Nagar, Near Tulisi Market,\n  Shastri Nagar, Kothrud, Pune",
                                            "Laxminarayan Pavbhaji Center \n  1, Behede Complex, Near Bank Of India, Paud Road, \n  Kothrud, Pune"
                                            ],
                               "Puran_Poli":["Puran Poli \n  589, Anna Athawale Rd, Narayan Peth, Pune"],
                               "Momos":["The Momo Panda \n  Karishma Society Shop No. 26, Opposite Creamstone Ice cream,\n  Kothrud, Pune",
                                        "Yahoo Momos \n  Shop Number 8, Ideal Chambers, &nbsp, Paud Rd, Ideal Colony, \n  Kothrud, Pune"
                                        ]
                                 },
                      "Aundh":{"Bhel":["Radhika Bhel And Pavbhaji Center \n  Kumar Classics Rd, Ward No. 8, Aundh Gaon, Aundh, Pune",
                                       "Shraddha Snacks \n  Aundh DP Road, Besides Kaka Halwai, opposite Ram Laxman Garden, \n  Aundh, Pune"
                                       ],
                               "Bhakharwadi":["Mithas Delicious Sweets \n  Siddeshwar Heights, Shop No. 5, Shree, ITI Rd, Aundh, Pune",
                                              "Kaka Halwai Sweets and Namkeen \n  Shop No A, Abja Pavillion, Raagdari Society, Aundh, Pune"
                                              ],
                               "Misal":["Thorat's Barbeque Misal \n  Uttam Enclave Society, Mahadji Shinde Rd, Ward No. 8, Aundh Gaon, Aundh, Pune",
                                        "Vadheev Misal \n  Shop no. B 10, Sai heritage, near Medipoint hospital, \n  Aundh - Baner Link Rd, Aundh, Pune"
                                        ],
                               "Pav_Bhaji":["Radhika Bhel And Pavbhaji Center \n  Kumar Classics Rd, Ward No. 8, Aundh Gaon, Aundh, Pune",
                                            "Rudra Pav Bhaji & Juice Bar \n  Shop B9, Sai Heritage Co-op Society, Aundh - Baner Link Rd,\n  Aundh, Pune"
                                            ],
                               "Puran_Poli":["Ratnaj Kitchen \n  B-17 Shivali Apt., Sinhgad Rd, Anand Nagar, Pune"],
                               "Momos":["Momos Centre \n ITI Road Sindh Society, Ward No. 8, Anand Park, Aundh, Pune",
                                        "Kimling \n  SR Chambers, 161/162, Nagras Rd, opp. Tangent Furniture, \n  Suvarnayug Society, Ward No. 8, Aundh, Pune"]
                               }
                      }
            f = location[place]
            fp= f[foods]
            j=1
            
            for i in fp:
                txt=str(j)+'. '+str(i)
                lbl = Label(window,text=txt,font=('Times New Roman',16),fg="black",bg="#ffffff",justify =LEFT)
                lbl.place(x=3,y=j*100)
                j+=1

            def exit():
                    window.destroy()
                    
            btne=Button(window,text="Thank You",fg="blue",font=("Times",16),command=exit,padx=20,pady=10)
            btne.place(x=310,y=390)


        rb1 = Button(window,text="Baner",font=('Calibri',18),pady=15,fg='#4f0445',bg='#ebdfed',command=lambda: end(101))
        rb1.pack(fill = X, ipady = 10)
        rb2 = Button(window,text="Deccan",font=('Calibri',18),pady=15,fg='#4f0445',bg='#ebdfed',command=lambda: end(102))
        rb2.pack(fill = X, ipady = 15)
        rb3 = Button(window,text="Kothrud",font=('Calibri',18),pady=15,fg='#4f0445',bg='#ebdfed',command=lambda: end(103))
        rb3.pack(fill = X, ipady = 15)
        rb4 = Button(window,text="Aundh",font=('Calibri',18),pady=15,fg='#4f0445',bg='#ebdfed',command=lambda: end(104))
        rb4.pack(fill = X, ipady = 15) 


        
    b1 = Button(window,text="bhel",padx=15,pady=15,relief='raised',borderwidth=2,bg="blue",command=lambda: fun(1))
    b1.config(image=ph_im1)
    b1.place(x = 25, y = 117)   
    
    b2 = Button(window,text="bhek",padx=15,pady=15,relief='raised',borderwidth=2,bg="blue",command=lambda: fun(2))
    b2.config(image=ph_im2)
    b2.place(x=315,y=117)    
    
    b3 = Button(window,text="misal",padx=20,pady=20,relief='raised',borderwidth=2,bg="blue",command=lambda: fun(3))
    b3.config(image=ph_im3)
    b3.place(x = 605, y = 117)   

    b4 = Button(window,text="pavbhaji",padx=20,pady=20,relief='raised',borderwidth=2,bg="blue",command=lambda: fun(4))
    b4.config(image=ph_im4)
    b4.place(x = 25, y = 420)    

    b5 = Button(window,text="puran",padx=20,pady=20,relief='raised',borderwidth=2,bg="blue",command=lambda: fun(5))
    b5.config(image=ph_im5)
    b5.place(x=315,y=420)    

    b6 = Button(window,text="modak",padx=20,pady=20,relief='raised',borderwidth=2,bg="blue",command=lambda: fun(6))
    b6.config(image=ph_im6)
    b6.place(x = 605, y = 423)
    

l=Label(window,text='WELCOME, PUNE FOOD WORLD',font=('Times New Roman Bold',40),fg="red",bg="#ffffff")
l.pack(pady=5)

l2=Label(window,text='smart people, smart choice',font=('Calibri',20),fg="black",bg="#ffffff")
l2.pack(padx=45,pady=0)


ph_im1 = ImageTk.PhotoImage(Image.open("foods/bhel.jpg"))
ph_im2 = ImageTk.PhotoImage(Image.open("foods/bhakarwadi.jpg"))
ph_im3 = ImageTk.PhotoImage(Image.open("foods/misal1.jpg"))
ph_im4 = ImageTk.PhotoImage(Image.open("foods/pavbhaji.png"))
ph_im5 = ImageTk.PhotoImage(Image.open("foods/PuranPoli.jpg"))
ph_im6 = ImageTk.PhotoImage(Image.open("foods/momos1.jpg"))

render = ImageTk.PhotoImage(Image.open("foods/ShaniwarWadaGate.jpg"))

e1 = Label(image=render,width=900,height=550)
e1.pack()

b=Button(window,text="Let's Go >> ",font=('Calibri',15),padx=40,pady=20,bg='#6dbce3',fg='#4f0445',command=buttonPresssed)
b.pack(side='bottom')
