import datetime
import os

class Task:
    def __init__(self, title, category, priority, due_date):
        self.title = title
        self.category = category
        self.priority = priority
        self.due_date = due_date

    def __str__(self):
        return f"任务名：{self.title}\n分类：{self.category}\n优先级：{self.priority}\n到期日期：{self.due_date}\n"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    print("1. 添加任务")
    print("2. 查看任务")
    print("3. 提醒任务")
    print("4. 退出")

def add_task():
    title = input("请输入任务名: ")
    category = input("请输入任务分类: ")
    priority = input("请输入任务优先级 (高/中/低): ")
    due_date = input("请输入任务到期日期 (YYYY-MM-DD): ")

    task = Task(title, category, priority, due_date)
    tasks.append(task)
    print("任务添加成功！")

def show_tasks():
    if len(tasks) == 0:
        print("当前没有任务。")
    else:
        for idx, task in enumerate(tasks):
            print(f"\n任务编号：{idx+1}")
            print(task)

def remind_tasks():
    current_date = datetime.date.today()

    for task in tasks:
        due_date = datetime.datetime.strptime(task.due_date, "%Y-%m-%d").date()
        if due_date >= current_date:
            print(f"\n待办任务提醒：{task.title}\n到期日期：{task.due_date}")

tasks = []

while True:
    clear_screen()
    show_menu()

    choice = input("\n请选择操作编号: ")

    if choice == "1":
        clear_screen()
        add_task()
        input("\n按 Enter 键返回菜单...")
    elif choice == "2":
        clear_screen()
        show_tasks()
        input("\n按 Enter 键返回菜单...")
    elif choice == "3":
        clear_screen()
        remind_tasks()
        input("\n按 Enter 键返回菜单...")
    elif choice == "4":
        break
    else:
        print("无效的选择，请重新输入。")
        input("\n按 Enter 键返回菜单...")

print("任务管理工具已退出。")