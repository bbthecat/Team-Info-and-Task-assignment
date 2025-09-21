# 🚀 โปรเจกต์: Team-Info-and-Task-assignment

โปรเจกต์นี้เป็นแอปพลิเคชัน Team-Info-and-Task-assignment สำหรับจัดการและแสดงข้อมูลทีม สร้างขึ้นเพื่อฝึกฝนการทำงานร่วมกันแบบ Agile, การใช้ Git/GitHub, และการแบ่งหน้าที่ในทีมพัฒนาระหว่าง Planner, Coder, และ Debugger

---

## 🛠️ วิธีการรันโปรเจกต์

1.  Clone a repository ลงมาที่เครื่องของคุณ:
    ```bash
    git clone https://github.com/bbthecat/Team-Info-and-Task-assignment.git
    ```
2.  เข้าไปที่โฟลเดอร์ของโปรเจกต์:
    ```bash
    cd Team-Info-and-Task-assignment
    ```
3.  รันไฟล์หลัก:
    ```bash
    python main.py
    ```


---
---

## 🎯 Sprint : Final Sprint - From CLI to Web Application

**สถานะ:** ✅ เสร็จสิ้น

---

### 📋 **เป้าหมายของสัปดาห์**
- เพื่อเปลี่ยนโปรเจกต์จาก Command-Line Interface (CLI) ให้เป็น **Web Application** เต็มรูปแบบที่ใช้งานผ่านเบราว์เซอร์ได้ โดยจะมีการพัฒนา **Backend API** เพื่อจัดการข้อมูล และสร้าง **Frontend UI** (HTML, CSS, JS) เพื่อให้ผู้ใช้สามารถดู, เพิ่ม, และลบข้อมูลได้แบบ Dynamic โดยไม่ต้องรีเฟรชหน้าจอ

---

### 🧑‍💻 **บทบาทสัปดาห์นี้**
* **Planner** 🗺️: **โอเล่**
    * **ภารกิจ**: ออกแบบสถาปัตยกรรมของ Web Application ทั้ง API และโครงสร้างหน้าเว็บ (Wireframe) พร้อมทั้งวางแผนและแบ่ง Task ย่อยๆ ของ Sprint นี้
* **Coder** 💻: **บี**
    * **ภารกิจ**: พัฒนา Web Application ทั้งส่วน Backend (ด้วย FastAPI/Flask) และ Frontend (HTML, CSS, JS) ตามที่ Planner ออกแบบไว้
* **Debugger** 🕵️‍♂️: **เจมส์**
    * **ภารกิจ**: ทดสอบความถูกต้องของ API Endpoints และทดสอบหน้าเว็บในฐานะผู้ใช้จริง (User Acceptance Test) เพื่อหา Bug และตรวจสอบว่าข้อมูลถูกบันทึกลงไฟล์ JSON ถูกต้อง

---

### ✔️ **นิยามของคำว่า "เสร็จ" (Definition of Done)**
* [✔] โปรแกรมสามารถรันในรูปแบบ Web Server บนเครื่อง Local ได้
* [✔] ผู้ใช้สามารถเปิดเบราว์เซอร์และเข้าใช้งานแอปพลิเคชันผ่าน `localhost` ได้
* [✔] ฟังก์ชันทั้งหมด (View, Add Member, Add Assignment, Remove) สามารถทำงานผ่านหน้าเว็บได้ครบถ้วน
* [✔] ข้อมูลยังคงถูกบันทึกและอ่านจากไฟล์ `.json` ได้อย่างถูกต้อง
* [✔] (Stretch Goal) โปรเจกต์ถูก "Containerize" ด้วย `Dockerfile` เพื่อเตรียมพร้อมสำหรับการ Deploy ในอนาคต

---
---

## 📚 ประวัติ Sprint (Sprint Log)

*เมื่อจบ Sprint ในแต่ละสัปดาห์ เราจะย้ายสรุปของสัปดาห์นั้นมาเก็บไว้ที่นี่*

<details>
  <summary>คลิกเพื่อดู Sprint ที่ผ่านมา</summary>
    - **Sprint1 / Week 1** --- https://colab.research.google.com/drive/1lYKohn3Qxv-M3jVvpBQK3So5V5FLYqqp?usp=sharing <br>
    - **Sprint2 / Week 2** --- https://colab.research.google.com/drive/1CeILnUVqAzTSNgHYBrSbbdL1d0-9RtbE?usp=sharing <br>
    - **Sprint3 / Week 3** --- https://colab.research.google.com/drive/1YzWTm_wB6IIQR52D7-emCozVJiwA0Ai4?usp=sharing <br>
    - **Sprint final    ** --- https://colab.research.google.com/drive/1tkngKFgDVK4jq3B2HbdXsXk7_OcDMVIw?usp=sharing 
  </details>
