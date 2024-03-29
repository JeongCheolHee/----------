# LRU Homework

class CacheSimulator:
    def __init__(self, cache_slots):
        self.cache_slots = cache_slots #cache 크기
        self.cache_hit = 0 # 캐쉬 히트 수 추적,
        self.tot_cnt = 0 # 접근한 총 요청 수
        self.cache = []


    def do_sim(self, page):
        self.tot_cnt += 1  # 요청 수 증가
        if page in self.cache:
            # 캐시 히트: 페이지를 MRU (Most Recently Used) 위치로 이동
            self.cache_hit += 1
            self.cache.remove(page)
            self.cache.append(page)
        else:
            # 캐시 미스: 캐시가 꽉 찼다면, 가장 오래된 페이지 (LRU - Least Recently Used) 제거
            if len(self.cache) == self.cache_slots:
                self.cache.pop(0)  # 가장 오래된 페이지 제거
            self.cache.append(page)  # 새 페이지를 캐시에 추가

        
    def print_stats(self):
        print("cache_slot = ", self.cache_slots, "cache_hit = ", self.cache_hit, "hit ratio = ", self.cache_hit / self.tot_cnt)


if __name__ == "__main__":

    data_file = open("C:\\Users\\USER\\structure-3\\Homework\\data\\linkbench.trc")
    lines = data_file.readlines()
    for cache_slots in range(100, 1001, 100):
        cache_sim = CacheSimulator(cache_slots)
        for line in lines:
            page = line.split()[0]
            cache_sim.do_sim(page)
        
        cache_sim.print_stats()