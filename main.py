import tkinter as tk
import tkinter.messagebox as messagebox

from database.database import create_database, save_student


def register_student():
    register_window = tk.Toplevel()

    register_window.title("Register Student")
    register_window.geometry("400x300")

    # Labels
    tk.Label(register_window, text="Student ID").grid(
        row=0, column=0, padx=10, pady=10)
    tk.Label(register_window, text="Name").grid(
        row=1, column=0, padx=10, pady=10)
    tk.Label(register_window, text="Class").grid(
        row=2, column=0, padx=10, pady=10)
    tk.Label(register_window, text="School Fee").grid(
        row=3, column=0, padx=10, pady=10)

    # Entry boxes
    student_id_entry = tk.Entry(register_window)
    name_entry = tk.Entry(register_window)
    class_entry = tk.Entry(register_window)
    fee_entry = tk.Entry(register_window)

    student_id_entry.grid(row=0, column=1)
    name_entry.grid(row=1, column=1)
    class_entry.grid(row=2, column=1)
    fee_entry.grid(row=3, column=1)

    def save():
        try:
            student_id = student_id_entry.get()
            name = name_entry.get()
            student_class = class_entry.get()
            school_fee = float(fee_entry.get())

            saved = save_student(
                student_id,
                name,
                student_class,
                school_fee
)
            if (
                        not student_id.strip()
                        or not name.strip()
                        or not student_class.strip()
                        or not fee_entry.get().strip()
                      ):
                     messagebox.showerror(
                    "Missing Information",
                    "Please fill in all fields."
                )
                     return    

            if saved:
                messagebox.showinfo(
                    "Success",
                    "Student registered successfully!"
                )
                register_window.destroy()
            else:
                messagebox.showerror(
                    "Duplicate Student",
                    "A student with this ID already exists."
                )

            

        except ValueError:
            messagebox.showerror(
                "Error",
                "School fee must be a number."
            )
            
        

    save_button = tk.Button(
        register_window,
        text="Save Student",
        command=save
    )

    save_button.grid(
        row=4,
        column=1,
        pady=20
    )


def record_payment():
    print("Record Payment clicked")


def search_student():
    print("Search Student clicked")


def payment_history():
    print("Payment History clicked")


def main():
    # Create the database when the application starts
    create_database()

    # Create the main window
    root = tk.Tk()

    # Window title
    root.title("School Fee Payment Tracker")

    # Window size
    root.geometry("500x400")

    # Prevent resizing (optional)
    root.resizable(False, False)

    # Heading
    heading = tk.Label(
        root,
        text="School Fee Payment Tracker",
        font=("Arial", 18, "bold")
    )
    heading.pack(pady=20)
    register_button = tk.Button(
        root,
        text="Register Student",
        width=25,
        height=2,
        command=register_student,
    )

    register_button.pack(pady=5)

    payment_button = tk.Button(
        root,
        text="Record Payment",
        width=25,
        height=2,
        command=record_payment,
    )

    payment_button.pack(pady=5)

    search_button = tk.Button(
        root,
        text="Search Student",
        width=25,
        height=2,
        command=search_student,
    )

    search_button.pack(pady=5)

    history_button = tk.Button(
        root,
        text="Payment History",
        width=25,
        height=2,
        command=payment_history,
    )

    history_button.pack(pady=5)

    exit_button = tk.Button(
        root,
        text="Exit",
        width=25,
        height=2,
        command=root.destroy,
    )

    exit_button.pack(pady=20)
# Start the application
    root.mainloop()


if __name__ == "__main__":
    main()
