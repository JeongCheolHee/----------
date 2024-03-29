#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

class ListNode {
public:
    int item;
    ListNode* next;

    ListNode(int item, ListNode* nextNode = nullptr) : item(item), next(nextNode) {}
};

class CircularLinkedList {
public:
    ListNode* tail;
    int numItems;

    CircularLinkedList() : tail(new ListNode(0)), numItems(0) {
        tail->next = tail;
    }

    ~CircularLinkedList() {
        clear();
        delete tail;
    }

    void insert(int i, int newItem) {
        if (i < 0 || i > numItems) {
            std::cerr << "Index out of bounds" << std::endl;
            return;
        }
        ListNode* newNode = new ListNode(newItem, nullptr);
        if (i == 0) {
            newNode->next = tail->next;
            tail->next = newNode;
            if (numItems == 0) tail = newNode;
        }
        else {
            ListNode* prev = getNode(i - 1);
            newNode->next = prev->next;
            prev->next = newNode;
            if (i == numItems) tail = newNode;
        }
        numItems++;
    }

    void append(int newItem) {
        insert(numItems, newItem);
    }

    int pop(int i) {
        if (numItems == 0) {
            std::cerr << "List is empty" << std::endl;
            return -1;
        }
        if (i < 0 || i >= numItems) {
            std::cerr << "Index out of bounds" << std::endl;
            return -1;
        }
        ListNode* prev = (i == 0) ? tail : getNode(i - 1);
        ListNode* toRemove = prev->next;
        int removedItem = toRemove->item;
        prev->next = toRemove->next;
        if (i == 0) tail->next = toRemove->next;
        if (i == numItems - 1) tail = prev;
        delete toRemove;
        numItems--;
        return removedItem;
    }

    ListNode* getNode(int i) {
        if (i < 0 || i >= numItems) return nullptr;
        ListNode* current = tail->next;
        for (int k = 0; k < i; ++k) {
            current = current->next;
        }
        return current;
    }

    void printList() {
        ListNode* current = tail->next;
        if (numItems == 0) {
            std::cout << "List is empty." << std::endl;
            return;
        }
        do {
            std::cout << current->item << " ";
            current = current->next;
        } while (current != tail->next);
        std::cout << std::endl;
    }

    void clear() {
        while (numItems > 0) {
            pop(0);
        }
    }
};

class LRUCacheSimulator {
public:
    int cache_slots;
    CircularLinkedList* cache;
    int cache_hit;
    int tot_cnt;

    LRUCacheSimulator(int slots) : cache_slots(slots), cache_hit(0), tot_cnt(0) {
        cache = new CircularLinkedList();
    }

    ~LRUCacheSimulator() {
        delete cache;
    }

    void do_sim(int page) {
        tot_cnt++;
        bool found = false;
        ListNode* current = cache->tail->next;
        int index = 0;

        for (int i = 0; current != cache->tail; current = current->next, ++i) {
            if (current->item == page) {
                found = true;
                index = i;
                break;
            }
        }

        if (found) {
            cache_hit++;
            cache->pop(index);
            cache->append(page);
        }
        else {
            if (cache->numItems >= cache_slots) {
                cache->pop(0);
            }
            cache->append(page);
        }
    }

    void print_stats() {
        double hit_ratio = (tot_cnt > 0) ? static_cast<double>(cache_hit) / tot_cnt : 0;
        std::cout << "Cache slots: " << cache_slots
            << ", Cache hits: " << cache_hit
            << ", Hit ratio: " << hit_ratio << std::endl;
    }
};

int main() {
    for (int cache_slots = 100; cache_slots <= 1000; cache_slots += 100) {
        LRUCacheSimulator cache_sim(cache_slots);

        std::ifstream data_file("C:\\Users\\USER\\source\\repos\\Project1\\linkbench.trc");  // 파일 경로를 확인하십시오.
        if (!data_file.is_open()) {
            std::cerr << "파일을 열 수 없습니다: linkbench.trc" << std::endl;
            return 1;
        }

        std::string line;
        while (std::getline(data_file, line)) {
            std::istringstream iss(line);
            int page;
            while (iss >> page) {
                cache_sim.do_sim(page);
            }
        }
        data_file.close();

        std::cout << "실험결과\n캐시 크기: " << cache_slots;
        cache_sim.print_stats();
    }
    return 0;
}
