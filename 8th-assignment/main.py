import json
import os
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn
from rich.prompt import Prompt, IntPrompt, FloatPrompt
from rich import box

# Initialize Rich Console
console = Console()

# Parent Class (Inheritance)
class Person:
    def __init__(self, name, id):
        self.__name = name  # Private attribute (Encapsulation)
        self.__id = id

    # Getters
    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

# Child Class (Student)
class Student(Person):
    def __init__(self, name, roll_no, marks):
        super().__init__(name, roll_no)  # Parent class constructor
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def update_marks(self, new_marks):
        if 0 <= new_marks <= 100:  # Data validation
            self.__marks = new_marks
            return True
        return False

# Child Class (Teacher)
class Teacher(Person):
    def __init__(self, name, emp_id, subject):
        super().__init__(name, emp_id)
        self.__subject = subject

    def get_subject(self):
        return self.__subject

# Main App Class (Handles File Storage + Menu)
class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.teachers = []
        self.data_file = "student_data.json"
        self.load_data()  # Load data on startup

    def save_data(self):
        data = {
            "students": [
                {"name": s.get_name(), "roll_no": s.get_id(), "marks": s.get_marks()}
                for s in self.students
            ],
            "teachers": [
                {"name": t.get_name(), "emp_id": t.get_id(), "subject": t.get_subject()}
                for t in self.teachers
            ]
        }
        with open(self.data_file, "w") as f:
            json.dump(data, f)

    def load_data(self):
        if os.path.exists(self.data_file):
            with Progress(SpinnerColumn(), transient=True) as progress:
                task = progress.add_task("[cyan]Loading data...", total=1)
                with open(self.data_file, "r") as f:
                    data = json.load(f)
                    for s in data.get("students", []):
                        self.students.append(Student(s["name"], s["roll_no"], s["marks"]))
                    for t in data.get("teachers", []):
                        self.teachers.append(Teacher(t["name"], t["emp_id"], t["subject"]))
                progress.update(task, advance=1)

    def add_student(self):
        console.print("\n[bold yellow]➕ Add New Student[/bold yellow]")
        name = Prompt.ask("Enter student name")
        roll_no = Prompt.ask("Enter roll number")
        marks = FloatPrompt.ask("Enter marks (0-100)", default=0.0)

        if not (0 <= marks <= 100):
            console.print("[bold red]❌ Invalid marks! Must be between 0-100.[/bold red]")
            return

        self.students.append(Student(name, roll_no, marks))
        self.save_data()
        console.print("[bold green]✅ Student added successfully![/bold green]")

    def view_students(self):
        if not self.students:
            console.print("[bold red]❌ No students found![/bold red]")
            return

        table = Table(title="📝 Student List", box=box.ROUNDED)
        table.add_column("Roll No", style="cyan")
        table.add_column("Name", style="magenta")
        table.add_column("Marks", style="green")

        for student in self.students:
            marks = student.get_marks()
            table.add_row(
                student.get_id(),
                student.get_name(),
                f"{marks}/100",
            )

        console.print(table)

    def search_student(self):
        roll_no = Prompt.ask("Enter roll number to search")
        found = False
        for student in self.students:
            if student.get_id() == roll_no:
                console.print("\n[bold green]🔍 Student Found:[/bold green]")
                console.print(f"Name: [cyan]{student.get_name()}[/cyan]")
                console.print(f"Roll No: [yellow]{student.get_id()}[/yellow]")
                console.print(f"Marks: [green]{student.get_marks()}/100[/green]")
                found = True
                break
        if not found:
            console.print("[bold red]❌ Student not found![/bold red]")

    def update_marks(self):
        roll_no = Prompt.ask("Enter roll number to update marks")
        for student in self.students:
            if student.get_id() == roll_no:
                new_marks = FloatPrompt.ask("Enter new marks (0-100)", default=student.get_marks())
                if not (0 <= new_marks <= 100):
                    console.print("[bold red]❌ Invalid marks! Must be between 0-100.[/bold red]")
                    return
                if student.update_marks(new_marks):
                    self.save_data()
                    console.print("[bold green]✅ Marks updated![/bold green]")
                else:
                    console.print("[bold red]❌ Invalid marks![/bold red]")
                return
        console.print("[bold red]❌ Student not found![/bold red]")

    def class_average(self):
        if not self.students:
            console.print("[bold red]❌ No students to calculate average![/bold red]")
            return

        total = sum(s.get_marks() for s in self.students)
        avg = total / len(self.students)
        console.print(f"\n📊 [bold]Class Average Marks:[/bold] [green]{avg:.2f}/100[/green]")

    def add_teacher(self):
        console.print("\n[bold yellow]➕ Add New Teacher[/bold yellow]")
        name = Prompt.ask("Enter teacher name")
        emp_id = Prompt.ask("Enter employee ID")
        subject = Prompt.ask("Enter subject")
        self.teachers.append(Teacher(name, emp_id, subject))
        self.save_data()
        console.print("[bold green]✅ Teacher added successfully![/bold green]")

    def view_teachers(self):
        if not self.teachers:
            console.print("[bold red]❌ No teachers found![/bold red]")
            return

        table = Table(title="👨‍🏫 Teacher List", box=box.ROUNDED)
        table.add_column("Emp ID", style="cyan")
        table.add_column("Name", style="magenta")
        table.add_column("Subject", style="green")

        for teacher in self.teachers:
            table.add_row(
                teacher.get_id(),
                teacher.get_name(),
                teacher.get_subject(),
            )

        console.print(table)

    def run(self):
        while True:
            console.print("\n[bold blue]==== 🎓 Student Management System ====[/bold blue]")
            console.print("1. Add Student")
            console.print("2. View All Students")
            console.print("3. Search Student")
            console.print("4. Update Marks")
            console.print("5. View Class Average")
            console.print("6. Add Teacher")
            console.print("7. View Teachers")
            console.print("8. Exit")

            choice = Prompt.ask("Enter your choice (1-8)", choices=["1", "2", "3", "4", "5", "6", "7", "8"])

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.view_students()
            elif choice == "3":
                self.search_student()
            elif choice == "4":
                self.update_marks()
            elif choice == "5":
                self.class_average()
            elif choice == "6":
                self.add_teacher()
            elif choice == "7":
                self.view_teachers()
            elif choice == "8":
                console.print("[bold yellow]Exiting...[/bold yellow]")
                break

if __name__ == "__main__":
    app = StudentManagementSystem()
    app.run()
    