import sys
sys.path.append('c:\\Users\\USER\\structure-3') 
from Heap.src.minHeap import MinHeap

# 캐시 항목을 포함하는 클래스 필요, 여기에는 lpn과 frequency가 포함
class CacheEntry:
    def __init__(self, lpn, frequency):
        self.lpn = lpn
        self.frequency = frequency

    # MinHeap 삽입/정렬을 위한 작은 연산자 구현
    def __lt__(self, other):
        return self.frequency < other.frequency

# lfu_sim 함수 내에서 이 클래스를 사용
def lfu_sim(cache_slots):
    cache_hit = 0  # 캐시 히트 횟수
    tot_cnt = 0    # 전체 요청 횟수
    cache = {}     # CacheEntry 객체를 저장
    frequency_dict = {} # 모든 lpn의 빈도를 추적, 캐시에 있는 것만 아님
    heap = MinHeap()    # MinHeap 인스턴스

    # 데이터 파일 열기
    data_file = open("C:/Users/USER/structure-3/Homework/data/linkbench2.trc")

    for line in data_file.readlines():
        lpn = line.split()[0]
        tot_cnt += 1

        # 빈도 업데이트
        if lpn in frequency_dict:
            frequency_dict[lpn] += 1
        else:
            frequency_dict[lpn] = 1

        # 캐시에 있다면, 히트
        if lpn in cache:
            cache_hit += 1
            # 캐시 항목 업데이트 및 힙 속성 유지를 위해 아래로 퍼지기
        else:
            # 캐시가 가득 찼다면, 가장 자주 사용되지 않는 항목 제거
            if len(cache) >= cache_slots:
                removed = heap.deleteMin()
                del cache[removed.lpn]
            # 캐시 및 힙에 새 lpn 삽입
            entry = CacheEntry(lpn, frequency_dict[lpn])
            cache[lpn] = entry
            heap.insert(entry)

    data_file.close()
    # 이 시뮬레이션의 히트 비율을 반환
    return cache_hit / tot_cnt

if __name__ == "__main__":
    for cache_slots in range(100, 1000, 100):
        hit_ratio = lfu_sim(cache_slots)
        print("cache_slot =", cache_slots, "cache_hit = ", int(hit_ratio*100000) ,"hit ratio =", hit_ratio)
