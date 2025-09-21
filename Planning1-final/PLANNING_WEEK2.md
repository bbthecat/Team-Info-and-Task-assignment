# แผนการทำงานสำหรับ Sprint 2: Member Management

## เป้าหมาย
- เพิ่มคำสั่ง `add` และ `remove` เพื่อจัดการสมาชิกทีม

## Definition of Done (DoD)
- โปรแกรมรันได้โดยไม่มี error
- เมนูคำสั่งเริ่มต้น แสดง `[view, add, remove, quit]`
- เมื่อใช้คำสั่ง `add` สามารถเพิ่มสมาชิกใหม่ได้จริง และเมื่อใช้ `view` จะเห็นสมาชิกใหม่
- เมื่อใช้คำสั่ง `remove` กับบทบาทที่มีอยู่ สมาชิกจะถูกลบออกไปจริง และเมื่อใช้ `view` จะไม่เห็นสมาชิกคนนั้นแล้ว
- เมื่อใช้คำสั่ง `remove` กับบทบาทที่ ไม่มีอยู่ โปรแกรมจะแสดงข้อความแจ้งเตือนและทำงานต่อได้ปกติ
- คำสั่งเก่า (`view`, `quit`) ยังคงทำงานได้เหมือนเดิม (Regression Test)

## Test Cases (สำหรับ Debugger)
- **Case 1: Happy Path (Add):**
  - **Action:** พิมพ์ `add` -> `Tester` -> `Ole`
  - **Expected:** โปรแกรมแสดง `"Added Tester: Ole"` จากนั้นพิมพ์ `view` แล้วต้องเห็น `Tester: Ole` ในรายชื่อ
- **Case 2: Happy Path (Remove):**
  - **Action:** พิมพ์ `remove` -> `Coder`
  - **Expected:** โปรแกรมแสดง `"Removed Coder: เจมส์"` จากนั้นพิมพ์ `view` แล้วต้องไม่เห็น `Coder` ในรายชื่อ
- **Case 3: Edge Case (Remove Non-Existent Role):**
  - **Action:** พิมพ์ `remove` -> `Manager`
  - **Expected:** โปรแกรมแสดงข้อความ `"Error: Role 'Manager' not found in the team."` และวนกลับไปรอรับคำสั่งใหม่
- **Case 4: Regression Test:**
  - **Action:** ทดสอบคำสั่ง `view` และ `quit` อีกครั้ง
  - **Expected:** ต้องยังทำงานได้ปกติเหมือนสัปดาห์ที่ 1
