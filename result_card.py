import tkinter as tk
from tkinter import messagebox

class result():
    def __init__(self,root):
        self.root= root
        self.root.title("Result card management system")
        
        self.frame=tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)
        
        self.marks1=tk.Label(self.frame, text="English Marks:")
        self.marks1.grid(row=0, column=0, sticky="w")
        self.marks1In=tk.Entry(self.frame)
        self.marks1In.grid(row=0, column=1, sticky="w")
        
        self.marks2=tk.Label(self.frame, text="Math Marks:")
        self.marks2.grid(row=1, column=0, sticky="w")
        self.marks2In=tk.Entry(self.frame)
        self.marks2In.grid(row=1, column=1, sticky="w")
        
        self.marks3=tk.Label(self.frame, text="Science Marks:")
        self.marks3.grid(row=2, column=0, sticky="w")
        self.marks3In=tk.Entry(self.frame)
        self.marks3In.grid(row=2, column=1, sticky="w")
        
        self.button=tk.Button(self.frame, text="Result", command=self.calFun)
        self.button.grid(row=3, column=1, sticky="w")
        
        self.list=tk.Listbox(self.frame, width=100, height=30, bg="sky blue")
        self.list.grid(row=4, columnspan=10, sticky="w")
        
        
    def calFun(self):
            eng=self.marks1In.get()
            mth=self.marks2In.get()
            sc= self.marks3In.get()
            if eng and mth and sc:
                engMarks= int(eng)
                mthMarks= int(mth)
                scMarks= int(sc)
                total= engMarks+mthMarks+scMarks
                max=300
                per= (total/max)*100
                
                if per >=80:
                    totalMarks=f"Total Marks: {total}, out of: {max}"
                    grade= f"You are assigned Grade A"
                    perf= f"Your performance is Excelent"
                    self.list.insert(tk.END, totalMarks)
                    self.list.insert(tk.END, grade)
                    self.list.insert(tk.END, perf)
                    
                elif per <80 and per >=70:
                    totalMarks=f"Total Marks: {total}, out of: {max}"
                    grade= f"You are assigned Grade B"
                    perf= f"Your performance is Very Good"
                    self.list.insert(tk.END, totalMarks)
                    self.list.insert(tk.END, grade)
                    self.list.insert(tk.END, perf)  
                    
                elif per < 70 and per >=60:
                    totalMarks=f"Total Marks: {total}, out of: {max}"
                    grade= f"You are assigned Grade C"
                    perf= f"Your performance is Good"
                    self.list.insert(tk.END, totalMarks)
                    self.list.insert(tk.END, grade)
                    self.list.insert(tk.END, perf)
                    
                elif per < 60 and per >=50:
                    totalMarks=f"Total Marks: {total}, out of: {max}"
                    grade= f"You are assigned Grade D"
                    perf= f"Your performance is Poor"
                    self.list.insert(tk.END, totalMarks)
                    self.list.insert(tk.END, grade)
                    self.list.insert(tk.END, perf)
                    
                elif per < 50:
                    totalMarks=f"Total Marks: {total}, out of: {max}"
                    grade= f"You are assigned Grade F"
                    perf= f"Your are Fail!"
                    self.list.insert(tk.END, totalMarks)
                    self.list.insert(tk.END, grade)
                    self.list.insert(tk.END, perf)
                self.clearFun()       
                      
            else:
               tk.messagebox.showerror("Error","Fill all input fields:")
               
    def clearFun(self):
        self.marks1In.delete(0,tk.END)
        self.marks2In.delete(0,tk.END)
        self.marks3In.delete(0,tk.END)
        
         
root=tk.Tk()
obj=result(root)
root.mainloop()
    