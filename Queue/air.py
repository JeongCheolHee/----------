#3. A항공사는 고객 등급을 일반, 골드, 플래티넘 회원으로 나누어 관리한다. 
#비행기 탑승 시 등급이 높은 순서대로 (일반 < 골드 < 플래티넘) 탑승하고, 동일 등급 내에서는 도착한 순서대로 탑승한다. 
#고객이 도착했을 때 위와 같은 순서로 탑승을 하도록 하는 프로그램을 만드시오. 

from src.ListQueue import *

def boarding(customers):
    normal = ListQueue()
    gold = ListQueue()
    platinum = ListQueue()
    
    # 올바른 속성과 값을 사용하여 등급별로 분류
    for customer in customers:
            if customer[0] == '1':
                normal.enqueue(customer)
            elif customer[0] == '2': 
                gold.enqueue(customer)
            elif customer[0] == '3': 
                platinum.enqueue(customer)
    
    # 등급별로 탑승 처리
    for queue in [platinum, gold, normal]:
        while not queue.isEmpty():
            customer = queue.dequeue()
            print(f"{customer[1]} 님이 탑승했습니다 ({customer[0]} grade)")

customers = []
with open("C:/Users/USER/structure-3/Queue/data/customer.txt", 'r') as file:
    lines = file.readlines()
    for line in lines:
        customer = line.split()
        customers.append(customer)

boarding(customers)



