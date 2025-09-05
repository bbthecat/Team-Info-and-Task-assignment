# src/main.py

def run_cli():
    """
    ฟังก์ชันหลักสำหรับรันโปรแกรม Team Info CLI
    มีลูปหลักสำหรับรอรับคำสั่งจากผู้ใช้และประมวลผล
    """

    # 1. โหลดข้อมูลสำหรับเก็บข้อมูลทีมตามที่ Planner กำหนด
    team_data = {
        'Planner': 'บี',
        'Coder': 'เจมส์',
        'Debugger': 'โอเล่'
    }

    # 2. แสดงข้อความต้อนรับเมื่อโปรแกรมเริ่มทำงาน
    print("--- Welcome to Team Info CLI ---")
    print("Available commands: [view, add, remove, quit]")

    # 3. ลูปหลักของโปรแกรม (ทำงานไปเรื่อยๆ จนกว่าจะสั่ง break)
    while True:
        command = input("\nEnter command: ").lower()

        # 4. ตรวจสอบและจัดการคำสั่งด้วย if/elif/else
        if command == 'view':
            print("\nTeam Members:")
            # วนลูปเพื่อแสดงข้อมูลสมาชิกทุกคนในทีม
            for role, name in team_data.items():
                print(f"- {role}: {name}")
        
        elif command == 'add':
            role = input("Enter role : ").capitalize()
            name = input("Enter name : ")
            team_data[role]=name
            print(f"Add {role}: {name}")

        elif command == 'remove':
            print("\nTeam Members:")
            # วนลูปเพื่อแสดงข้อมูลสมาชิกทุกคนในทีม
            for role, name in team_data.items():
                print(f"- {role}")
            role = input("\nEnter role to remove: ").capitalize()
            if role in team_data:
                removed_name = team_data.pop(role)
                print(f"Removed {role}: {removed_name}")
            else:
                print(f"Role '{role}' not found in team.")

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