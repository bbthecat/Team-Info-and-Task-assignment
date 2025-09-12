# src/main.py
# hello where is my github
import json
import os

def load_team():
    """โหลดข้อมูลทีมจาก team.json ถ้าไม่มีไฟล์ให้คืนค่า dict ว่าง"""
    if os.path.exists("team.json"):
        with open("team.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return {
        "Coder": [
            "เจมส์"
        ],
        "Debugger": [
            "โอเล่"
        ],
        "Tester": [
            "john"
        ],
        "Planner": [
            "bee"
        ]
    }

def save_team(team_data):
    """บันทึกข้อมูลทีมลงไฟล์ team.json"""
    with open("team.json", "w", encoding="utf-8") as f:
        json.dump(team_data, f, ensure_ascii=False, indent=4)

def load_task():
    """โหลดข้อมูลทีมจาก team.json ถ้าไม่มีไฟล์ให้คืนค่า dict ว่าง"""
    if os.path.exists("task.json"):
        with open("task.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return {
        "เจมส์": [
            "Final"
        ],
        "โอเล่": [
            "Final"
        ],
        "john": [
            "Final"
        ],
        "bee": [
            "Final"
        ]
    }

def save_task(task_data):
    """บันทึกข้อมูลทีมลงไฟล์ team.json"""
    with open("task.json", "w", encoding="utf-8") as f:
        json.dump(task_data, f, ensure_ascii=False, indent=4)

def run_cli():
    """
    ฟังก์ชันหลักสำหรับรันโปรแกรม Team Info CLI
    มีลูปหลักสำหรับรอรับคำสั่งจากผู้ใช้และประมวลผล
    """

    # 1. โหลดข้อมูลสำหรับเก็บข้อมูลทีมตามที่ Planner กำหนด
    team_data = load_team()
    task_data = load_task()

    # 2. แสดงข้อความต้อนรับเมื่อโปรแกรมเริ่มทำงาน
    print("--- Welcome to Team Info CLI ---")
    print("Available commands: [view, add member, add assignment, remove, clear, quit]")

    # 3. ลูปหลักของโปรแกรม (ทำงานไปเรื่อยๆ จนกว่าจะสั่ง break)
    while True:
        command = input("\nEnter command: ").lower()

        # 4. ตรวจสอบและจัดการคำสั่งด้วย if/elif/else
        if command == 'view':
            if (team_data ) == {} :
                print("!!!Data is nothing!!!")
            else :
                role_groups = team_data
                role = []
                for r, name in team_data.items():
                    if r not in role:
                        role.append(r)

                print("\nTeam Members:")
                # วนลูปเพื่อแสดงข้อมูลสมาชิกทุกคนในทีม
                print("--------------------------------------------------------------------------------------------------------------------")
                for i in role:
                    print(f"- {i:<12}", end="")
                print()
                print("--------------------------------------------------------------------------------------------------------------------")
                
                max_len = max(len(names) for names in role_groups.values())

                # แสดง Name
                for i in range(max_len):
                    for r in role_groups:
                        names = role_groups[r]
                        if i < len(names):
                            print(f"  {names[i]:<12}", end="")
                        else:
                            print(f"  {'':<12}", end="")
                    print()
                print()


                #task show
                task_groups = task_data
                tname = []
                for tn, p in task_data.items():
                    if tn not in tname:
                        tname.append(tn)

                print("\nTask Assignment:")
                # วนลูปเพื่อแสดงข้อมูลสมาชิกทุกคนในทีม
                print("--------------------------------------------------------------------------------------------------------------------")
                for i in tname:
                    print(f"- {i:<12}", end="")
                print()
                print("--------------------------------------------------------------------------------------------------------------------")
                
                max_len = max(len(Name) for Name in task_groups.values())

                # แสดง Name
                for i in range(max_len):
                    for n in task_groups:
                        Name = task_groups[n]
                        if i < len(Name):
                            print(f"  {Name[i]:<11}", end="")
                        else:
                            print(f"  {'':<12}", end="")
                    print()
                print()

        elif command == 'add member':
            role = input("Enter role : ").capitalize()
            newname = input("Enter name : ")

            task_data[newname] = []

            n = []
            for r, name in team_data.items() :
                if role in r:
                    if isinstance(name, list):
                        n = name
                    else :
                        n.append(name)
            n.append(newname)
            team_data[role]=n
            print(f"Add {role}: {newname}")
            save_team(team_data)
            save_task(task_data)

        elif command == 'add assignment':
            name = input("Enter name : ")
            newtask = input("Enter task : ")

            t = []
            for n, task in team_data.items() :
                if name in n:
                    if isinstance(task, list):
                        t = task
                    else :
                        t.append(task)
            t.append(newtask)
            task_data[name]=t
            print(f"Add {name}: {newtask}")
            save_team(team_data)
            save_task(task_data)

        elif command == 'remove':
            print("\nTeam Members:")
            # วนลูปเพื่อแสดงข้อมูลสมาชิกทุกคนในทีม
            for role, name in team_data.items():
                print(f"- {role}")
            role = input("\nEnter role to remove: ").capitalize()
            if role in team_data:
                removed_name = team_data.pop(role)
                print(f"Removed {role}: {removed_name}")
                save_team(team_data)

                for name in removed_name:
                    task_data.pop(name)

                save_task(task_data)
            else:
                print(f"Role '{role}' not found in team.")

        elif command == 'clear':
            print("--- clear everything!!! ---")
            cont = input(str("Do you want to clear data (y/n): ")).lower()
            if cont == 'y':
                team_data.clear()
                task_data.clear()
                save_team(team_data)
                save_task(task_data)
            else:
                print(" ")

        elif command == 'quit':
            print("--- Thank you for using Team Info CLI! ---")
            break  # ออกจาก while loop และจบการทำงานของโปรแกรม
        
        else:
            # กรณีที่ผู้ใช้พิมพ์คำสั่งที่ไม่รู้จัก
            print(f"Error: Unknown command '{command}'. Please try again.")

# บรรทัดมาตรฐานของ Python เพื่อให้แน่ใจว่าฟังก์ชัน run_cli() จะถูกเรียกใช้
# ก็ต่อเมื่อไฟล์นี้ถูกรันโดยตรงเท่านั้น
if __name__ == "__main__":
    run_cli()
