import json
import os

def load_team():
    """โหลดข้อมูลทีมจาก team.json ถ้าไม่มีไฟล์ให้คืนค่า dict ที่มีข้อมูลเริ่มต้น"""
    if os.path.exists("team.json"):
        with open("team.json", "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {} # หากไฟล์เสียหาย คืนค่า dict ว่าง
    return {
        "Coder": ["เจมส์"],
        "Debugger": ["โอเล่"],
        "Planner": ["บี"]
    }

def save_team(team_data):
    """บันทึกข้อมูลทีมลงไฟล์ team.json"""
    with open("team.json", "w", encoding="utf-8") as f:
        json.dump(team_data, f, ensure_ascii=False, indent=4)

def load_task():
    """โหลดข้อมูลงานจาก task.json ถ้าไม่มีไฟล์ให้คืนค่า dict ที่มีข้อมูลเริ่มต้น"""
    if os.path.exists("task.json"):
        with open("task.json", "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {} # หากไฟล์เสียหาย คืนค่า dict ว่าง
    return {
        "เจมส์": ["Implement auth feature"],
        "โอเล่": ["Test login flow"],
        "บี": ["Plan next sprint"]
    }

def save_task(task_data):
    """บันทึกข้อมูลงานลงไฟล์ task.json"""
    with open("task.json", "w", encoding="utf-8") as f:
        json.dump(task_data, f, ensure_ascii=False, indent=4)

def run_cli():
    """
    ฟังก์ชันหลักสำหรับรันโปรแกรม Team Info CLI
    มีลูปหลักสำหรับรอรับคำสั่งจากผู้ใช้และประมวลผล
    """
    team_data = load_team()
    task_data = load_task()

    print("--- Welcome to Team Info CLI ---")
    print("Available commands: [view, add member, add assignment, remove, clear, quit]")

    while True:
        command = input("\nEnter command: ").lower()

        if command == 'view':
            if not team_data:
                print("!!! No team data to display !!!")
            else:
                print("\nTeam Members:")
                print("-" * 50)
                for role, members in team_data.items():
                    print(f"- {role:<15}: {', '.join(members)}")
                print("-" * 50)

            if not task_data:
                print("\n!!! No task assignments to display !!!")
            else:
                print("\nTask Assignment:")
                print("-" * 50)
                for member, tasks in task_data.items():
                    print(f"- {member:<15}:")
                    if tasks:
                        for task in tasks:
                            print(f"  - {task}")
                    else:
                        print("  (No tasks assigned)")
                print("-" * 50)

        elif command == 'add member':
            role = input("Enter role : ").capitalize()
            new_name = input("Enter name : ")

            # ตรวจสอบว่า role นี้มีอยู่แล้วหรือไม่
            if role in team_data:
                # ถ้ามีแล้ว ก็เพิ่มชื่อใหม่เข้าไปใน list เดิม
                team_data[role].append(new_name)
            else:
                # ถ้ายังไม่มี ให้สร้าง key ใหม่พร้อมกับ list ที่มีชื่อคนแรก
                team_data[role] = [new_name]
            
            # เพิ่มชื่อใหม่เข้าไปใน task_data เพื่อให้พร้อมรับงาน
            if new_name not in task_data:
                task_data[new_name] = []

            print(f"Added '{new_name}' to role '{role}'")
            save_team(team_data)
            save_task(task_data)

        elif command == 'add assignment':
            name = input("Enter name : ")
            # ตรวจสอบก่อนว่ามีชื่อสมาชิกคนนี้ในระบบหรือไม่
            member_exists = any(name in names for names in team_data.values())
            
            if not member_exists:
                print(f"Error: Member '{name}' not found.")
                continue

            new_task = input("Enter task : ")

            # ดึงรายการ task เดิมของ 'name' มา (ถ้าไม่มีให้สร้าง list ว่าง)
            tasks = task_data.get(name, [])
            
            # เพิ่ม task ใหม่เข้าไปใน list
            tasks.append(new_task)
            
            # อัปเดตข้อมูลกลับเข้าไปใน dictionary
            task_data[name] = tasks
            
            print(f"Added task '{new_task}' to '{name}'")
            save_task(task_data) # บันทึกเฉพาะไฟล์ task.json ก็พอ

        elif command == 'remove':
            name_to_remove = input("Enter name of the member to remove: ")
            role_to_delete = None
            member_found = False

            for role, members in team_data.items():
                if name_to_remove in members:
                    members.remove(name_to_remove)
                    member_found = True
                    # ถ้า role นั้นไม่มีสมาชิกเหลือแล้ว ให้เก็บชื่อ role ไว้เพื่อลบทีหลัง
                    if not members:
                        role_to_delete = role
                    break
            
            if role_to_delete:
                del team_data[role_to_delete]
            
            if member_found:
                if name_to_remove in task_data:
                    del task_data[name_to_remove]
                print(f"Removed member '{name_to_remove}' and their tasks.")
                save_team(team_data)
                save_task(task_data)
            else:
                print(f"Error: Member '{name_to_remove}' not found.")

        elif command == 'clear':
            confirm = input("Are you sure you want to clear all data? (y/n): ").lower()
            if confirm == 'y':
                team_data.clear()
                task_data.clear()
                save_team(team_data)
                save_task(task_data)
                print("--- All data has been cleared. ---")
            else:
                print("Clear operation cancelled.")

        elif command == 'quit':
            print("--- Thank you for using Team Info CLI! ---")
            break

        else:
            print(f"Error: Unknown command '{command}'. Please try again.")

if __name__ == "__main__":
    run_cli()