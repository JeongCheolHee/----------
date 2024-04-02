from src.ListQueue import *
import threading
import time

normal = ListQueue()
gold = ListQueue()
platinum = ListQueue()

class Producer:
    def __init__(self, items):
        self.__alive = True
        self.items = items
        self.pos = 0
        self.worker = threading.Thread(target=self.run)

    def get_item(self):
        if self.pos < len(self.items):
            item = self.items[self.pos]
            self.pos += 1
            return item
        else:
            return None

    def run(self):
        while self.__alive:
            time.sleep(0.2)
            item = self.get_item()
            if item:
                print("Arrived", item)
                # 등급에 따라 해당 큐에 넣기
                if item[0] == '1':
                    normal.enqueue(item)
                elif item[0] == '2':
                    gold.enqueue(item)
                elif item[0] == '3':
                    platinum.enqueue(item)
        print("Producer is dying")

    def start(self):
        self.worker.start()

    def finish(self):
        self.__alive = False
        self.worker.join()

class Consumer:
    def __init__(self):
        self.__alive = True
        self.worker = threading.Thread(target=self.run)

    def run(self):
        while self.__alive or not (platinum.isEmpty() and gold.isEmpty() and normal.isEmpty()):
            # 등급이 높은 순서대로 큐를 확인하여 탑승 처리
            for queue in [platinum, gold, normal]:
                if not queue.isEmpty():
                    boarding = queue.dequeue()
                    print("Boarding:", boarding)
                    time.sleep(1)
                    break  # 등급별로 한 명씩 처리 후 다시 높은 등급부터 확인
        print("Consumer is dying")

    def start(self):
        self.worker.start()

    def finish(self):
        self.__alive = False
        self.worker.join()

if __name__ == "__main__":
    customers = []
    with open("C:/Users/USER/structure-3/Queue/data/customer.txt", 'r') as file:
        lines = file.readlines()
        for line in lines:
            customer = line.strip().split()
            customers.append(customer)

    producer = Producer(customers)
    consumer = Consumer()
    producer.start()
    consumer.start()

    # 주어진 시간 동안 실행
    time.sleep(10)

    # 작업 완료 후 스레드 종료
    producer.finish()
    consumer.finish()
