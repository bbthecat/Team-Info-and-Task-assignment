import json
import os
from typing import Dict, List, Union

TEAM_FILE = os.path.join('data', 'team.json')
TASK_FILE = os.path.join('data', 'task.json')

# สร้างโฟลเดอร์ data หากยังไม่มี
os.makedirs('data', exist_ok=True)

def load_data() -> (Dict[str, List[str]], Dict[str, List[str]]):
    """โหลดข้อมูลทีมและงานจากไฟล์ JSON"""
    if not os.path.exists(TEAM_FILE):
        with open(TEAM_FILE, 'w', encoding='utf-8') as f:
            json.dump({}, f)
    
    if not os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'w', encoding='utf-8') as f:
            json.dump({}, f)

    try:
        with open(TEAM_FILE, 'r', encoding='utf-8') as f:
            team_data = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        team_data = {}

    try:
        with open(TASK_FILE, 'r', encoding='utf-8') as f:
            task_data = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        task_data = {}
        
    return team_data, task_data

def save_data(team_data: Dict[str, List[str]], task_data: Dict[str, List[str]]):
    """บันทึกข้อมูลทีมและงานลงไฟล์ JSON"""
    with open(TEAM_FILE, 'w', encoding='utf-8') as f:
        json.dump(team_data, f, ensure_ascii=False, indent=4)
    with open(TASK_FILE, 'w', encoding='utf-8') as f:
        json.dump(task_data, f, ensure_ascii=False, indent=4)