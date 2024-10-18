from tkinter import *
from tkinter import messagebox

import mysql.connector


class NlpApp:

    def __init__(self):

        # database connection
        self.db = mysql.connector.connect(
            host= "localhost",
            user= "root",
            password ="Mumb@i1029011011",
            database = "satishtable"

        )

        self.cursor = self.db.cursor()

        # Login ka GUI load karna hai
        self.root = Tk()
        self.root.title('Tuber')
        self.root.iconbitmap("Resources/favicon-32x32.png")
        self.root.geometry('350x600')
        self.root.configure(bg='#7f8c8d')
        self.Login()

        self.root.mainloop()


    def Login(self):

        self.clear()

        heading =Label(self.root,text="Tuber App",bg='#7f8c8d',fg='white')
        heading.pack(pady=(20,20))
        heading.configure(font=('verdana',24,'bold'))

        label1= Label(self.root,text="Enter Email",bg='#7f8c8d',fg='white')
        label1.pack(pady=(10,10))
        label1.configure(font=('verdana',13,'bold'))

        self.email_input= Entry(self.root,width=30)
        self.email_input.pack(pady=(10,10))

        label2= Label(self.root,text="Enter Password",bg='#7f8c8d',fg='white')
        label2.pack(pady=(10,10))
        label2.configure(font=('verdana',13,'bold'))

        self.password_input= Entry(self.root,width=30,show="*")
        self.password_input.pack(pady=(10,10))

        login_btn = Button(self.root,text="Login",command=self.performing_login)
        login_btn.pack(pady=(10,10))

        label3= Label(self.root,text="Not a Member ?",bg='#7f8c8d',fg='white')
        label3.pack(pady=(10,10))
        label3.configure(font=('verdana',13,'bold'))

        regbtn = Button(self.root, text="Register Now",command=self.register_gui)
        regbtn.pack(pady=(5,5))

    def performing_login(self):
        email = self.email_input.get()
        password = self.password_input.get()

        # Check if user exists in the database
        query = "SELECT * FROM tuber_data WHERE email=%s AND password=%s"
        self.cursor.execute(query, (email, password))
        result = self.cursor.fetchone()

        if result:
            messagebox.showinfo("Login Success", "Welcome!")
            self.home_gui()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials")

    def home_gui(self):

        self.clear()

        heading =Label(self.root,text="Tuber App",bg='#7f8c8d',fg='white')
        heading.pack(pady=(20,20))
        heading.configure(font=('verdana',24,'bold'))

        sentiment_btn = Button(self.root,text="Sentiment",command=self.sentiment_gui)
        sentiment_btn.pack(pady=(10,10))

        ner_btn = Button(self.root,text="Named Entity Recognition",command=self.performing_login)
        ner_btn.pack(pady=(10,10))

        emotion_btn = Button(self.root,text="Emotion Prediction",command=self.performing_login)
        emotion_btn.pack(pady=(10,10))


        logout_btn = Button(self.root, text="logout",command=self.Login)
        logout_btn.pack(pady=(5,5))

    def sentiment_gui(self):
        self.clear()

        heading =Label(self.root,text="Tuber App",bg='#7f8c8d',fg='white')
        heading.pack(pady=(20,20))
        heading.configure(font=('verdana',24,'bold'))

        heading2 =Label(self.root,text="Sentiment Analysis",bg='#7f8c8d',fg='white')
        heading2.pack(pady=(20,20))
        heading2.configure(font=('verdana',20))

        label1= Label(self.root,text="Enter a Text",bg='#7f8c8d',fg='white')
        label1.pack(pady=(10,10))
        label1.configure(font=('verdana',13,'bold'))

        self.sentiment_input= Entry(self.root,width=30)
        self.sentiment_input.pack(pady=(10,10))

        sentiment_btn = Button(self.root, text="Sentiment Analyzer")
        sentiment_btn.pack(pady=(10,10))

        sentiment_result= Label(self.root,text="",bg='#7f8c8d',fg='white')
        sentiment_result.pack(pady=(10,10))
        sentiment_result.configure(font=('verdana',13,'bold'))

        goback_btn = Button(self.root, text="Go Back",command=self.home_gui)
        goback_btn.pack(pady=(10,10))




    def register_gui(self):
        self.clear()
        heading =Label(self.root,text="Tuber App",bg='#7f8c8d',fg='white')
        heading.pack(pady=(20,20))
        heading.configure(font=('verdana',24,'bold'))

        label0= Label(self.root,text="Enter Name")
        label0.pack(pady=(5,5))
        label0.configure(font=('verdana',13,'bold'))

        self.name_input= Entry(self.root,width=30)
        self.name_input.pack(pady=(5,5))


        label1= Label(self.root,text="Enter Email",bg='#7f8c8d',fg='white')
        label1.pack(pady=(10,10))
        label1.configure(font=('verdana',13,'bold'))

        self.email_input= Entry(self.root,width=30)
        self.email_input.pack(pady=(10,10))

        label2= Label(self.root,text="Enter Password",bg='#7f8c8d',fg='white')
        label2.pack(pady=(10,10))
        label2.configure(font=('verdana',13,'bold'))

        self.password_input= Entry(self.root,width=30,show="*")
        self.password_input.pack(pady=(10,10))

        register_btn = Button(self.root,text="Register",command=self.perform_registration)
        register_btn.pack(pady=(10,10))

        label3= Label(self.root,text="Already a Member ?",bg='#7f8c8d',fg='white')
        label3.pack(pady=(10,10))
        label3.configure(font=('verdana',13,'bold'))

        regbtn = Button(self.root, text="login",command=self.Login)
        regbtn.pack(pady=(5,5))





    def clear(self):

        # clear the existing GUI
        for i in self.root.pack_slaves():
            i.destroy()


    def perform_registration(self):
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        # Insert user data into database

        query = "insert into tuber_data(name,email,password) values (%s, %s, %s)"
        self.cursor.execute(query,(name,email,password))
        self.db.commit()

        messagebox.showinfo("Registration Success", "Account Created Successfully!")






nlp = NlpApp()