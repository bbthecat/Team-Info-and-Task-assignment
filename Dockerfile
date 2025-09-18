# ใช้ Python 3.9 เป็น base image
FROM python:3.9-slim

# ตั้งค่า working directory
WORKDIR /app

# คัดลอกไฟล์ dependencies
COPY requirements.txt .

# ติดตั้ง dependencies
RUN pip install --no-cache-dir -r requirements.txt

# คัดลอก source code ทั้งหมด
COPY ./src /app/src
COPY ./data /app/data

# Expose port ที่ FastAPI จะรัน
EXPOSE 8000

# คำสั่งสำหรับรันแอปพลิเคชันเมื่อ container เริ่มทำงาน
# --host 0.0.0.0 เพื่อให้สามารถเข้าถึงได้จากภายนอก container
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]