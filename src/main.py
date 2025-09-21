from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List, Dict

import src.data_api as data_api
import src.ai_service as ai_service

app = FastAPI()

# --- Pydantic Models for Request Bodies ---
class Member(BaseModel):
    name: str
    role: str

class Assignment(BaseModel):
    name: str
    task: str

class AITaskRequest(BaseModel):
    task_description: str
    
# --- Data Management ---
team_data, task_data = data_api.load_data()

def persist_data():
    """Helper function to save data to files"""
    data_api.save_data(team_data, task_data)

# --- API Endpoints ---
@app.get("/api/data")
async def get_all_data():
    """ดึงข้อมูลทีมและงานทั้งหมด"""
    return {"teams": team_data, "tasks": task_data}

@app.post("/api/members")
async def add_member(member: Member):
    """เพิ่มสมาชิกใหม่"""
    role = member.role.capitalize()
    name = member.name
    
    if role not in team_data:
        team_data[role] = []
    
    if name not in team_data[role]:
        team_data[role].append(name)
    
    if name not in task_data:
        task_data[name] = []
        
    persist_data()
    return {"message": f"Member '{name}' added to role '{role}'."}

@app.post("/api/assignments")
async def add_assignment(assignment: Assignment):
    """เพิ่มงานใหม่ให้สมาชิก"""
    name = assignment.name
    task = assignment.task
    
    member_exists = any(name in members for members in team_data.values())
    if not member_exists:
        raise HTTPException(status_code=404, detail=f"Member '{name}' not found.")
        
    if name not in task_data:
        task_data[name] = []
        
    task_data[name].append(task)
    persist_data()
    return {"message": f"Task '{task}' assigned to '{name}'."}

@app.delete("/api/members/{name}")
async def remove_member(name: str):
    """ลบสมาชิกและงานของพวกเขา"""
    role_to_remove_from = None
    member_found = False
    
    for role, members in team_data.items():
        if name in members:
            members.remove(name)
            member_found = True
            if not members: # ถ้า role ไม่มีสมาชิกเหลือแล้ว
                role_to_remove_from = role
            break
            
    if role_to_remove_from:
        del team_data[role_to_remove_from]
        
    if name in task_data:
        del task_data[name]
        
    if not member_found:
        raise HTTPException(status_code=404, detail=f"Member '{name}' not found.")
        
    persist_data()
    return {"message": f"Member '{name}' and their tasks have been removed."}

@app.post("/api/tasks/generate")
async def generate_ai_tasks(request: AITaskRequest):
    """ใช้ AI เพื่อแตกย่อยงาน"""
    if not request.task_description:
        raise HTTPException(status_code=400, detail="Task description cannot be empty.")
    
    subtasks = ai_service.generate_subtasks(request.task_description)
    return {"subtasks": subtasks}

# --- Serve Frontend ---
# ต้องอยู่ท้ายสุดเพื่อให้ API endpoints ถูกลงทะเบียนก่อน
app.mount("/", StaticFiles(directory="src/static", html=True), name="static")