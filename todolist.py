# A simple to-do list written in Python using Tkinter GUI library

#import the libraries needed for this program to work
import tkinter
import tkinter.messagebox
import pickle

root = tkinter.Tk()
root.title('To Do List')

#Create functions for buttons
def add_task():
	task = entry_task.get()
	if task != '':
		listbox_tasks.insert(tkinter.END, task)
		entry_task.delete(0, tkinter.END)
	else:
		tkinter.messagebox.showwarning(title='Warning!', message = 'Enter a task to add.')

def delete_task():
	try:
		task_index = listbox_tasks.curselection()[0]
		listbox_tasks.delete(task_index)
	except:
		tkinter.messagebox.showwarning(title='Warning!', message = 'Enter a task to delete.')

#Use pickle to dump tasks into errands.txt
#Even saves a blank listbox when clicking it at the start of program (listbox will be empty by default on start of program)
def save_tasks():
	tasks = listbox_tasks.get(0, listbox_tasks.size())
	#print(tasks)
	if len(tasks) != 0:
		pickle.dump(tasks, open('errands.txt', 'wb'))
	else:
		tkinter.messagebox.showwarning(title='Warning!', message = 'Cannot save a blank list.')

#Use pickle again to load up saved tasks from errands.txt
def load_tasks():
	try:
		tasks = pickle.load(open('errands.txt','rb'))
		listbox_tasks.delete(0,tkinter.END)
		for task in tasks:
			listbox_tasks.insert(tkinter.END, task)
	except:
		tkinter.messagebox.showwarning(title='Warning!', message = 'errands.txt NOT FOUND.')

#Create GUI
frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

listbox_tasks = tkinter.Listbox(frame_tasks, height=3, width=50)
listbox_tasks.pack(side=tkinter.LEFT)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

#Next two lines of code makes the scroll bar functional with the Tkinter listbox
listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tkinter.Entry(root, width=50)
entry_task.pack()

#Create buttons
button_add_task = tkinter.Button(root, text = 'Add task', width=48, command = add_task)
button_add_task.pack()

button_delete_task = tkinter.Button(root, text = 'Delete task', width=48, command = delete_task)
button_delete_task.pack()

button_load_tasks = tkinter.Button(root, text = 'Load task', width=48, command = load_tasks)
button_load_tasks.pack()

button_save_tasks = tkinter.Button(root, text = 'Save task', width=48, command = save_tasks)
button_save_tasks.pack()

root.mainloop()
