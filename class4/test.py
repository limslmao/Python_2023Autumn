import tkinter as tk

def on_open():
    print("Tkinter is working!")

root = tk.Tk()
root.title("Test Window")

# 設置視窗的最小尺寸
root.geometry("300x200")

label = tk.Label(root, text="Hello, Tkinter!", bg="yellow")  # 添加背景色以便更明顯
label.pack(padx=10, pady=10)  # 添加一些間隔

button = tk.Button(root, text="Click Me", command=lambda: label.config(text="Button Clicked!"))
button.pack(pady=10)

root.after(1000, on_open)  # 延遲 1 秒後調用 on_open
root.mainloop()
