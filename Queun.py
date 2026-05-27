from collections import deque
import threading
import time

class Queue:
    def __init__(self):
        self.queue = deque()#deque is a double-ended queue that allows for efficient appending and popping from both ends. It is used here to implement the queue data structure, providing O(1) time complexity for enqueue and dequeue operations.

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        else:
            raise IndexError("Queue is empty")

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("Queue is empty")

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)
    
    
#ข้อ 1: สร้างระบบร้านอาหารที่มีการใช้คิว (Queue) ในการจัดการคำสั่งซื้ออาหาร โดยมีร่างแยก (Thread) 2 ตัวทำงานคู่ขนานกัน ดังนี้:   
def order(order_list,food_queue):
    for item in order_list:
        print(f"Order placed: {item}")
        food_queue.enqueue(item)
        time.sleep(0.5)  # Simulate time taken to place an order
        
def serve(food_queue):
    time.sleep(1)  # Simulate time taken to prepare the first order
    while True:
        if not food_queue.is_empty():
            item = food_queue.dequeue()
            print(f"Order served: {item}")
            time.sleep(2)  # Simulate time taken to serve an order
        else:
            print("No more orders to serve.")
            break
        
if __name__ == "__main__":
    # สมมติมีคลาส Queue และลิสต์อาหารเตรียมไว้แล้ว
    food_queue = Queue()
    order_list = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']

    # 1. สร้างร่างแยก (Thread) 2 ตัว
    # ส่ง food_queue และลิสต์อาหารผ่านพารามิเตอร์ args
    t1 = threading.Thread(target=order, args=(order_list,food_queue))
    t2 = threading.Thread(target=serve, args=(food_queue,))

    # 2. สั่งให้ร่างแยกทั้งสองเริ่มทำงานพร้อมกันแบบคู่ขนาน
    t1.start()
    t2.start()

    # 3. สั่งให้โปรแกรมหลัก (Main Thread) รอให้ร่างแยกทำงานเสร็จก่อนถึงจะจบโปรแกรม
    t1.join()
    t2.join()
    print("จบการทำงานของระบบร้านอาหาร")
    
# ข้อ 2
def eiei (n):
    q = Queue()
    q.enqueue("1")
    
    for i in range(n):  
        peek = q.dequeue() # ดึงค่าที่อยู่หน้าคิวออกมาเพื่อใช้งาน
        print(peek)  # แสดงค่าที่อยู่หน้าคิว
        
        q.enqueue(peek + "0")
        q.enqueue(peek + "1")
        
if __name__ == "__main__":
    n = 10  # จำนวนรอบที่ต้องการ
    eiei(n)