from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import mysql.connector
from tkinter import messagebox
import tkinter





class BankManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("BANK MANAGEMENT SYSTEM")
        self.root.geometry("1550x800+0+0")
#=============VARIABLE================#

        self.user_var=StringVar()
        self.accountNo_var=StringVar()
        self.firstName_var=StringVar()
        self.lastName_var=StringVar()
        self.branch_var=StringVar()
        self.balance_var=StringVar()
        self.gender_var=StringVar()
        self.mobileNo_var=StringVar()
        self.pincode_var=StringVar()
        self.adharNo_var=StringVar()
        self.accountType_var=StringVar()
        self.IFSCcode_var=StringVar()

        



        # Add a label
        label_title = Label(self.root, text="Welcome to the Bank Management System", bg="powder blue", fg="green", bd=20, relief=RIDGE, font=("Arial", 50, "bold"), padx=2, pady=6)
        label_title.pack(side=TOP, fill=X)

        # Main frame container
        frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        frame.place(x=0, y=130, width=1530, height=600)

        # Left frame for "BANK MEMBERS INFORMATION"
        DataFrameLeft = LabelFrame(frame, text="BANK MEMBERS INFORMATION", bg="powder blue", fg="black", bd=12, relief=RIDGE, font=("Arial", 20, "bold"))
        DataFrameLeft.place(x=0, y=0, width=900, height=350)

        # USER TYPE section inside DataFrameLeft
        lblMember = Label(DataFrameLeft, font=("Arial", 12, "bold"),text="USER TYPE", bg="powder blue",   padx=10, pady=12)
        lblMember.grid(row=0, column=0, sticky=W)

       
        comMember = ttk.Combobox(DataFrameLeft, font=("Arial", 12, "bold"),textvariable=self.user_var, width=20, state="readonly")
        comMember["values"] = ("Admin staff", "Customer", "Manager")  # Corrected spelling from "Admin staff" to "Admin"
        comMember.grid(row=0, column=1, padx=10, pady=5)  # Adjust grid position if necessary
        
        lblAccount_No = Label(DataFrameLeft,text="ACCOUNT NUMBER", bg="powder blue",  font=("Arial", 12, "bold"), padx=10, pady=12)
        lblAccount_No.grid(row=1, column=0, sticky=W)
        txtAccount_No = Entry(DataFrameLeft,font=("Arial", 12, "bold"),textvariable=self.accountNo_var, width =20)
        txtAccount_No.grid(row=1, column=1 )

        lblTitle = Label(DataFrameLeft, text="USER FIRSTNAME", bg="powder blue",  font=("Arial", 12, "bold"), padx=10, pady=12)
        lblTitle.grid(row=2, column=0, sticky=W)
        txtTitle= Entry(DataFrameLeft,font=("Arial", 12, "bold"),textvariable=self.firstName_var, width =20)
        txtTitle.grid(row=2, column=1 )

        lblTitle1 = Label(DataFrameLeft, text="USER LASTNAME", bg="powder blue",  font=("Arial", 12, "bold"), padx=10, pady=12)
        lblTitle1.grid(row=3, column=0, sticky=W)
        txtTitle1= Entry(DataFrameLeft,font=("Arial", 12, "bold"),textvariable=self.lastName_var, width =20)
        txtTitle1.grid(row=3, column=1 )

        lblbranch = Label(DataFrameLeft, text="BRANCH", bg="powder blue",  font=("Arial", 12, "bold"), padx=10, pady=12)
        lblbranch.grid(row=4, column=0, sticky=W)
        

        comMember = ttk.Combobox(DataFrameLeft, font=("Arial", 12, "bold"),textvariable=self.branch_var, width=20, state="readonly")
        comMember["values"] = ("AMBEGAON", "KONDHWA", "KATRAJ","SWARGATE","NARHE","KARVE NAGAR","KOTHRUD","WADGAON","PADMAVATI","BALAJI NAGAR","Uptown Branch",
                            "Lakeside Branch","Hilltop Branch","Southgate Branch","Maple Avenue Branch","Central Plaza Branch","Pine Street Branch")  # Corrected spelling from "Admin staff" to "Admin"
        comMember.grid(row=4, column=1, padx=10, pady=5)  # Adjust grid position if necessary

        lblbalance = Label(DataFrameLeft, text="BALANCE", bg="powder blue",  font=("Arial", 12, "bold"), padx=10, pady=12)
        lblbalance.grid(row=5, column=0, sticky=W)
        txtbalance= Entry(DataFrameLeft,font=("Arial", 12, "bold"), textvariable=self.balance_var,width =20)
        txtbalance.grid(row=5, column=1 )

        lblgender = Label(DataFrameLeft, font=("Arial", 12, "bold"),text="GENDER", bg="powder blue",   padx=2, pady=6)
        lblgender.grid(row=0, column=3, sticky=W)

       
        comMember1 = ttk.Combobox(DataFrameLeft, font=("Arial", 12, "bold"),textvariable=self.gender_var, width=20, state="readonly")
        comMember1["values"] = ("FEMALE", "MALE")  # Corrected spelling from "Admin staff" to "Admin"
        comMember1.grid(row=0, column=4, padx=10, pady=5)

        lblmobile = Label(DataFrameLeft, text="MOBILE NUMBER", bg="powder blue",  font=("Arial", 12, "bold"), padx=2, pady=6)
        lblmobile.grid(row=1, column=3, sticky=W)
        txtmobile= Entry(DataFrameLeft,font=("Arial", 12, "bold"),textvariable=self.mobileNo_var, width =20)
        txtmobile.grid(row=1, column=4 )

        lblPincode = Label(DataFrameLeft, text="PINCODE", bg="powder blue",  font=("Arial", 12, "bold"), padx=2, pady=6)
        lblPincode.grid(row=2, column=3, sticky=W)
        txtPincode= Entry(DataFrameLeft,font=("Arial", 12, "bold"), textvariable=self.pincode_var,width =20)
        txtPincode.grid(row=2, column=4 )

        lblaadhar = Label(DataFrameLeft, text="AADHAR NUMBER", bg="powder blue",  font=("Arial", 12, "bold"), padx=2, pady=6)
        lblaadhar.grid(row=3, column=3, sticky=W)
        txtaadhar= Entry(DataFrameLeft,font=("Arial", 12, "bold"),textvariable=self.adharNo_var, width =20)
        txtaadhar.grid(row=3, column=4 )
        
        lblType = Label(DataFrameLeft, font=("Arial", 12, "bold"),text="ACCOUNT TYPE", bg="powder blue",   padx=1, pady=2)
        lblType.grid(row=4, column=3, sticky=W)

       
        comMember2 = ttk.Combobox(DataFrameLeft, font=("Arial", 12, "bold"),textvariable=self.accountType_var, width=20, state="readonly")
        comMember2["values"] = ("SAVING", "CURRENT")  # Corrected spelling from "Admin staff" to "Admin"
        comMember2.grid(row=4, column=4, padx=10, pady=5)

        lblIFSC = Label(DataFrameLeft, text="IFSC CODE", bg="powder blue",  font=("Arial", 12, "bold"), padx=10, pady=12)
        lblIFSC.grid(row=5, column=3, sticky=W)
        txtIFSC= Entry(DataFrameLeft,font=("Arial", 12, "bold"),textvariable=self.IFSCcode_var, width =20)
        txtIFSC.grid(row=5, column=4 )

     #================================DATAFRAME RIGHT=========================================#

        DataFrameRight = LabelFrame(frame, text="BRANCH", bg="powder blue", fg="black", bd=12, relief=RIDGE, font=("Arial", 20, "bold"), padx=20)
        DataFrameRight.place(x=870, y=5, width=580, height=345)

# Text box
        self.txtBox = Text(DataFrameRight, font=("Arial", 12, "bold"), width=32, height=14, padx=2, pady=6)
        self.txtBox.grid(row=0, column=2)

# Scrollbar
        ListScrollbar = Scrollbar(DataFrameRight)
        ListScrollbar.grid(row=0, column=1, sticky="ns")

        

# List of branch names
        branches = [
    "AMBEGAON", "KONDHWA", "KATRAJ", "SWARGATE", "NARHE", "KARVE NAGAR", "KOTHRUD", "WADGAON", "PADMAVATI", "BALAJI NAGAR",
    "UPTOWN BRANCH", "LAKESIDE BRANCH", "HILLTOP BRANCH", "SOUTHGATE BRANCH", "MAPLE AVENUE BRANCH", "CENTRAL PLAZA BRANCH", "PINE STREET BRANCH"
]

        def SelectBranch(event=""):
            selected_branch = branchListbox.get(branchListbox.curselection())
            branch_ifsc_codes = {
                "AMBEGAON": "SBIN0004719",
                "KONDHWA": "SBIN0004711" , 
                "KATRAJ": "SBIN0004732", 
                "SWARGATE": "SBIN0004798", 
                "NARHE": "SBIN0004729",
                "KARVE NAGAR": "SBIN0004713", 
                "KOTHRUD": "SBIN0004763", 
                "WADGAON": "SBIN0004773", 
                "PADMAVATI": "SBIN0004712", 
                "BALAJI NAGAR": "SBIN0004722",
                "UPTOWN BRANCH": "SBIN0004748", 
                "LAKESIDE BRANCH": "SBIN0004798", 
                "HILLTOP BRANCH": "SBIN0004742", 
                "SOUTHGATE BRANCH": "SBIN0004752", 
                "MAPLE AVENUE BRANCH":"SBIN0004734", 
                "CENTRAL PLAZA BRANCH": "SBIN0004799", 
                "PINE STREET BRANCH":"SBIN0004701"


                
            }
            self.IFSCcode_var.set(branch_ifsc_codes.get(selected_branch, "Unknown"))


# Listbox for branch names
        
        branchListbox = Listbox(DataFrameRight, font=("Arial", 12, "bold"), width=20, height=14, yscrollcommand=ListScrollbar.set)
        branchListbox.bind("<<ListboxSelect>>", SelectBranch)
        branchListbox.grid(row=0, column=0, padx=10, pady=12)
# Configure scrollbar
        ListScrollbar.config(command=branchListbox.yview)

# Insert branch names into the listbox
        for branch in branches:
            branchListbox.insert(END, branch)


#=================BUTTONS==================#
        FrameButton=Frame(root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameButton.place(x=0,y=530,width=1530,height=60)

        btnAddData=Button(FrameButton,command=self.add_data,text="ADD DATA",font=("Arial", 12, "bold"), width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=0)

        btnAddData=Button(FrameButton,command=self.show_data,text="SHOW DATA",font=("Arial", 12, "bold"), width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(FrameButton,command=self.update,text="UPDATE",font=("Arial", 12, "bold"), width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(FrameButton,command=self.delete,text="DELETE",font=("Arial", 12, "bold"), width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(FrameButton,command=self.reset,text="RESET",font=("Arial", 12, "bold"), width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=4)

        btnAddData=Button(FrameButton,command=self.iExit,text="EXIT",font=("Arial", 12, "bold"), width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=5)
        

#============FRAME===========#


        FrameDetails = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        FrameDetails.place(x=0, y=590, width=1530, height=210)

        Table_frame = Frame(FrameDetails, bd=6, relief=RIDGE, bg="powder blue")
        Table_frame.place(x=0, y=2, width=1460, height=190)

        # Scrollbars
        xscroll = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(Table_frame, orient=VERTICAL)

        # Treeview (Table)
        self.library_table = ttk.Treeview(
            Table_frame, 
            columns=("UserType", "AccountNO", "FirstName", "LastName", "Branch", "Balance", "Gender", "MobileNo", "Pincode", "AdharNo", "AccountType", "IFSCcode"), 
            xscrollcommand=xscroll.set, 
            yscrollcommand=yscroll.set
        )

        # Pack scrollbars
        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        # Configure scrollbars
        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        # Define headings for each column
        self.library_table.heading("UserType", text="USER TYPE")
        self.library_table.heading("AccountNO", text="ACCOUNT NO")
        self.library_table.heading("FirstName", text="FIRST NAME")
        self.library_table.heading("LastName", text="LAST NAME")
        self.library_table.heading("Branch", text="BRANCH")
        self.library_table.heading("Balance", text="BALANCE")
        self.library_table.heading("Gender", text="GENDER")
        self.library_table.heading("MobileNo", text="MOBILE NO")
        self.library_table.heading("Pincode", text="PINCODE")
        self.library_table.heading("AdharNo", text="AADHAR NO")
        self.library_table.heading("AccountType", text="ACCOUNT TYPE")
        self.library_table.heading("IFSCcode", text="IFSC CODE")

        # Show headings only
        self.library_table["show"] = "headings"

        # Pack the Treeview (table)
        self.library_table.pack(fill=BOTH, expand=1)

        # Define column widths
        self.library_table.column("UserType", width=100)
        self.library_table.column("AccountNO", width=100)
        self.library_table.column("FirstName", width=100)
        self.library_table.column("LastName", width=100)
        self.library_table.column("Branch", width=100)
        self.library_table.column("Balance", width=100)
        self.library_table.column("Gender", width=100)
        self.library_table.column("MobileNo", width=100)
        self.library_table.column("Pincode", width=100)
        self.library_table.column("AdharNo", width=100)
        self.library_table.column("AccountType", width=100)
        self.library_table.column("IFSCcode", width=100)
        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)

    def add_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="Shraddha#14", database="MyData1")
            my_cursor = conn.cursor()
            my_cursor.execute(
                "INSERT INTO library1 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (
                    self.user_var.get(),
                    self.accountNo_var.get(),
                    self.firstName_var.get(),
                    self.lastName_var.get(),
                    self.branch_var.get(),
                    self.balance_var.get(),
                    self.gender_var.get(),
                    self.mobileNo_var.get(),
                    self.pincode_var.get(),
                    self.adharNo_var.get(),
                    self.accountType_var.get(),
                    self.IFSCcode_var.get()
                )
            )
            conn.commit()
            self.fetch_data()
            messagebox.showinfo("Success", "USER HAS BEEN INSERTED SUCCESSFULLY")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error inserting data: {err}")
        finally:
            conn.close()

    def update(self):
        try:
        # Corrected the parameter name from 'username' to 'user'
            conn = mysql.connector.connect(host="localhost", username="root", password="Shraddha#14", database="MyData1")
            my_cursor = conn.cursor()

        # Ensure to specify the WHERE clause for the update operation
            my_cursor.execute(
             "UPDATE library1 SET user=%s, accountNo=%s, firstName=%s, lastName=%s, branch=%s, balance=%s, gender=%s, mobileNo=%s, pincode=%s, adharNo=%s, accountType=%s, IFSCcode=%s WHERE accountNo=%s",
            (
                self.user_var.get(),
                self.accountNo_var.get(),
                self.firstName_var.get(),
                self.lastName_var.get(),
                self.branch_var.get(),
                self.balance_var.get(),
                self.gender_var.get(),
                self.mobileNo_var.get(),
                self.pincode_var.get(),
                self.adharNo_var.get(),
                self.accountType_var.get(),
                self.IFSCcode_var.get(),
                self.accountNo_var.get()  # Adding this as a parameter for the WHERE clause
            )
        )
            conn.commit()
        
            self.fetch_data()  # Refresh the data after update
            self.reset()       # Reset input fields
            messagebox.showinfo("Success", "USER HAS BEEN UPDATED SUCCESSFULLY")
        
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error updating data: {err}")
        finally:
            if conn.is_connected():
               conn.close()  # Ensure the connection is closed if it was opened


        

    def fetch_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="Shraddha#14", database="MyData1")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM library1")
            rows = my_cursor.fetchall()
            if len(rows) != 0:
                self.library_table.delete(*self.library_table.get_children())
                for i in rows:
                    self.library_table.insert("", END, values=i)
            conn.commit()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error fetching data: {err}")
        finally:
            conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content = self.library_table.item(cursor_row)
        row=content['values']

        self.user_var.set(row[0]),
        self.accountNo_var.set(row[1]),
        self.firstName_var.set(row[2]),
        self.lastName_var.set(row[3]),
        self.branch_var.set(row[4]),
        self.balance_var.set(row[5]),
        self.gender_var.set(row[6]),
        self.mobileNo_var.set(row[7]),
        self.pincode_var.set(row[8]),
        self.adharNo_var.set(row[9]),
        self.accountType_var.set(row[10]),
        self.IFSCcode_var.set(row[11])

    def show_data(self):
        self.txtBox.insert(END,"User Type:\t\t"+self.user_var.get()+"\n")
        self.txtBox.insert(END,"AccountNO:\t\t"+self.accountNo_var.get()+"\n")
        self.txtBox.insert(END,"FirstName:\t\t"+self.firstName_var.get()+"\n")
        self.txtBox.insert(END,"LastName:\t\t"+self.lastName_var.get()+"\n")
        self.txtBox.insert(END,"Branch:\t\t"+self.branch_var.get()+"\n")
        self.txtBox.insert(END,"Balance:\t\t"+self.balance_var.get()+"\n")
        self.txtBox.insert(END,"Gender:\t\t"+self.gender_var.get()+"\n")
        self.txtBox.insert(END,"MobileNo:\t\t"+self.mobileNo_var.get()+"\n")
        self.txtBox.insert(END,"Pincode:\t\t"+self.pincode_var.get()+"\n")
        self.txtBox.insert(END,"AdharNo:\t\t"+self.adharNo_var.get()+"\n")
        self.txtBox.insert(END,"Account Type:\t\t"+self.accountType_var.get()+"\n")
        self.txtBox.insert(END,"IFSCCode:\t\t"+self.IFSCcode_var.get()+"\n")

    def reset(self):
        self.user_var.set(""),
        self.accountNo_var.set(""),
        self.firstName_var.set(""),
        self.lastName_var.set(""),
        self.branch_var.set(""),
        self.balance_var.set(""),
        self.gender_var.set(""),
        self.mobileNo_var.set(""),
        self.pincode_var.set(""),
        self.adharNo_var.set(""),
        self.accountType_var.set(""),
        self.IFSCcode_var.set("")
        self.txtBox.delete("1.0",END)

    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Bank Management System","Do you want to exit")
        if iExit>0:
            self.root.destroy()
            return
        
    def delete(self):
        if self.accountNo_var.get() == "" or self.branch_var.get() == "":
          messagebox.showerror("Error", "First select a user")
        else:
           try:
            # Corrected the parameter name from 'username' to 'user'
               conn = mysql.connector.connect(host="localhost", username="root", password="Shraddha#14", database="MyData1")
               my_cursor = conn.cursor()

               query = "DELETE FROM library1 WHERE accountNo = %s"  # Ensure the correct table name
               value = (self.accountNo_var.get(),)
               my_cursor.execute(query, value)

               conn.commit()
               self.fetch_data()  # Refresh the data after deletion
               self.reset()       # Reset input fields

               messagebox.showinfo("Success", "USER SUCCESSFULLY DELETED")
           except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error deleting data: {err}")
           finally:
            if conn.is_connected():
                conn.close()  # Ensure the connection is closed if it was opened



        



if __name__ == "__main__":
    root = Tk()
    obj = BankManagementSystem(root)
    root.mainloop()