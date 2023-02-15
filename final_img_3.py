import tkinter as tk
from tkinter.filedialog import askopenfilename
import shutil
import os
import sys
from PIL import Image, ImageTk

window = tk.Tk()

window.title("Dr. Plant")

window.geometry("700x710")
window.configure(background ="lightgray")

title = tk.Label(text="Click below to choose picture for testing disease....", background = "lightgray", fg="Brown", font=("", 15))
title.grid()
def bact_viru():
    window.destroy()
    window1 = tk.Tk()

    window1.title("Dr. Plant")

    window1.geometry("900x510")
    window1.configure(background="lightgray")

    def exit():
        window1.destroy()
    rem = "The remedies for yellow to white patches are:\n\n "
    remedies = tk.Label(text=rem, background="lightgreen",
                      fg="Brown", font=("", 15))
    remedies.grid(column=0, row=7, padx=10, pady=10)
    rem1 = " Discard or destroy any affected plants. \n  Spray infected plants with fungicides. \n  Effective organic fungicides for treating powdery mildew include sulfur, lime-sulfur, neem oil, and potassium bicarbonate."
    remedies1 = tk.Label(text=rem1, background="lightgreen",
                        fg="Black", font=("", 12))
    remedies1.grid(column=0, row=8, padx=10, pady=10)

    button = tk.Button(text="Exit", command=exit)
    button.grid(column=0, row=9, padx=20, pady=20)

    window1.mainloop()

def fung_viru():
    window.destroy()
    window1 = tk.Tk()

    window1.title("Dr. Plant")

    window1.geometry("900x510")
    window1.configure(background="lightgray")

    def exit():
        window1.destroy()
    rem = "The remedies for The fungal disease powdery mildew are:\n "
    remedies = tk.Label(text=rem, background="lightgreen",
                      fg="Brown", font=("", 15))
    remedies.grid(column=0, row=7, padx=10, pady=10)
    rem1 = " Discard or destroy any affected plants. \n  Do not compost them. \n  Rotate yoour tomato plants yearly to prevent re-infection next year. \n Use copper fungicites"
    remedies1 = tk.Label(text=rem1, background="lightgreen",
                        fg="Black", font=("", 12))
    remedies1.grid(column=0, row=8, padx=10, pady=10)

    button = tk.Button(text="Exit", command=exit)
    button.grid(column=0, row=9, padx=20, pady=20)

    window1.mainloop()

def bligh():
    window.destroy()
    window1 = tk.Tk()

    window1.title("Dr. Plant")

    window1.geometry("900x510")
    window1.configure(background="lightgray")

    def exit():
        window1.destroy()
    rem = "The remedies for water-soaked, gray-green spots are:\n\n "
    remedies = tk.Label(text=rem, background="lightgreen",
                      fg="Brown", font=("", 15))
    remedies.grid(column=0, row=7, padx=10, pady=10)
    rem1 = " Plant resistant cultivars when available. \n  Remove volunteers from the garden prior to planting and space plants far enough apart to allow for plenty of air circulation. \n  Water in the early morning hours, or use soaker hoses, to give plants time to dry out during the day — avoid overhead irrigation"
    remedies1 = tk.Label(text=rem1, background="lightgreen",
                        fg="Black", font=("", 12))
    remedies1.grid(column=0, row=8, padx=10, pady=10)

    button = tk.Button(text="Exit", command=exit)
    button.grid(column=0, row=9, padx=20, pady=20)

    window1.mainloop()

def bact():
    window.destroy()
    window1 = tk.Tk()

    window1.title("Dr. Plant")

    window1.geometry("900x510")
    window1.configure(background="lightgray")

    def exit():
        window1.destroy()
    rem = "The remedies for Bacterial Spot are:\n\n "
    remedies = tk.Label(text=rem, background="lightgreen",
                      fg="Brown", font=("", 15))
    remedies.grid(column=0, row=7, padx=10, pady=10)
    rem1 = " Discard or destroy any affected plants. \n  Do not compost them. \n  Rotate yoour tomato plants yearly to prevent re-infection next year. \n Use copper fungicites"
    remedies1 = tk.Label(text=rem1, background="lightgreen",
                        fg="Black", font=("", 12))
    remedies1.grid(column=0, row=8, padx=10, pady=10)

    button = tk.Button(text="Exit", command=exit)
    button.grid(column=0, row=9, padx=20, pady=20)

    window1.mainloop()


def vir():
    window.destroy()
    window1 = tk.Tk()

    window1.title("Dr. Plant")

    window1.geometry("900x510")
    window1.configure(background="lightgray")

    def exit():
        window1.destroy()
    rem = "The remedies for Yellow leaf curl virus are: "
    remedies = tk.Label(text=rem, background="lightgreen",
                      fg="Brown", font=("", 15))
    remedies.grid(column=0, row=7, padx=10, pady=10)
    rem1 = " Monitor the field, handpick diseased plants and bury them. \n  Use sticky yellow plastic traps. \n  Spray insecticides such as organophosphates, carbametes during the seedliing stage. \n Use copper fungicites"
    remedies1 = tk.Label(text=rem1, background="lightgreen",
                         fg="Black", font=("", 12))
    remedies1.grid(column=0, row=8, padx=10, pady=10)

    button = tk.Button(text="Exit", command=exit)
    button.grid(column=0, row=9, padx=20, pady=20)

    window1.mainloop()

def latebl():
    window.destroy()
    window1 = tk.Tk()

    window1.title("Dr. Plant")

    window1.geometry("900x510")
    window1.configure(background="lightgray")

    def exit():
        window1.destroy()
    rem = "The remedies for Late Blight are: "
    remedies = tk.Label(text=rem, background="lightgreen",
                      fg="Brown", font=("", 15))
    remedies.grid(column=0, row=7, padx=10, pady=10)

    rem1 = " Monitor the field, remove and destroy infected leaves. \n  Treat organically with copper spray. \n  Use chemical fungicides,the best of which for tomatoes is chlorothalonil."
    remedies1 = tk.Label(text=rem1, background="lightgreen",
                         fg="Black", font=("", 12))
    remedies1.grid(column=0, row=8, padx=10, pady=10)

    button = tk.Button(text="Exit", command=exit)
    button.grid(column=0, row=9, padx=20, pady=20)

    window1.mainloop()


def analysis():
    import cv2  # working with, mainly resizing, images
    import numpy as np  # dealing with arrays
    import os  # dealing with directories
    from random import shuffle  # mixing up or currently ordered data that might lead our network astray in training.
    from tqdm import \
        tqdm  # a nice pretty percentage bar for tasks. Thanks to viewer Daniel BA1/4hler for this suggestion
    verify_dir = 'testpicture'
    IMG_SIZE = 50
    LR = 1e-3
    MODEL_NAME = 'healthyvsunhealthy-{}-{}.model'.format(LR, '2conv-basic')

    def process_verify_data():
        verifying_data = []
        for img in tqdm(os.listdir(verify_dir)):
            path = os.path.join(verify_dir, img)
            img_num = img.split('.')[0]
            img = cv2.imread(path, cv2.IMREAD_COLOR)
            img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
            verifying_data.append([np.array(img), img_num])
        np.save('verify_data.npy', np.array(verifying_data, dtype=object))
        return verifying_data

    verify_data = process_verify_data()
    #verify_data = np.load('verify_data.npy')

    import tflearn
    from tflearn.layers.conv import conv_2d, max_pool_2d
    from tflearn.layers.core import input_data, dropout, fully_connected
    from tflearn.layers.estimator import regression
    import tensorflow as tf
    tf.reset_default_graph()

    convnet = input_data(shape=[None, IMG_SIZE, IMG_SIZE, 3], name='input')

    convnet = conv_2d(convnet, 32, 3, activation='relu')
    convnet = max_pool_2d(convnet, 3)

    convnet = conv_2d(convnet, 64, 3, activation='relu')
    convnet = max_pool_2d(convnet, 3)

    convnet = conv_2d(convnet, 128, 3, activation='relu')
    convnet = max_pool_2d(convnet, 3)

    convnet = conv_2d(convnet, 32, 3, activation='relu')
    convnet = max_pool_2d(convnet, 3)

    convnet = conv_2d(convnet, 64, 3, activation='relu')
    convnet = max_pool_2d(convnet, 3)

    convnet = fully_connected(convnet, 1024, activation='relu')
    convnet = dropout(convnet, 0.8)

    convnet = fully_connected(convnet, 4, activation='softmax')
    convnet = regression(convnet, optimizer='adam', learning_rate=LR, loss='categorical_crossentropy', name='targets')

    model = tflearn.DNN(convnet, tensorboard_dir='log')

    if os.path.exists('{}.meta'.format(MODEL_NAME)):
        model.load(MODEL_NAME)
        print('model loaded!')

    import matplotlib.pyplot as plt

    fig = plt.figure()

    for num, data in enumerate(verify_data):

        img_num = data[1]
        img_data = data[0]

        y = fig.add_subplot(3, 4, num + 1)
        orig = img_data
        data = img_data.reshape(IMG_SIZE, IMG_SIZE, 3)
       # print (data)
        # model_out = model.predict([data])[0]
        model_out = model.predict([data])[0]
        print(model_out)
        print(np.argmax(model_out))
        if np.argmax(model_out) == 0:
            str_label = 'healthy'
        elif np.argmax(model_out) == 1:
            str_label = 'bacterial_virus'
        elif np.argmax(model_out) == 2:
            str_label = 'fungal'
        elif np.argmax(model_out) == 3:
            str_label = 'blights'
        elif np.argmax(model_out) == 4:
            str_label = 'bacterial'
        elif np.argmax(model_out) == 5:
            str_label = 'viral'
        elif np.argmax(model_out) == 6:
            str_label = 'lateblight'


        if str_label =='healthy':
            status ="HEALTHY"
        else:
            status = "UNHEALTHY"

        message = tk.Label(text='Status: '+status, background="lightgreen",
                           fg="Brown", font=("", 15))
        message.grid(column=1, row=4, padx=10, pady=10)
        if str_label == 'bacterial_virus':
            diseasename = "Downy Mildew "
            disease = tk.Label(text='Disease Name: ' + diseasename, background="lightgreen",
                               fg="Black", font=("", 15))
            disease.grid(column=1, row=5, padx=10, pady=10)
            r = tk.Label(text='Click below for remedies...', background="lightgreen", fg="Brown", font=("", 15))
            r.grid(column=1, row=6, padx=10, pady=10)
            button3 = tk.Button(text="Remedies", command=bact_viru)
            button3.grid(column=0, row=3, padx=10, pady=10)
        elif str_label == 'fungal':
            diseasename = "POWDERY MILDEW "
            disease = tk.Label(text='Disease Name: ' + diseasename, background="lightgreen",
                               fg="Black", font=("", 15))
            disease.grid(column=1, row=5, padx=10, pady=10)
            r = tk.Label(text='Click below for remedies...', background="lightgreen", fg="Brown", font=("", 15))
            r.grid(column=1, row=6, padx=10, pady=10)
            button3 = tk.Button(text="Remedies", command=fung_viru)
            button3.grid(column=0, row=3, padx=10, pady=10)
        elif str_label == 'blights':
            diseasename = "Leaf Blights "
            disease = tk.Label(text='Disease Name: ' + diseasename, background="lightgreen",
                               fg="Black", font=("", 15))
            disease.grid(column=1, row=5, padx=10, pady=10)
            r = tk.Label(text='Click below for remedies...', background="lightgreen", fg="Brown", font=("", 15))
            r.grid(column=1, row=6, padx=10, pady=10)
            button3 = tk.Button(text="Remedies", command=bligh)
            button3.grid(column=0, row=3, padx=10, pady=10)
        elif str_label == 'bacterial':
            diseasename = "Bacterial Spot "
            disease = tk.Label(text='Disease Name: ' + diseasename, background="lightgreen",
                               fg="Black", font=("", 15))
            disease.grid(column=1, row=5, padx=10, pady=10)
            r = tk.Label(text='Click below for remedies...', background="lightgreen", fg="Brown", font=("", 15))
            r.grid(column=1, row=6, padx=10, pady=10)
            button3 = tk.Button(text="Remedies", command=bact)
            button3.grid(column=0, row=3, padx=10, pady=10)
        elif str_label == 'viral':
            diseasename = "Yellow leaf curl virus "
            disease = tk.Label(text='Disease Name: ' + diseasename, background="lightgreen",
                               fg="Black", font=("", 15))
            disease.grid(column=1, row=5, padx=10, pady=10)
            r = tk.Label(text='Click below for remedies...', background="lightgreen", fg="Brown", font=("", 15))
            r.grid(column=1, row=6, padx=10, pady=10)
            button3 = tk.Button(text="Remedies", command=vir)
            button3.grid(column=0, row=3, padx=10, pady=10)
        elif str_label == 'lateblight':
            diseasename = "Late Blight "
            disease = tk.Label(text='Disease Name: ' + diseasename, background="lightgreen",
                               fg="Black", font=("", 15))
            disease.grid(column=1, row=5, padx=10, pady=10)
            r = tk.Label(text='Click below for remedies...', background="lightgreen", fg="Brown", font=("", 15))
            r.grid(column=1, row=6, padx=10, pady=10)
            button3 = tk.Button(text="Remedies", command=latebl)
            button3.grid(column=0, row=3, padx=10, pady=10)
        else:
            r = tk.Label(text='Plant is healthy', background="lightgreen", fg="Black",
                         font=("", 15))
            r.grid(column=1, row=6, padx=10, pady=10)
            button = tk.Button(text="Exit", command=exit)
            button.grid(column=1, row=9, padx=20, pady=20)

def openphoto():
    dirPath = "testpicture"
    fileList = os.listdir(dirPath)
    for fileName in fileList:
        os.remove(dirPath + "/" + fileName)
    # C:/Users/user/Desktop/Ramesh/ is the location of the image which you want to test..... you can change it according to the image location you have  
    fileName = askopenfilename(initialdir='testpicture', title='Select image for analysis ',
                           filetypes=[('image files', '.jpg')])
    dst = "testpicture"
    shutil.copy(fileName, dst)
    load = Image.open(fileName)
    render = ImageTk.PhotoImage(load)
    img = tk.Label(image=render, height="500", width="500")
    img.image = render
    img.place(x=0, y=0)
    img.grid(column=1, row=1, padx=10, pady = 10)
    title.destroy()
    button1.destroy()
    button2 = tk.Button(text="Analyse Image", command=analysis)
    button2.grid(column=0, row=1, padx=10, pady = 10)
button1 = tk.Button(text="Get Photo", command = openphoto)
button1.grid(column=0, row=1, padx=20, pady = 20)



window.mainloop()



