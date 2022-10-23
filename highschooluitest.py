from tkinter import *
from tkinter import ttk
import json
import os

with open('highschoolclasses2.json', 'r') as in_file:
    masterlist = json.load(in_file)

frame = Tk()
frame.title("High school courses")
frame.geometry('500x400')

def get_courses(type="all"):
    if type == "all":
    
        names = [p['name'] for p in masterlist['courses']]
    else:
        names = [p['name'] for p in masterlist['courses'] if type in p['credit']]
    return names

def get_year(type="all"):
    if type == "all":
        names = [p['name'] for p in masterlist['courses']]
    else:
        names = [p['name'] for p in masterlist['courses'] if type in p['year']]
    return names

def get_both(x,y):
    names = [p['name'] for p in masterlist['courses'] if x in p['year'] and y in p['credit']]
    return names

def get_credit_type(x):
    credit_type = [p['credit'] for p in masterlist['courses'] if x in p['name']]
    return credit_type

def get_length(x):
    length = [p['length'] for p in masterlist['courses'] if x in p['name']]
    return length
    
def get_course_info(name):
    for p in masterlist['courses']:
        if name in p['name']:
            return p

def clear_frame():
    for widgets in frame.winfo_children():
        widgets.destroy()

def list_all():
    clear_frame()
    #sb = Scrollbar(frame)
    mylist = Listbox(frame)#frame, yscrollcommand = sb.set)
    names = get_courses()
    for i, name in enumerate(names):
        mylist.insert(END, name)

    #sb.config(command=mylist.yview)
    exit_button = Button(text="Back to main menu", command=main_menu)
    mylist.pack(expand=True, fill='both')
    exit_button.pack(side=RIGHT)

def list_business():
    clear_frame()
    sb = Scrollbar(frame)
    mylist = Listbox(frame, yscrollcommand = sb.set)
    credit_type = "Business, Marketing, and Computer Science"
    names = get_courses(credit_type)
    for i, name in enumerate(names):
        mylist.insert(END, name)
    mylist.pack(expand=True, fill='both')
    sb.config(command=mylist.yview)
    exit_button = Button(text="Back to main menu", command=main_menu)
    exit_button.pack(side=RIGHT)

def list_facs():
    clear_frame()
    sb = Scrollbar(frame)
    mylist = Listbox(frame, yscrollcommand = sb.set)
    credit_type = "Family and Consumer Science"
    names = get_courses(credit_type)
    for i, name in enumerate(names):
        mylist.insert(END, name)
    mylist.pack(expand=True, fill='both')
    sb.config(command=mylist.yview)
    exit_button = Button(text="Back to main menu", command=main_menu)
    exit_button.pack(side=RIGHT)

def list_ela():
    clear_frame()
    sb = Scrollbar(frame)
    mylist = Listbox(frame, yscrollcommand = sb.set)
    credit_type = "English / Language Arts"
    names = get_courses(credit_type)
    for i, name in enumerate(names):
        mylist.insert(END, name)
    mylist.pack(expand=True, fill='both')
    sb.config(command=mylist.yview)
    exit_button = Button(text="Back to main menu", command=main_menu)
    exit_button.pack(side=RIGHT)

def list_math():
    clear_frame()
    sb = Scrollbar(frame)
    mylist = Listbox(frame, yscrollcommand = sb.set)
    credit_type = "Mathematics"
    names = get_courses(credit_type)
    for i, name in enumerate(names):
        mylist.insert(END, name)
    mylist.pack(expand=True, fill='both')
    sb.config(command=mylist.yview)
    exit_button = Button(text="Back to main menu", command=main_menu)
    exit_button.pack(side=RIGHT)

def list_performing():
    clear_frame()
    sb = Scrollbar(frame)
    mylist = Listbox(frame, yscrollcommand = sb.set)
    credit_type = "Performing Arts"
    names = get_courses(credit_type)
    for i, name in enumerate(names):
        mylist.insert(END, name)
    mylist.pack(expand=True, fill='both')
    sb.config(command=mylist.yview)
    exit_button = Button(text="Back to main menu", command=main_menu)
    exit_button.pack(side=RIGHT)

def list_pe():
    clear_frame()
    sb = Scrollbar(frame)
    mylist = Listbox(frame, yscrollcommand = sb.set)
    credit_type = "Physical Education and Health"
    names = get_courses(credit_type)
    for i, name in enumerate(names):
        mylist.insert(END, name)
    mylist.pack(expand=True, fill='both')
    sb.config(command=mylist.yview)
    exit_button = Button(text="Back to main menu", command=main_menu)
    exit_button.pack(side=RIGHT)

def list_science():
    clear_frame()
    sb = Scrollbar(frame)
    mylist = Listbox(frame, yscrollcommand = sb.set)
    credit_type = "Science "
    names = get_courses(credit_type)
    for i, name in enumerate(names):
        mylist.insert(END, name)
    mylist.pack(expand=True, fill='both')
    sb.config(command=mylist.yview)
    exit_button = Button(text="Back to main menu", command=main_menu)
    exit_button.pack(side=RIGHT)

def list_social():
    clear_frame()
    sb = Scrollbar(frame)
    mylist = Listbox(frame, yscrollcommand = sb.set)
    credit_type = "Social Studies"
    names = get_courses(credit_type)
    for i, name in enumerate(names):
        mylist.insert(END, name)
    mylist.pack(expand=True, fill='both')
    sb.config(command=mylist.yview)
    exit_button = Button(text="Back to main menu", command=main_menu)
    exit_button.pack(side=RIGHT)

def list_visual():
    clear_frame()
    sb = Scrollbar(frame)
    mylist = Listbox(frame, yscrollcommand = sb.set)
    credit_type = "Visual Arts"
    names = get_courses(credit_type)
    for i, name in enumerate(names):
        mylist.insert(END, name)
    mylist.pack(expand=True, fill='both')
    sb.config(command=mylist.yview)
    exit_button = Button(text="Back to main menu", command=main_menu)
    exit_button.pack(side=RIGHT)

def list_world():
    clear_frame()
    sb = Scrollbar(frame)
    mylist = Listbox(frame, yscrollcommand = sb.set)
    credit_type = "World Language"
    names = get_courses(credit_type)
    for i, name in enumerate(names):
        mylist.insert(END, name)
    mylist.pack(expand=True, fill='both')
    sb.config(command=mylist.yview)
    exit_button = Button(text="Back to main menu", command=main_menu)
    exit_button.pack(side=RIGHT)
    
def list_multi():
    clear_frame()
    sb = Scrollbar(frame)
    mylist = Listbox(frame, yscrollcommand = sb.set)
    credit_type = "Multidisciplinary"
    names = get_courses(credit_type)
    for i, name in enumerate(names):
        mylist.insert(END, name)
    mylist.pack(expand=True, fill='both')
    sb.config(command=mylist.yview)
    exit_button = Button(text="Back to main menu", command=main_menu)
    exit_button.pack(side=RIGHT)

def list_name():

    class_list = []

    names = get_courses()
    for i, name in enumerate(names):
        class_list.append(name)
    
    def update(data):
        my_list.delete(0, END)

        for item in data:
            my_list.insert(END, item)
        
    def fillout(e):
        entry.delete(0, END)
        if my_list.curselection() != ():
            entry.insert(0, my_list.get(my_list.curselection()))

    def check(e):
        typed = entry.get()
        if typed == '':
            data = class_list
        else:
            data = []
            for item in class_list:
                if typed.lower() in item.lower():
                    data.append(item)
        update(data)
        

    def submit_class():
        if entry.get() in class_list:
            course = get_course_info(entry.get())
            entry.delete(0, END)
            update(course)
            
        else:
            data = ['That is not a valid course', 'press backspace to go back to course list']
            update(data)
            
        
                

    clear_frame()
    label = Label(frame, text="Enter class name below")
    label.pack()

    entry = Entry(frame, bg='white', fg='black')
    entry.pack()
    my_list = Listbox(frame, width=30)
    my_list.pack()

    confirm = Button(text="Get course info", command=submit_class)
    confirm.pack()

    exit_button = Button(text="Back to main menu", command=main_menu)
    exit_button.pack()


    update(class_list)

    my_list.bind("<<ListboxSelect>>", fillout)

    entry.bind("<KeyRelease>", check)
    

def list_freshman():
    clear_frame()
    sb = Scrollbar(frame)
    mylist = Listbox(frame, yscrollcommand = sb.set)
    names = get_year("9")
    for i, name in enumerate(names):
        mylist.insert(END, name)
    mylist.pack(expand=True, fill='both')
    sb.config(command=mylist.yview)
    exit_button = Button(text="Back to main menu", command=main_menu)
    exit_button.pack(side=RIGHT)

def list_sophomore():
    clear_frame()
    sb = Scrollbar(frame)
    mylist = Listbox(frame, yscrollcommand = sb.set)
    names = get_year("10")
    for i, name in enumerate(names):
        mylist.insert(END, name)
    mylist.pack(expand=True, fill='both')
    sb.config(command=mylist.yview)
    exit_button = Button(text="Back to main menu", command=main_menu)
    exit_button.pack(side=RIGHT)

def list_junior():
    clear_frame()
    sb = Scrollbar(frame)
    mylist = Listbox(frame, yscrollcommand = sb.set)
    names = get_year("11")
    for i, name in enumerate(names):
        mylist.insert(END, name)
    mylist.pack(expand=True, fill='both')
    sb.config(command=mylist.yview)
    exit_button = Button(text="Back to main menu", command=main_menu)
    exit_button.pack(side=RIGHT)

def list_senior():
    clear_frame()
    sb = Scrollbar(frame)
    mylist = Listbox(frame, yscrollcommand = sb.set)
    names = get_year("12")
    for i, name in enumerate(names):
        mylist.insert(END, name)
    mylist.pack(expand=True, fill='both')
    sb.config(command=mylist.yview)
    exit_button = Button(text="Back to main menu", command=main_menu)
    exit_button.pack(side=RIGHT)
    

def list_credit():
    clear_frame()
    busbutton = Button(text="Business, Marketing, and Computer Science", command=list_business)
    facsbutton = Button(text="Family and Consumer Science", command=list_facs)
    elabutton = Button(text="English / Language Arts", command=list_ela)
    mathbutton = Button(text="Mathematics", command=list_math)
    performbutton = Button(text="Performing Arts", command=list_performing)
    pebutton = Button(text="Physical Education and Health", command=list_pe)
    sciencebutton = Button(text="Science", command=list_science)
    socialbutton = Button(text="Social Studies", command=list_social)
    visualbutton = Button(text="Visual Arts", command=list_visual)
    worldbutton = Button(text="World Languages", command=list_world)
    multibutton = Button(text="Multidisciplinary", command=list_multi)
    exitbutton = Button(text="Back to main menu", command=main_menu)
    busbutton.pack()
    facsbutton.pack()
    elabutton.pack()
    mathbutton.pack()
    performbutton.pack()
    pebutton.pack()
    sciencebutton.pack()
    socialbutton.pack()
    visualbutton.pack()
    worldbutton.pack()
    multibutton.pack()
    exitbutton.pack()

def list_year():
    clear_frame()
    freshman = Button(text="Freshman", command=list_freshman)
    sophomore = Button(text="Sophomore", command=list_sophomore)
    junior = Button(text="Junior", command=list_junior)
    senior = Button(text="Senior", command=list_senior)
    exitbutton = Button(text="Back to main menu", command=main_menu)
    freshman.pack()
    sophomore.pack()
    junior.pack()
    senior.pack()
    exitbutton.pack()

def both_info_3(x,y):
    clear_frame()
    credit = x
    year = y

    sb = Scrollbar(frame)
    mylist = Listbox(frame, yscrollcommand = sb.set)
    names = get_both(credit, year)
    for i, name in enumerate(names):
        mylist.insert(END, name)
    mylist.pack(expand=True, fill='both')
    sb.config(command=mylist.yview)
    exit_button = Button(text="Back to main menu", command=main_menu)
    exit_button.pack(side=RIGHT)
    

def both_info_2(x):
    clear_frame()
    year = x
    a = "Business, Marketing, and Computer Science"
    b = "Family and Consumer Science"
    c = "English / Language Arts"
    d = "Mathematics"
    e = "Performing Arts"
    f = "Physical Education and Health"
    g = "Science "
    h = "Social Studies"
    i = "Visual Arts"
    j = "World Language"
    k = "Multidisciplinary"
    
    busbutton = Button(text=a, command=lambda: both_info_3(year, a))
    facsbutton = Button(text=b, command=lambda: both_info_3(year, b))
    elabutton = Button(text=c, command=lambda: both_info_3(year, c))
    mathbutton = Button(text=d, command=lambda: both_info_3(year, d))
    performbutton = Button(text=e, command=lambda: both_info_3(year, e))
    pebutton = Button(text=f, command=lambda: both_info_3(year, f))
    sciencebutton = Button(text=g, command=lambda: both_info_3(year, g))
    socialbutton = Button(text=h, command=lambda: both_info_3(year, h))
    visualbutton = Button(text=i, command=lambda: both_info_3(year, i))
    worldbutton = Button(text=j, command=lambda: both_info_3(year, j))
    multibutton = Button(text=k, command=lambda: both_info_3(year, k))
    exitbutton = Button(text="Back to main menu", command=main_menu)
    busbutton.pack()
    facsbutton.pack()
    elabutton.pack()
    mathbutton.pack()
    performbutton.pack()
    pebutton.pack()
    sciencebutton.pack()
    socialbutton.pack()
    visualbutton.pack()
    worldbutton.pack()
    multibutton.pack()
    exitbutton.pack()

def both_info():
    clear_frame()
    a = "9"
    b = "10"
    c = "11"
    d = "12"
    freshman = Button(text="Freshman", command=lambda: both_info_2("9"))
    sophomore = Button(text="Sophomore", command=lambda: both_info_2("10"))
    junior = Button(text="Junior", command=lambda: both_info_2("11"))
    senior = Button(text="Senior", command=lambda: both_info_2("12"))
    exitbutton = Button(text="Back to main menu", command=main_menu)
    freshman.pack()
    sophomore.pack()
    junior.pack()
    senior.pack()
    exitbutton.pack()

def remove_classes():
    clear_frame()
    class_list = []

    with open('hsclasstrack.txt', 'r') as track:
        for line in track:
            strip_lines = line.strip()
            class_list.append(strip_lines)


    def update(data):
        my_list.delete(0, END)

        for item in data:
            my_list.insert(END, item)
        
    def fillout(e):
        entry.delete(0, END)
        if my_list.curselection() != ():
            entry.insert(0, my_list.get(my_list.curselection()))

    def check(e):
        typed = entry.get()
        if typed == '':
            data = class_list
        else:
            data = []
            for item in class_list:
                if typed.lower() in item.lower():
                    data.append(item)
        update(data)
        

    def remove_class():
        with open('hsclasstrack.txt', 'r') as track:
            taken = track.readlines()
            for item in taken:

                removed = entry.get()
                if removed not in class_list:
                    if removed == "":
                        pass
                    else:
                        data = ['That is not a valid course', 'press backspace to go back to course list']
                        update(data)
                
                elif removed in item:
                    class_remove = removed + "\n"
                    taken.remove(class_remove)
                    track.close()
                    with open('hsclasstrack.txt', 'w') as track:
                        for item in taken:
                            track.write(item)
                    class_list.remove(removed)
                    entry.delete(0, END)
                    update(class_list)
                    
                    
                elif taken == []:
                    data = ['You have not input any classes']
                    update(data)
                
        
                

    clear_frame()
    label = Label(frame, text="Choose class to remove")
    label.pack()

    entry = Entry(frame, bg='white', fg='black')
    entry.pack()
    my_list = Listbox(frame, width=30)
    my_list.pack()

    submit_button = Button(text="Remove class", command=remove_class)
    submit_button.pack()
    exit_button = Button(text="Back to main menu", command=main_menu)
    exit_button.pack()

    my_list.delete(0, END)
    for item in class_list:
        my_list.insert(END, item)

    update(class_list)

    my_list.bind("<<ListboxSelect>>", fillout)

    entry.bind("<KeyRelease>", check)

    
    

def add_classes():
        
    class_list = []

    names = get_courses()
    for i, name in enumerate(names):
        class_list.append(name)

    with open('hsclasstrack.txt', 'r') as track:
        for line in track:
            strip_lines = line.strip()
            if strip_lines in class_list:
                class_list.remove(strip_lines)
        
        
    
    def update(data):
        my_list.delete(0, END)

        for item in data:
            my_list.insert(END, item)
        
    def fillout(e):
        entry.delete(0, END)
        if my_list.curselection() != ():
            entry.insert(0, my_list.get(my_list.curselection()))

    def check(e):
        typed = entry.get()
        if typed == '':
            data = class_list
        else:
            data = []
            for item in class_list:
                if typed.lower() in item.lower():
                    data.append(item)
        update(data)
        

    def submit_class():
        with open('hsclasstrack.txt', 'a') as track:
            if entry.get() in class_list:
                track.write(entry.get())
                track.write("\n")
                class_list.remove(entry.get())
                entry.delete(0, END)
                update(class_list)
                track.close()
            else:
                data = ['That is not a valid course', 'press backspace to go back to course list']
                update(data)
            
        
                

    clear_frame()
    label = Label(frame, text="Enter class names below")
    label.pack()

    entry = Entry(frame, bg='white', fg='black')
    entry.pack()
    my_list = Listbox(frame, width=30)
    my_list.pack()

    submit_button = Button(text="Submit class", command=submit_class)
    submit_button.pack()
    exit_button = Button(text="Back to main menu", command=main_menu)
    exit_button.pack()


    update(class_list)

    my_list.bind("<<ListboxSelect>>", fillout)

    entry.bind("<KeyRelease>", check)

def view_classes():
    clear_frame()
    class_list = []

    my_list = Listbox(frame, width=30)
    exit_button = Button(text="Back to main menu", command=main_menu)

    with open('hsclasstrack.txt', 'r') as track:
        for line in track:
            strip_lines = line.strip()
            class_list.append(strip_lines)

    my_list.delete(0, END)
    for item in class_list:
        my_list.insert(END, item)

    my_list.pack(expand=True, fill='both')
    exit_button.pack(side=RIGHT)

def remaining_credits():
    clear_frame()
    class_list = []
    credit_type_list = []
    class_length_list = []

    a = "Business, Marketing, and Computer Science"
    b = "Family and Consumer Science"
    c = "English / Language Arts"
    d = "Mathematics"
    e = "Performing Arts"
    f = "Physical Education and Health"
    g = "Science "
    h = "Social Studies"
    i = "Visual Arts"
    j = "World Language"
    k = "Multidisciplinary"
    

    with open('diplomatype.txt', 'r') as dip:
            diploma_num = dip.readline()
            dip.close()

    with open('hsclasstrack.txt', 'r') as track:
        for line in track:
            strip_lines = line.strip()
            class_list.append(strip_lines)

    for item in class_list:
        credit_type = get_credit_type(item)
        credit_type_list.append(credit_type)

    for item in class_list:
        class_length = get_length(item)
        class_length_list.append(class_length)
        
            
    if diploma_num ==  "1":
        diploma_type = "Core 40"
    elif diploma_num == "2":
        diploma_type = "Core 40 with Academic Honors"

    current_diploma = Label(frame, text="Current diploma: " + diploma_type)
    current_diploma.pack()

    if diploma_num == "1":
        eng = 8
        ss = 6
        math = 6
        sci = 6
        pe = 3
        direct = 5
        bus = 1
        elec = 7

        x = 0

        for item in credit_type_list:
            length_of_class = class_length_list[x]
            if a in item:
                if "Semester" in length_of_class:
                    if bus == 1:
                        bus -= 1
                    else:
                        elec -= 1
                elif "Year" in length_of_class:
                    if bus == 1:
                        bus -= 1
                        elec -= 1
                    else:
                        elec -= 2
                elif "Either" in length_of_class:
                    if bus == 1:
                        bus -= 1
                    else:
                        elec -= 1
            elif b in item:
                if "Semester" in length_of_class:
                    elec -= 1
                elif "Year" in length_of_class:
                    elec -= 2
                elif "Either" in length_of_class:
                    elec -= 1
            elif c in item:
                if "Semester" in length_of_class:
                    if eng > 0:
                        eng -= 1
                    else:
                        elec -= 1
                elif "Year" in length_of_class:
                    if eng > 0:
                        eng -= 2
                    else:
                        elec -= 2
                elif "Either" in length_of_class:
                    if eng > 0:
                        eng -= 1
                    else:
                        elec -= 1
            elif d in item:
                if "Semester" in length_of_class:
                    if math > 0:
                        math -= 1
                    else:
                        elec -= 1
                elif "Year" in length_of_class:
                    if math > 0:
                        math -= 2
                    else:
                        elec -= 2
                elif "Either" in length_of_class:
                    if math > 0:
                        math -= 1
                    else:
                        elec -= 1
            elif e in item:
                if "Semester" in length_of_class:
                    if direct > 0:
                        direct -= 1
                    else:
                        elec -= 1
                elif "Year" in length_of_class:
                    if direct > 0:
                        direct -= 2
                    else:
                        elec -= 2
                elif "Either" in length_of_class:
                    if direct > 0:
                        direct -= 1
                    else:
                        elec -= 1
            elif f in item:
                if "Semester" in length_of_class:
                    if pe > 0:
                        pe -= 1
                    else:
                        elec -= 1
                elif "Year" in length_of_class:
                    if pe > 0:
                        pe -= 2
                    else:
                        elec -= 2
                elif "Either" in length_of_class:
                    if pe > 0:
                        pe -= 1
                    else:
                        elec -= 1
            elif g in item:
                if "Semester" in length_of_class:
                    if sci > 0:
                        sci -= 1
                    else:
                        elec -= 1
                elif "Year" in length_of_class:
                    if sci > 0:
                        sci -= 2
                    else:
                        elec -= 2
                elif "Either" in length_of_class:
                    if sci > 0:
                        sci -= 1
                    else:
                        elec -= 1
            elif h in item:
                if "Semester" in length_of_class:
                    if ss > 0:
                        ss -= 1
                    else:
                        elec -= 1
                elif "Year" in length_of_class:
                    if ss > 0:
                        ss -= 2
                    else:
                        elec -= 2
                elif "Either" in length_of_class:
                    if ss > 0:
                        ss -= 1
                    else:
                        elec -= 1
            elif i in item:
                if "Semester" in length_of_class:
                    if direct > 0:
                        direct -= 1
                    else:
                        elec -= 1
                elif "Year" in length_of_class:
                    if direct > 0:
                        direct -= 2
                    else:
                        elec -= 2
                elif "Either" in length_of_class:
                    if direct > 0:
                        direct -= 1
                    else:
                        elec -= 1
            elif j in item:
                if "Semester" in length_of_class:
                    if direct > 0:
                        direct -= 1
                    else:
                        elec -= 1
                elif "Year" in length_of_class:
                    if direct > 0:
                        direct -= 2
                    else:
                        elec -= 2
                elif "Either" in length_of_class:
                    if direct > 0:
                        direct -= 1
                    else:
                        elec -= 1
            elif k in item:
                if "Semester" in length_of_class:
                    elec -= 1
                elif "Year" in length_of_class:
                    elec -= 2
                elif "Either" in length_of_class:
                    elec -= 1
                    
            else:
                pass
            
            x += 1
            
        eng_label = Label(frame, text="You have " + str(eng) + " credits left for English")
        eng_label.pack()

        ss_label = Label(frame, text="You have " + str(ss) + " credits left for Social Studies")
        ss_label.pack()

        math_label = Label(frame, text="You have " + str(math) + " credits left for Math")
        math_label.pack()

        sci_label = Label(frame, text="You have " + str(sci) + " credits left for Science")
        sci_label.pack()

        pe_label = Label(frame, text="You have " + str(pe) + " credits left for PE and Health")
        pe_label.pack()

        direct_label = Label(frame, text="You have " + str(direct) + " credits left for Directed Electives")
        direct_label.pack()

        bus_label = Label(frame, text="You have " + str(bus) + " credits left for Business/Tech")
        bus_label.pack()

        elec_label = Label(frame, text="You have " + str(elec) + " credits left for Required Electives")
        elec_label.pack()
    elif diploma_num == "2":
        eng = 8
        ss = 6
        math = 8
        sci = 6
        pe = 3
        lang = 6
        bus = 1
        fine = 2
        elec = 7

        x = 0

        for item in credit_type_list:
            length_of_class = class_length_list[x]
            if a in item:
                if "Semester" in length_of_class:
                    if bus == 1:
                        bus -= 1
                    else:
                        elec -= 1
                elif "Year" in length_of_class:
                    if bus == 1:
                        bus -= 1
                        elec -= 1
                    else:
                        elec -= 2
                elif "Either" in length_of_class:
                    if bus == 1:
                        bus -= 1
                    else:
                        elec -= 1
            elif b in item:
                if "Semester" in length_of_class:
                    elec -= 1
                elif "Year" in length_of_class:
                    elec -= 2
                elif "Either" in length_of_class:
                    elec -= 1
            elif c in item:
                if "Semester" in length_of_class:
                    if eng > 0:
                        eng -= 1
                    else:
                        elec -= 1
                elif "Year" in length_of_class:
                    if eng > 0:
                        eng -= 2
                    else:
                        elec -= 2
                elif "Either" in length_of_class:
                    if eng > 0:
                        eng -= 1
                    else:
                        elec -= 1
            elif d in item:
                if "Semester" in length_of_class:
                    if math > 0:
                        math -= 1
                    else:
                        elec -= 1
                elif "Year" in length_of_class:
                    if math > 0:
                        math -= 2
                    else:
                        elec -= 2
                elif "Either" in length_of_class:
                    if math > 0:
                        math -= 1
                    else:
                        elec -= 1
            elif e in item:
                if "Semester" in length_of_class:
                    if fine > 0:
                        fine -= 1
                    else:
                        elec -= 1
                elif "Year" in length_of_class:
                    if fine > 0:
                        fine -= 2
                    else:
                        elec -= 2
                elif "Either" in length_of_class:
                    if fine > 0:
                        fine = 1
                    else:
                        elec -= 1
            elif f in item:
                if "Semester" in length_of_class:
                    if pe > 0:
                        pe -= 1
                    else:
                        elec -= 1
                elif "Year" in length_of_class:
                    if pe > 0:
                        pe -= 2
                    else:
                        elec -= 2
                elif "Either" in length_of_class:
                    if pe > 0:
                        pe -= 1
                    else:
                        elec -= 1
            elif g in item:
                if "Semester" in length_of_class:
                    if sci > 0:
                        sci -= 1
                    else:
                        elec -= 1
                elif "Year" in length_of_class:
                    if sci > 0:
                        sci -= 2
                    else:
                        elec -= 2
                elif "Either" in length_of_class:
                    if sci > 0:
                        sci -= 1
                    else:
                        elec -= 1
            elif h in item:
                if "Semester" in length_of_class:
                    if ss > 0:
                        ss -= 1
                    else:
                        elec -= 1
                elif "Year" in length_of_class:
                    if ss > 0:
                        ss -= 2
                    else:
                        elec -= 2
                elif "Either" in length_of_class:
                    if ss > 0:
                        ss -= 1
                    else:
                        elec -= 1
            elif i in item:
                if "Semester" in length_of_class:
                    if fine > 0:
                        fine -= 1
                    else:
                        elec -= 1
                elif "Year" in length_of_class:
                    if fine > 0:
                        fine -= 2
                    else:
                        elec -= 2
                elif "Either" in length_of_class:
                    if fine > 0:
                        fine -= 1
                    else:
                        elec -= 1
            elif j in item:
                if "Semester" in length_of_class:
                    if lang > 0:
                        lang -= 1
                    else:
                        elec -= 1
                elif "Year" in length_of_class:
                    if lang > 0:
                        lang -= 2
                    else:
                        elec -= 2
                elif "Either" in length_of_class:
                    if lang > 0:
                        lang -= 1
                    else:
                        elec -= 1
            elif k in item:
                if "Semester" in length_of_class:
                    elec -= 1
                elif "Year" in length_of_class:
                    elec -= 2
                elif "Either" in length_of_class:
                    elec -= 1
                    
            else:
                pass

            x += 1
            
        eng_label = Label(frame, text="You have " + str(eng) + " credits left for English")
        eng_label.pack()

        ss_label = Label(frame, text="You have " + str(ss) + " credits left for Social Studies")
        ss_label.pack()

        math_label = Label(frame, text="You have " + str(math) + " credits left for Math")
        math_label.pack()

        sci_label = Label(frame, text="You have " + str(sci) + " credits left for Science")
        sci_label.pack()

        pe_label = Label(frame, text="You have " + str(pe) + " credits left for PE and Health")
        pe_label.pack()

        fine_label = Label(frame, text="You have " + str(fine) + " credits left for Fine Arts")
        fine_label.pack()

        lang_label = Label(frame, text="You have " + str(lang) + " credits left for World Language")
        lang_label.pack()

        bus_label = Label(frame, text="You have " + str(bus) + " credits left for Business/Tech")
        bus_label.pack()

        elec_label = Label(frame, text="You have " + str(elec) + " credits left for Required Electives")
        elec_label.pack()
                

    exit_button = Button(text="Back to main menu", command=main_menu)
    exit_button.pack()

def diploma_type():
    def set_menu():
        clear_frame()
        with open('diplomatype.txt', 'r') as track:
            diploma_num = track.readline()
            track.close()

        if diploma_num ==  "1":
            diploma_type = "Core 40"
        elif diploma_num == "2":
            diploma_type = "Core 40 with Academic Honors"
            
        current_diploma = Label(frame, text="Current diploma: " + diploma_type)
        current_diploma.pack()
    
        core_40 = Button(text="Core 40", command=set_core_40)
        core_40.pack()

        core_40_ah = Button(text="Core 40 with Academic Honors", command=set_core_40_ah)
        core_40_ah.pack()
    
        exit_button = Button(text="Back to main menu", command=main_menu)
        exit_button.pack()
        
    
    def set_core_40():
        with open('diplomatype.txt', 'w') as track:
            track.write("1")
            track.close()
            set_menu()
            

    def set_core_40_ah():
        with open('diplomatype.txt', 'w') as track:
            track.write("2")
            track.close()
            set_menu()

    set_menu()
        
def list_menu():
    clear_frame()
    all_button = Button(text="List all classes", command=list_all)
    all_button.pack()
    credit_button = Button(text="List classes by credit", command=list_credit)
    credit_button.pack()
    year_button = Button(text="List classes by year", command=list_year)
    year_button.pack()
    both = Button(text="List classes by credit and year", command=both_info)
    both.pack()
    name_button = Button(text="Search for a class by name", command=list_name)
    name_button.pack()
    exit_button = Button(text="Back to main menu", command=main_menu)
    exit_button.pack()

def add_menu():
    clear_frame()
    add_button = Button(text="Add classes that you have taken", command=add_classes)
    add_button.pack()
    view_button = Button(text="View previously taken classes", command=view_classes)
    view_button.pack()
    remove_button = Button(text="Remove classes from your list", command=remove_classes)
    remove_button.pack()
    exit_button = Button(text="Back to main menu", command=main_menu)
    exit_button.pack()

def credit_menu():
    clear_frame()
    remaining = Button(text="View your credit requirements", command=remaining_credits)
    remaining.pack()
    diploma = Button(text="Change diploma type", command=diploma_type)
    diploma.pack()
    exit_button = Button(text="Back to main menu", command=main_menu)
    exit_button.pack()
    

def main_menu():
    clear_frame()
    list_button = Button(text="List Classes", command=list_menu)
    list_button.pack()
    add_button = Button(text="Your Classes", command=add_menu)
    add_button.pack()
    credit_button = Button(text="Credit requirements and Diploma", command=credit_menu)
    credit_button.pack()
    quit_button = Button(frame, text="Quit", command=frame.destroy)
    quit_button.pack()
    
    
main_menu()
frame.mainloop()

