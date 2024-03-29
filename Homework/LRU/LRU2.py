# Circularlikedlist 이용
import sys
sys.path.append('c:\\Users\\USER\\structure-3') 

from list.src.model.circularlikedlist import CircularLinkedList

class LRUCacheSimulator:
    def __init__(self, cache_slots):
        self.cache_slots = cache_slots
        self.cache = CircularLinkedList()
        self.cache_hit = 0
        self.tot_cnt = 0

    def do_sim(self, page):
        self.tot_cnt += 1
        found = False

        # 캐시 내에서 페이지 검색
        for i, item in enumerate(self.cache):
            if item == page:
                found = True
                break

        if found:
            # 캐시 히트: 페이지를 리스트 끝으로 이동
            self.cache_hit += 1
            self.cache.pop(i)  # 페이지 제거
            self.cache.append(page)  # 페이지를 리스트 끝에 다시 삽입
        else:
            # 캐시 미스: 캐시가 꽉 찼다면, 가장 오래된 페이지 제거
            if self.tot_cnt > self.cache_slots:
                self.cache.pop(0)
            self.cache.append(page)

    def print_stats(self):
        hit_ratio = self.cache_hit / self.tot_cnt if self.tot_cnt > 0 else 0
        print(f"Cache slots: {self.cache_slots}, Cache hits: {self.cache_hit}, Hit ratio: {hit_ratio:.5f}")

if __name__ == "__main__":
        with open("C:\\Users\\USER\\structure-3\\Homework\\data\\linkbench.trc") as data_file:
            lines = data_file.readlines()
            for cache_slots in range(100, 1001, 100):
                cache_sim = LRUCacheSimulator(cache_slots)
                for line in lines:
                    page = line.strip().split()[0]
                    cache_sim.do_sim(page)
                
                cache_sim.print_stats()

