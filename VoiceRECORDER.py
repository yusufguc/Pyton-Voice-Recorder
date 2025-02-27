from tkinter import *
from tkinter import messagebox
import sounddevice as sound
from scipy.io.wavfile import write
import time


root=Tk()
root.geometry("400x500")
root.resizable(False,False)
root.title("VOICE RECORDER")
root.configure(bg="#d4f4dd")

def record():
    freq=44100
    dur=int(drt.get())
    recording=sound.rec(dur*freq,
                        samplerate=freq,channels=2)
    try:
        temp=int(drt.get())
    except:
        print("please enter the right value")

    while temp>0:
        root.update()
        time.sleep(1)
        temp-=1

        if temp==0:
            messagebox.showinfo("Time Countdown","Time's up")
        Label(text=f"{str(temp)}",font="arial 40",width=4,background="#d4f4dd").place(x=135,y=390)
    sound.wait()
    write("recording.wav",freq,recording)



#icon
image_icon=PhotoImage(file="icons8-microphone-50.png")
root.iconphoto(False,image_icon)

#logo
label_photo=PhotoImage(file="icons8-microphone-100.png")
Label(root,image=label_photo,bg="#d4f4dd").pack(padx=10,pady=10)

Label(text="Voice Recorder",fg="black",bg="#d4f4dd", font=("Helvetica", 25, "bold")).pack()               

drt=StringVar()
entry=Entry(root,textvariable=drt,font="arial 30",width=15).pack(pady=10)

Label(text="Enter time in second",fg="black",bg="#d4f4dd", font=("Helvetica", 13,)).pack()

Button(root,text="RECORD",bg="black",fg="white",font=("Helvetica", 15,),border=0,command=record).pack(pady=30)



root.mainloop()
