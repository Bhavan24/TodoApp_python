import tkinter as tk
import tkinter.font as tkFont


tasks_list = []
task_no = 1
     

def btnSubmit_command():
    global task_no
    task = textInput.get() + "\n"
    tasks_list.append(task)
    textList.insert('end -1 chars',f"({task_no}) {task}")
    task_no += 1
    textInput.delete(0, 'end')


def btnDelete_command():
    global task_no

    number = int(textNum.get())
    textNum.delete(0, 'end')      

    tasks_list.pop(number - 1) 
    task_no -= 1
    textList.delete(1.0, tk.END) 

    for i in range(len(tasks_list)) : 
        textList.insert('end -1 chars',f'({str(i+1)}) {tasks_list[i]}') 



def btnSave_command():
    with open('todo.txt', 'w') as file_out:
        for line in tasks_list:
            file_out.write(line)



if __name__ == "__main__" :
    root = tk.Tk()

    root.title("To-do Application")
    root.geometry("600x500")
    root.resizable(width=False, height=False)

    text1 = tk.Label(root)
    ft = tkFont.Font(family='Times',size=20)
    text1["font"] = ft
    text1["fg"] = "#333333"
    text1["justify"] = "center"
    text1["text"] = "Enter Your Task"
    text1.place(x=30,y=20,width=186,height=47)

    textInput = tk.Entry(root)
    textInput["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=18)
    textInput["font"] = ft
    textInput["fg"] = "#333333"
    textInput["justify"] = "left"
    textInput["text"] = ""
    textInput.place(x=240,y=20,width=340,height=47)

    btnSubmit = tk.Button(root)
    btnSubmit["bg"] = "#8cf717"
    ft = tkFont.Font(family='Times',size=23)
    btnSubmit["font"] = ft
    btnSubmit["fg"] = "#000000"
    btnSubmit["justify"] = "center"
    btnSubmit["text"] = "SUBMIT"
    btnSubmit["relief"] = "groove"
    btnSubmit.place(x=240,y=80,width=117,height=44)
    btnSubmit["command"] = btnSubmit_command

    textList = tk.Text(root)
    textList["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=18)
    textList["font"] = ft
    textList["fg"] = "#333333"
    textList.place(x=30,y=140,width=549,height=232)

    btnDelete = tk.Button(root)
    btnDelete["bg"] = "#ff0a0a"
    ft = tkFont.Font(family='Times',size=18)
    btnDelete["font"] = ft
    btnDelete["fg"] = "#000000"
    btnDelete["justify"] = "center"
    btnDelete["text"] = "Delete Task"
    btnDelete.place(x=250,y=400,width=150,height=50)
    btnDelete["command"] = btnDelete_command

    textNum = tk.Entry(root)
    textNum["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=16)
    textNum["font"] = ft
    textNum["fg"] = "#333333"
    textNum.place(x=190,y=400,width=50,height=50)

    text3 = tk.Label(root)
    ft = tkFont.Font(family='Times',size=20)
    text3["font"] = ft
    text3["fg"] = "#333333"
    text3["justify"] = "center"
    text3["text"] = "Task Number: "
    text3.place(x=10,y=400,width=169,height=51)

    btnSave = tk.Button(root)
    btnSave["bg"] = "#eddc1c"
    ft = tkFont.Font(family='Times',size=23)
    btnSave["font"] = ft
    btnSave["fg"] = "#000000"
    btnSave["justify"] = "center"
    btnSave["text"] = "Save to file"
    btnSave.place(x=440,y=390,width=150,height=87)
    btnSave["command"] = btnSave_command
        
    root.mainloop()