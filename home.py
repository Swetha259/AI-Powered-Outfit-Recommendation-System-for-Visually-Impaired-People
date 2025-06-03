from tkinter import *
import numpy as np
from PIL import Image, ImageTk
import cv2
import mediapipe as mp
import pyttsx3  # ✅ NEW

# ✅ Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

class tk_master:
    name='ar_master'
    gender=''
    size=''
    color=''

    def __init__(self):
        self.master = 'ar_master'
        self.title = 'Reccomendation System For Blind Shopping'
        self.titlec = 'VR BLIND SHOPPING'
        self.backround_color = '#2F4F4F'
        self.text_color = '#FFF'
        self.backround_image = 'images/background_hd1.jpg'

    def get_title(self):
        return self.title

    def get_titlec(self):
        return self.titlec

    def get_backround_color(self):
        return self.backround_color

    def get_text_color(self):
        return self.text_color

    def get_backround_image(self):
        return self.backround_image

    def set_window_design(self):
        root = Tk()
        w = 780
        h = 500
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.bg = ImageTk.PhotoImage(file='images/background_hd1.jpg')
        root.title(self.title)
        root.resizable(False, False)
        bg = ImageTk.PhotoImage(file=self.backround_image)
        canvas = Canvas(root, width=200, height=300)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor=NW)
        canvas.create_text(390, 20, text=self.title, font=("Times New Roman", 24), fill=self.text_color)

        def clickHandler(event):
            tt = tk_master
            tt.login_home(event)

        image = Image.open('images/logo.png')
        img = image.resize((225, 225))
        my_img = ImageTk.PhotoImage(img)
        image_id = canvas.create_image(380, 200, image=my_img)
        canvas.tag_bind(image_id, "<1>", clickHandler)
        admin_id = canvas.create_text(380, 360, text="Start", font=("Times New Roman", 28), fill=self.text_color)
        canvas.tag_bind(admin_id, "<1>", clickHandler)
        root.mainloop()

    def login_home(self, event=None):
        def categorize_skin_color(image, face_region):
            x, y, w, h = face_region
            roi = image[y:y + h, x:x + w]
            ycrcb = cv2.cvtColor(roi, cv2.COLOR_BGR2YCrCb)
            y_mean = np.mean(ycrcb[:, :, 0])
            cr_mean = np.mean(ycrcb[:, :, 1])
            cb_mean = np.mean(ycrcb[:, :, 2])
            if y_mean > 180 and cr_mean > 130 and cr_mean < 170 and cb_mean > 77 and cb_mean < 127:
                return "White"
            elif y_mean > 120 and cr_mean > 100 and cr_mean < 150 and cb_mean > 90 and cb_mean < 130:
                return "Brown"
            elif y_mean < 120 and cr_mean > 130 and cr_mean < 170 and cb_mean > 77 and cb_mean < 127:
                return "Black"
            else:
                return "Fair"

        def highlightFace(net, frame, conf_threshold=0.7):
            frameOpencvDnn = frame.copy()
            frameHeight = frameOpencvDnn.shape[0]
            frameWidth = frameOpencvDnn.shape[1]
            blob = cv2.dnn.blobFromImage(frameOpencvDnn, 1.0, (300, 300), [104, 117, 123], True, False)
            net.setInput(blob)
            detections = net.forward()
            faceBoxes = []
            for i in range(detections.shape[2]):
                confidence = detections[0, 0, i, 2]
                if confidence > conf_threshold:
                    x1 = int(detections[0, 0, i, 3] * frameWidth)
                    y1 = int(detections[0, 0, i, 4] * frameHeight)
                    x2 = int(detections[0, 0, i, 5] * frameWidth)
                    y2 = int(detections[0, 0, i, 6] * frameHeight)
                    faceBoxes.append([x1, y1, x2, y2])
                    cv2.rectangle(frameOpencvDnn, (x1, y1), (x2, y2), (0, 255, 0), int(round(frameHeight / 150)), 8)
            return frameOpencvDnn, faceBoxes

        total_frame_count = 30
        count = 0
        faceProto = "ar_model_gender/opencv_face_detector.pbtxt"
        faceModel = "ar_model_gender/opencv_face_detector_uint8.pb"
        genderProto = "ar_model_gender/gender_deploy.prototxt"
        genderModel = "ar_model_gender/gender_net.caffemodel"
        MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
        genderList = ['Male', 'Female']
        faceNet = cv2.dnn.readNet(faceModel, faceProto)
        genderNet = cv2.dnn.readNet(genderModel, genderProto)
        video = cv2.VideoCapture(0)
        padding = 20

        size_dict = {"s": 0, "m": 0, "l": 0, "xl": 0, "xxl": 0, "xxxl": 0}
        gender_dict = {"Male": 0, "Female": 0}
        color_dict = {"White": 0, "Black": 0, "Brown": 0, "Fair": 0,  "Other": 0}
        upper_body_cascade = cv2.CascadeClassifier('data/haarcascades/haarcascade_mcs_upperbody.xml')
        cascPath = "data/haarcascades/haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascPath)

        check_distance = 0
        find_sholder = 0
        last_instruction = None  # ✅ NEW: Track last spoken command

        while 1:
            ret, frame = video.read()
            height, width = frame.shape[:2]
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            resultImg, faceBoxes = highlightFace(faceNet, frame)

            frame_center_w = width / 2
            frame_left2_w = frame_center_w / 2
            frame_left1_w = frame_left2_w / 2
            left_edge_w = frame_left1_w + frame_left2_w
            start_point_h = (int(left_edge_w), 10)
            end_point_h = (int(left_edge_w), height - 10)
            cv2.line(resultImg, start_point_h, end_point_h, (0, 0, 0), 1)

            if check_distance == 0:
                upper_bodies = upper_body_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
                for (x, y, w, h) in upper_bodies:
                    cv2.rectangle(resultImg, (x, y), (x + w, y + h), (0, 255, 255), 2)
                    if left_edge_w + 10 < x:
                        body_type = 'Move Right'
                    elif left_edge_w - 10 > x:
                        body_type = 'Move Left'
                    else:
                        body_type = 'Ok'
                        find_sholder = 1

                    # ✅ Speak if instruction changes
                    if body_type != last_instruction:
                        speak(body_type)
                        last_instruction = body_type

                    cv2.putText(resultImg, f'{body_type}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 1, cv2.LINE_AA)

                    tmp_sholder = w / 5
                    if find_sholder == 1:
                        find_sholder = 0
                        sholder = tmp_sholder
                        sholder_result = "unknown"
                        if (sholder < 54):
                            sholder_result = 's'
                        elif (sholder < 58):
                            sholder_result = 'm'
                        elif (sholder < 62):
                            sholder_result = 'l'
                        elif (sholder < 66):
                            sholder_result = 'xl'
                        elif (sholder < 84):
                            sholder_result = 'xxl'
                        else:
                            sholder_result = 'xl'

                        size_dict[sholder_result] += 1
                        count += 1
                        if count > 40:
                            Keymax = max(zip(size_dict.values(), size_dict.keys()))[1]
                            cv2.putText(resultImg, Keymax, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                            tk_master.size = str(Keymax)

            for faceBox in faceBoxes:
                face = frame[max(0, faceBox[1] - padding):min(faceBox[3] + padding, frame.shape[0] - 1),
                       max(0, faceBox[0] - padding):min(faceBox[2] + padding, frame.shape[1] - 1)]
                blob = cv2.dnn.blobFromImage(face, 1.0, (227, 227), MODEL_MEAN_VALUES, swapRB=False)
                genderNet.setInput(blob)
                genderPreds = genderNet.forward()
                gender = genderList[genderPreds[0].argmax()]
                gender_dict[gender] += 1
                count += 1
                if count > total_frame_count:
                    Keymax = max(zip(gender_dict.values(), gender_dict.keys()))[1]
                    tk_master.gender = str(Keymax)
                cv2.putText(resultImg, f'{gender}', (faceBox[0], faceBox[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 1, cv2.LINE_AA)

                faces = faceCascade.detectMultiScale(frame, 1.1, 3, minSize=(100, 100))
                for (x, y, w, h) in faces:
                    category = categorize_skin_color(frame, (x, y, w, h))
                    color_dict[category] += 1

            cv2.imshow("Image1", resultImg)
            if tk_master.gender != '' and tk_master.size != '':
                Keymax2 = max(zip(color_dict.values(), color_dict.keys()))[1]
                tk_master.color = str(Keymax2)
                break

            if cv2.waitKey(30) & 0xff == 27:
                break

        with open("user_data.txt", "w") as file1:
            file1.writelines([tk_master.gender + "#" + tk_master.size + "#" + tk_master.color])

        video.release()
        cv2.destroyAllWindows()

        if tk_master.size != '':
            import dress_shopping
            ar = dress_shopping.shopping()
            ar.show_window()

ar = tk_master()
root = ar.set_window_design()
