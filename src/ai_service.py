import os
import google.generativeai as genai
import re
import ast

def configure_ai():
    """ตั้งค่า API Key จาก Environment Variable"""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable not set.")
    genai.configure(api_key=api_key)

def generate_subtasks(high_level_task: str) -> list[str]:
    """ส่ง high-level task ไปให้ Gemini API และขอให้แตกเป็น sub-tasks"""
    try:
        configure_ai()
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        
        prompt = f"""
        Analyze the following high-level software development task. 
        Break it down into a concise list of smaller, actionable sub-tasks.
        Return the response *only* as a valid Python list of strings. Do not include any other text or explanation.
        Example format: ["Design the database schema", "Create API endpoints", "Develop the frontend UI"]

        High-level task: "{high_level_task}"

        Sub-tasks:
        """

        response = model.generate_content(prompt)
        
        # ใช้ Regular Expression เพื่อหา list ที่อยู่ใน text ตอบกลับ
        match = re.search(r'\[.*\]', response.text, re.DOTALL)
        if match:
            list_str = match.group(0)
            # ใช้ ast.literal_eval เพื่อแปลง string เป็น list อย่างปลอดภัย
            subtasks = ast.literal_eval(list_str)
            return subtasks
        return []

    except Exception as e:
        print(f"An error occurred with the AI service: {e}")
        return ["Error: Could not generate tasks."]