from tkinter import*
import math,random,os
from typing import SupportsFloat
class bill_app:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("billing software")
        bg_color="#074463"
        title=Label(self.root,text="biling software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        #=================Variable====================
        #===================cosmetics=================
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.gell=IntVar()
        self.loshan=IntVar()
        #================grocery========================
        self.rice=IntVar()
        self.food_oil=IntVar()
        self.daal=IntVar()
        self.wheat=IntVar()        
        self.sugar=IntVar()
        self.tea=IntVar()
        #================softdrink======================
        self.maza =IntVar()
        self.coke =IntVar()
        self.fruti =IntVar()
        self.mountain_dew =IntVar()
        self.sprite=IntVar()
        self.limca=IntVar()

        #=======Total Product Price & Tax Variable========
        self.cosmectic_price=StringVar()
        self.grocery_price=StringVar()
        self.soft_drink_price=StringVar()

        self.cosmectic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.soft_drink_tax=StringVar()

        #=================customer========================
        self.c_name=StringVar()
        self.c_phon=StringVar()

        self.bill_no=StringVar()
        x=random.randint(100,15000)
        self.bill_no.set(str(X))

        self.search_bill=StringVar()


        
        #=================Customer Details Frame
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphn_lbl=Label(F1,text="Customer Number",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_txt=Entry(F1,width=15,textvariable=self.c_phon,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        c_bill_lbl=Label(F1,text="Bill Number",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        c_bill_txt=Entry(F1,width=15,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        bill_btn=Button(F1,text="search",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=8,pady=8)


        #=======Cosmetic Frame========
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="COSMETICS",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=180,width=325,height=380)

        Bath_lbl=Label(F2,text="bath soap",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        Bath_txt_txt=Entry(F2,width=10,textvariable=self.soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        face_Cream_lbl=Label(F2,text="face cream",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        face_cream_txt=Entry(F2,width=10,textvariable=self.face_cream,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        face_w_lbl=Label(F2,text="face wash",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        face_w_txt=Entry(F2,width=10,textvariable=self.face_wash,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        hair_w_lbl=Label(F2,text="hair spray",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        hair_w_txt=Entry(F2,width=10,textvariable=self.spray,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        hair_g_lbl=Label(F2,text="hair gell",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        hair_g_txt=Entry(F2,width=10,textvariable=self.gell,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        body_lbl=Label(F2,text="body loshan",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        body_txt=Entry(F2,width=10,textvariable=self.loshan,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #=======Grocery Frame========
        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="GROCERY",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=340,y=180,width=325,height=380)

        B1_lbl=Label(F3,text="rice",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        B1_txt_txt=Entry(F3,width=10,textvariable=self.rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        F1_Cream_lbl=Label(F3,text="food oil",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        F1_cream_txt=Entry(F3,width=10,textvariable=self.food_oil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        F2_lbl=Label(F3,text="daal",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        F2_txt=Entry(F3,width=10,textvariable=self.daal,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        H1_lbl=Label(F3,text="wheat",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        H1_txt=Entry(F3,width=10,textvariable=self.wheat,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        H2_lbl=Label(F3,text="sugar",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        H2_txt=Entry(F3,width=10,textvariable=self.sugar,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        B2_lbl=Label(F3,text="tea",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        B2_txt=Entry(F3,width=10,textvariable=self.tea,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #=======Soft drink Frame========
        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="soft drink",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=670,y=180,width=325,height=380)

        B3_lbl=Label(F4,text="maza",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        B3_txt_txt=Entry(F4,width=10,textvariable=self.maza,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        F3_lbl=Label(F4,text="coke",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        F3_txt=Entry(F4,width=10,textvariable=self.coke,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        F4_lbl=Label(F4,text="fruti",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        F4_txt=Entry(F4,width=10,textvariable=self.fruti,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        H3_lbl=Label(F4,text="mountain dew",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        H3_txt=Entry(F4,width=10,textvariable=self.mountain_dew,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        H4_lbl=Label(F4,text="sprite",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        H4_txt=Entry(F4,width=10,textvariable=self.sprite,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        B4_lbl=Label(F4,text="limca",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        B4_txt=Entry(F4,width=10,textvariable=self.limca,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #==========Bill Area===========

        F5=Frame(self.root,bd=20,relief=GROOVE)
        F5.place(x=1050,y=180,width=460,height=380)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack()
        self.txtarea.pack(fill=BOTH,expand=1)

        #=======Button Frame===========

        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="BILL MENU",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=0,y=560,relwidth=1,height=140)

        m1_lbl=Label(F6,text="TOTAL COSMETIC PRICE",bg=bg_color,fg="lightgreen",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.cosmectic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2_lbl=Label(F6,text="TOTAL GROCERY PRICE",bg=bg_color,fg="lightgreen",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(F6,width=18,textvariable=self.grocery_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m3_lbl=Label(F6,text="TOTAL SOFTDRINK PRICE",bg=bg_color,fg="lightgreen",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F6,width=18,textvariable=self.soft_drink_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

        C1_lbl=Label(F6,text="COSMETIC TAX",bg=bg_color,fg="lightgreen",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        C1_txt=Entry(F6,width=18,textvariable=self.cosmectic_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

        C2_lbl=Label(F6,text="GROCERY TAX",bg=bg_color,fg="lightgreen",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        C2_txt=Entry(F6,width=18,textvariable=self.grocery_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        C3_lbl=Label(F6,text="SOFT DRINK TAX",bg=bg_color,fg="lightgreen",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        C3_txt=Entry(F6,width=18,textvariable=self.soft_drink_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        btn_F=Frame(F6,bd=13,relief=GROOVE)
        btn_F.place(x=820,width=590,height=105)

        total_btn=Button(btn_F,command=self.total,text="TOTAL",bg="cadetblue",fg="white",bd=9,pady=15,width=15,font="arial 8 bold").grid(row=0,column=0,padx=5,pady=5)
        bill_btn=Button(btn_F,text="GENRATE BILL",command=self.bill_area,bg="cadetblue",fg="white",bd=9,pady=15,width=15,font="arial 8 bold").grid(row=0,column=1,padx=5,pady=5)
        clear_btn=Button(btn_F,text="CLEAR",command=self.clear_data,bg="cadetblue",fg="white",bd=9,pady=15,width=15,font="arial 8 bold").grid(row=0,column=2,padx=5,pady=5)
        exit_btn=Button(btn_F,text="EXIT",command=self.Exit_app,bg="cadetblue",fg="white",bd=9,pady=15,width=15,font="arial 8 bold").grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()
 
    def total(self):
        self.c_s_p=self.soap.get()*40
        self.c_fc_p=self.face_cream.get()*120
        self.c_fw_p=self.face_wash.get()*60
        self.c_hs_p=self.spray.get()*160
        self.c_hg_p=self.gell.get()*99
        self.c_bl_p=self.loshan.get()*130
        
        self.total_cosmetic_price=float(
                                        self.c_s_p+
                                        self.c_fc_p+                             
                                        self.c_fw_p+
                                        self.c_hs_p+
                                        self.c_hg_p+
                                        self.c_bl_p                                                                           
                                        )
        self.cosmectic_price.set("Rs. "+str(self.total_cosmetic_price))
        self.c_tax=(self.total_cosmetic_price*0.18)
        self.cosmectic_tax.set("Rs  "+str(self.c_tax))

        self.g_r_p=self.rice.get()*110
        self.g_f_p=self.food_oil.get()*140
        self.g_d_p=self.daal.get()*85
        self.g_w_p=self.wheat.get()*160
        self.g_s_p=self.sugar.get()*150
        self.g_t_p=self.tea.get()*140
      
        self.total_grocery_price=float(
                                    self.g_r_p+
                                    self.g_f_p+                            
                                    self.g_d_p+
                                    self.g_w_p+
                                    self.g_s_p+
                                    self.g_t_p                                                                           
                                     )
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.g_tax=(self.total_grocery_price*0.5)
        self.grocery_tax.set("Rs  "+str(self.g_tax))

        self.d_m_p=self.maza.get()*40
        self.d_c_p=self.coke.get()*50
        self.d_f_p=self.fruti.get()*45
        self.d_md_p=self.mountain_dew.get()*40
        self.d_s_p=self.sprite.get()*40
        self.d_l_p=self.limca.get()*30  

        self.total_soft_drink_price=float(
                                       self.d_m_p+
                                       self.d_c_p+                           
                                       self.d_f_p+
                                       self.d_md_p+
                                       self.d_s_p+
                                       self.d_l_p                                                                      
                                       )
        self.soft_drink_price.set("Rs. "+str(self.total_soft_drink_price))
        self.d_tax=(self.total_soft_drink_price*0.18)
        self.soft_drink_tax.set("Rs  "+str(self.d_tax))

        self.Total_bill=float(self.total_cosmetic_price+self.total_grocery_price+self.total_soft_drink_price+self.c_tax+self.g_tax+self.d_tax)

    def welcome_bill(self):
         self.txtarea.delete('1.0',END)
         self.txtarea.insert(END,"\t--WELCOME WEBCODE RETAIL--")
         self.txtarea.insert(END,f"\n bill number : {self.bill_no.get()}")
         self.txtarea.insert(END,f"\n customer name : {self.c_name.get()}")
         self.txtarea.insert(END,f"\n customer phone number : {self.c_phon.get()}")
         self.txtarea.insert(END,f"\n*===============================================*")
         self.txtarea.insert(END,f"\n |Product|       \t|Qty|        \t|Price|")
         self.txtarea.insert(END,f"\n*===============================================*")
    def bill_area(self):
       if self.c_name.get()=="" or self.c_phon.get()=="":
          messagebox.showerror("error","customer details are must")
       else:
          self.welcome_bill()
          #=====cosmetics=======
          if self.soap.get()!=0:
             self.txtarea.insert(END,f"\n soap\t\t{self.soap.get()}\t\t{self.c_s_p}")
          if self.face_cream.get()!=0:
             self.txtarea.insert(END,f"\n face cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")
          if self.face_wash.get()!=0:    
             self.txtarea.insert(END,f"\n face wash\t\t{self.face_wash.get()}\t\t{self.c_hw_p}")
          if self.spray.get()!=0:    
             self.txtarea.insert(END,f"\n spray\t\t{self.spray.get()}\t\t{self.c_hs_p}")
          if self.gell.get()!=0:
             self.txtarea.insert(END,f"\n hair gell\t\t{self.gell.get()}\t\t{self.c_hg_p}")    
          if self.loshan.get()!=0:
             self.txtarea.insert(END,f"\n loshan\t\t{self.loshan.get()}\t\t{self.c_bl_p}")    

         #===========grocery=======
          if self.rice.get()!=0:
             self.txtarea.insert(END,f"\n rice\t\t{self.rice.get()}\t\t{self.g_r_p}")
          if self.food_oil.get()!=0:
             self.txtarea.insert(END,f"\n food oil\t\t{self.food_oil.get()}\t\t{self.g_f_p}")
          if self.daal.get()!=0:    
             self.txtarea.insert(END,f"\n daal\t\t{self.daal.get()}\t\t{self.g_d_p}")
          if self.wheat.get()!=0:    
             self.txtarea.insert(END,f"\n wheat\t\t{self.wheat.get()}\t\t{self.g_w_p}")
          if self.sugar.get()!=0:
             self.txtarea.insert(END,f"\n sugar\t\t{self.sugar.get()}\t\t{self.g_s_p}")    
          if self.tea.get()!=0:
             self.txtarea.insert(END,f"\n tea\t\t{self.tea.get()}\t\t{self.g_t_p}")    

          #=======soft drink=========
          if self.maza.get()!=0:
             self.txtarea.insert(END,f"\n maza\t\t{self.maza.get()}\t\t{self.d_m_p}")
          if self.coke.get()!=0:
             self.txtarea.insert(END,f"\n coke\t\t{self.coke.get()}\t\t{self.d_c_p}")
          if self.fruti.get()!=0:    
             self.txtarea.insert(END,f"\n fruti\t\t{self.fruti.get()}\t\t{self.d_f_p}")
          if self.mountain_dew.get()!=0:    
             self.txtarea.insert(END,f"\n mountain dew\t\t{self.mountain_dew.get()}\t\t{self.d_md_p}")
          if self.sprite.get()!=0:
             self.txtarea.insert(END,f"\n sprite\t\t{self.sprite.get()}\t\t{self.d_s_p}")    
          if self.limca.get()!=0:
             self.txtarea.insert(END,f"\n limca\t\t{self.limca.get()}\t\t{self.d_l_p}")    

          self.txtarea.insert(END,f"\n-------------------------------------------------")
          if self.cosmectic_tax.get()!="   Rs. 0.0":
             self.txtarea.insert(END,f"\n cosmetic tax\t\t\t{self.cosmectic_tax.get()}")

          if self.grocery_tax.get()!="   Rs. 0.0":
             self.txtarea.insert(END,f"\n grocery tax\t\t\t{self.grocery_tax.get()}")

          if self.soft_drink_tax.get()!="   Rs. 0.0":
             self.txtarea.insert(END,f"\n soft drink tax\t\t\t{self.soft_drink_tax.get()}")

             self.txtarea.insert(END,f"\n total bill :  \t\t\tRs.{str(self.Total_bill)}")
             self.txtarea.insert(END,f"\n ------------------------------------------------")
             self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","do you want to save the bill")
        if op>0:
            self.bill_date=self.txtarea.get('1.0',END)
            f1=open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_date)
            f1.close()
            messagebox.showinfo("saved",f"bill no. : {self.bill_no.get()} saved successfull")
        else:
            return
    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("error","Invalid Bill No.")

    def clear_data(self):
        op=messagebox.askyesno("Clear","Do You Realy Want To Clear Data?")
        if op>0:


        #===================cosmetics=================
            self.soap.set(0)    
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.spray.set(0)
            self.gell.set(0)
            self.loshan.set(0)
        #================grocery========================
            self.rice.set(0)
            self.food_oil.set(0)
            self.daal.set(0)
            self.wheat.set(0)        
            self.sugar.set(0)
            self.tea.set(0)
        #================softdrink======================
            self.maza.set(0)
            self.coke.set(0)
            self.fruti.set(0)
            self.mountain_dew.set(0)
            self.sprite.set(0)
            self.limca.set(0)

        #=======Total Product Price & Tax Variable========
            self.cosmectic_price.set("")
            self.grocery_price.set("")
            self.soft_drink_price.set("")

            self.cosmectic_tax.set("")
            self.grocery_tax.set("")
            self.soft_drink_tax.set("")

        #=================customer========================
        self.c_name.set("")
        self.c_phon.set("")

        self.bill_no.set("")
        self.welcome_bill()
    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do You Want To Exit?")
        if op>0:
            self.root.destroy()
            



root=Tk()
obj = bill_app(root)
root.mainloop()







