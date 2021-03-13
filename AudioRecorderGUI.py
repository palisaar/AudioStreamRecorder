import tkinter as tk
import AudioRecorder

'''
Autor: Lennart Palisaar
20211638
'''


# funktionalitaet des record button
def on_click():
    try:
        temp_name = name.get()
        temp_url = url.get()
        temp_len = int(len.get())
        temp_bg = int(bg.get())
        print('recording imminent')
        AudioRecorder.record_audio(temp_name, temp_url, temp_len, temp_bg)
    except:
        raise ValueError('name or url is null')


# gui
master = tk.Tk()
tk.Label(master,
         text="Name").grid(row=0)
tk.Label(master,
         text="Url").grid(row=1)
tk.Label(master,
         text="Len (sec)").grid(row=2)
tk.Label(master,
         text="Block gr").grid(row=3)

name = tk.Entry(master)
url = tk.Entry(master)
len = tk.Entry(master)
bg = tk.Entry(master)

bg.insert(0, "40")
len.insert(0, "10")

name.grid(row=0, column=1)
url.grid(row=1, column=1)
len.grid(row=2, column=1)
bg.grid(row=3, column=1)

tk.Button(master,
          text='Record', command=on_click).grid(row=4,
                                                column=1,
                                                sticky=tk.W,
                                                pady=4)

tk.mainloop()
