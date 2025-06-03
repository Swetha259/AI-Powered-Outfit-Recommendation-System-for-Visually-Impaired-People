import csv
import time
from tkinter import *

import pyttsx3
import speech_recognition as sr
from PIL import Image, ImageTk


class shopping:
    gender = 'Female'
    size = 'xl'
    color = 'white'
    category=''
    name=''
    type=''
    rcolor=''
    pattern=''
    navigation=''
    description=''
    price=''
    offer=''

    def __init__(self):
        f = open("user_data.txt", "r")
        user_data=(f.read())
        xx = user_data.split('#')
        shopping.gender=xx[0]
        shopping.size=xx[1]
        shopping.color=xx[2]

        self.master = 'ar_master'
        self.title='Reccomendation system for blind people shopping'
        self.backround_color = '#2F4F4F'
        self.text_color = '#FFF'
        self.backround_image = 'images/background_hd1.jpg'
    def show_window(self):
        def get_voice_input():
            try:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    audio_data = r.record(source, duration=5)
                    text = r.recognize_google(audio_data)
                    print(text)
                return text
            except Exception as error:
                print(error)
                SpeakText('Incorrect Data')
                print("**")
                # get_voice_input()
        def get_csv_dress_category():
            data=[]
            shopping.gender=shopping.gender.lower().strip()
            shopping.size=shopping.size.lower().strip()
            shopping.color=shopping.color.lower().strip()
            file = 'vr_dataset.csv'
            with open(file) as f:
                reader = csv.DictReader(f, delimiter=',')
                for row in reader:
                    t1 = row['Gender'].lower().strip()
                    t2 = row['Size'].lower().strip()
                    t3 = row['Color'].lower().strip()
                    t4 = row['Dress Category'].lower()
                    if((t1==shopping.gender) and (t2==shopping.size) and (t3==shopping.color)):
                        data.append(t4.lower())
            data = list(set(data))
            return data
        def get_csv_dress_name():
            data=[]
            shopping.gender=shopping.gender.lower().strip()
            shopping.size=shopping.size.lower().strip()
            shopping.color=shopping.color.lower().strip()
            shopping.category=shopping.category.lower().strip()
            file = 'vr_dataset.csv'
            with open(file) as f:
                reader = csv.DictReader(f, delimiter=',')
                for row in reader:
                    t1 = row['Gender'].lower().strip()
                    t2 = row['Size'].lower().strip()
                    t3 = row['Color'].lower().strip()
                    t4 = row['Dress Category'].lower()
                    t5 = row['Dress name'].lower()
                    if((t1==shopping.gender) and (t2==shopping.size) and (t3==shopping.color) and (t4==shopping.category)):
                        data.append(t5.lower())
            data = list(set(data))
            return data
        def get_csv_dress_type():
            data=[]
            shopping.gender=shopping.gender.lower().strip()
            shopping.size=shopping.size.lower().strip()
            shopping.color=shopping.color.lower().strip()
            shopping.category=shopping.category.lower().strip()
            shopping.name=shopping.name.lower().strip()
            file = 'vr_dataset.csv'
            with open(file) as f:
                reader = csv.DictReader(f, delimiter=',')
                for row in reader:
                    t1 = row['Gender'].lower().strip()
                    t2 = row['Size'].lower().strip()
                    t3 = row['Color'].lower().strip()
                    t4 = row['Dress Category'].lower().strip()
                    t5 = row['Dress name'].lower().strip()
                    t6 = row['Dress type'].lower().strip()
                    if((t1==shopping.gender) and (t2==shopping.size) and (t3==shopping.color) and (t4==shopping.category) and (t5==shopping.name)):
                        data.append(t6.lower())
            data = list(set(data))
            return data
        def get_csv_dress_recommendation():
            data=[]
            shopping.gender=shopping.gender.lower().strip()
            shopping.size=shopping.size.lower().strip()
            shopping.color=shopping.color.lower().strip()
            shopping.category=shopping.category.lower().strip()
            shopping.name=shopping.name.lower().strip()
            shopping.type=shopping.type.lower().strip()
            file = 'vr_dataset.csv'
            with open(file) as f:
                reader = csv.DictReader(f, delimiter=',')
                for row in reader:
                    t1 = row['Gender'].lower().strip()
                    t2 = row['Size'].lower().strip()
                    t3 = row['Color'].lower().strip()
                    t4 = row['Dress Category'].lower().strip()
                    t5 = row['Dress name'].lower().strip()
                    t6 = row['Dress type'].lower().strip()
                    t7 = row['color'].lower().strip()
                    t8 = row['Pattern'].lower().strip()
                    t9 = row['Navigation'].lower().strip()
                    t10 = row['Description'].lower().strip()
                    t11 = row['Price'].lower().strip()
                    t12 = row['Offers'].lower().strip()
                    if((t1==shopping.gender) and (t2==shopping.size) and (t3==shopping.color) and (t4==shopping.category) and (t5==shopping.name) and (t6==shopping.type)):
                        shopping.rcolor=t7.lower()
                        shopping.pattern=t8.lower()
                        shopping.navigation=t9.lower()
                        shopping.description=t10.lower()
                        shopping.price=t11.lower()
                        shopping.offer=t12.lower()

            data = list(set(data))
            return data

        # Text-to-speech function
        def SpeakText(command, gui_root=None):
            if gui_root:
                gui_root.update()
            engine = pyttsx3.init()
            engine.say(command)
            engine.runAndWait()
            engine.stop()

        # Dress category selection (with user input)
        def select_dress_category():
            data = get_csv_dress_category()
            SpeakText("Listen to your Dress Category List.", user_home_root)

            for item in data:
                SpeakText(item, user_home_root)
                time.sleep(1)
            if data:
                SpeakText("Please, enter your choice.", user_home_root)
                time.sleep(5)
                SpeakText(data[0], user_home_root)
                return data[0]
            else:
                SpeakText("No dress categories found.", user_home_root)
                return None

        #########################################################################################################
        #########################################################################################################
        #########################################################################################################

        def welcome_note():
            first_text = "Welcome, to Blind People Recommendation System"
            SpeakText(first_text, user_home_root)
            user_home_root.update()
            canvas1.update()

            ############################################ Dress Category
            cdate1 = canvas1.create_text(100, 220, text=str("Category - " + str(shopping.category)),
                                         font=("Times New Roman", 18), fill='#FFF')
            canvas1.update()

            category_list = get_csv_dress_category()
            dress_category = select_dress_category()
            print(dress_category)
            if dress_category in category_list:
                shopping.category = dress_category
                canvas1.itemconfigure(cdate1, text=str("Category - " + shopping.category))
                canvas1.update()
            else:
                SpeakText("Sorry, data is incorrect.", user_home_root)
                welcome_note()  # Restart

            user_home_root.update()
            canvas1.update()
            time.sleep(1)

            # Dress Name Selection
            SpeakText("Available dress name.", user_home_root)
            name_list = get_csv_dress_name()
            if name_list:
                shopping.name = name_list[0]
                SpeakText(shopping.name, user_home_root)
            canvas1.create_text(110, 270, text=f"Dress Name - {shopping.name}", font=("Times New Roman", 18),
                                fill='#FFF')
            canvas1.update()

            # Dress Type Selection
            SpeakText("Available dress type.", user_home_root)
            type_list = get_csv_dress_type()
            if type_list:
                shopping.type = type_list[0]
                SpeakText(shopping.type, user_home_root)
            canvas1.create_text(120, 320, text=f"Dress Type - {shopping.type}", font=("Times New Roman", 18),
                                fill='#FFF')
            canvas1.update()

            # Dress Recommendation
            dress_recommendation = get_csv_dress_recommendation()

            SpeakText("Recommended color: " + shopping.rcolor, user_home_root)
            canvas1.create_text(150, 370, text=f"Recommended Color - {shopping.rcolor}", font=("Times New Roman", 18),
                                fill='#FFF')
            canvas1.update()
            time.sleep(1)

            SpeakText("Recommended pattern: " + shopping.pattern, user_home_root)
            canvas1.create_text(160, 420, text=f"Recommended Pattern - {shopping.pattern}",
                                font=("Times New Roman", 18), fill='#FFF')
            canvas1.update()
            time.sleep(1)

            SpeakText("Navigation: " + shopping.navigation, user_home_root)
            SpeakText("Description: " + shopping.description, user_home_root)

            # Ask before price and offer details
            SpeakText("Do you want to hear the price and offer details? Say yes to continue.", user_home_root)
            time.sleep(5)  # Wait for 5 seconds

            # Now speak and display the price and offer
            SpeakText("Price detail: " + shopping.price, user_home_root)
            canvas1.create_text(100, 470, text=f"Price - {shopping.price}", font=("Times New Roman", 18), fill='#FFF')
            canvas1.update()

            SpeakText("Offer detail: " + shopping.offer, user_home_root)
            canvas1.create_text(100, 520, text=f"Offers - {shopping.offer}", font=("Times New Roman", 18), fill='#FFF')
            canvas1.update()



            SpeakText("Thank you", user_home_root)

        def call_auto_function():
            user_home_root.update()
            canvas1.update()
            user_home_root.after_idle(welcome_note)

        ##################################################################
        # from datetime import datetime
        # now = datetime.now()
        # dt_string = now.strftime("%Y_%m_%d")
        user_home_root = Toplevel()
        user_home_root.attributes('-topmost', 'true')
        w = 1000
        h = 600
        ws = user_home_root.winfo_screenwidth()
        hs = user_home_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        user_home_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        image = Image.open('images/background_hd1.jpg')
        img = image.resize((w, h))
        my_img = ImageTk.PhotoImage(img)
        user_home_root.resizable(False, False)
        canvas1 = Canvas(user_home_root, width=200, height=300)
        canvas1.create_image(0, 0, image=my_img, anchor=NW)
        canvas1.pack(fill="both", expand=True)
        admin_id2 = canvas1.create_text(390, 20, text="USER HOME", font=("Times New Roman", 24), fill='#FFF')
        cdate = canvas1.create_text(100, 70, text=str("Gender - "+str(shopping.gender)), font=("Times New Roman", 18), fill='#FFF')
        cdate = canvas1.create_text(100, 120, text=str("Size - "+str(shopping.size)), font=("Times New Roman", 18), fill='#FFF')
        cdate = canvas1.create_text(100, 170, text=str("Color - "+str(shopping.color)), font=("Times New Roman", 18), fill='#FFF')
        ###############
        lbl2 = Label(user_home_root)
        a1 = Image.open('images/logo.png')
        a123 = a1.resize((100, 100), Image.Resampling.LANCZOS)
        a12 = ImageTk.PhotoImage(a123)
        lbl2.configure(image=a12)
        lbl2.place(x=555, y=15)
        ######################################################################################################

        user_home_root.after(1000,call_auto_function)
        user_home_root.mainloop()


ar=shopping()
ar.show_window()