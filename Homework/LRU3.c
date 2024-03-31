#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct ListNode {
    char item[50];
    struct ListNode *next;
} ListNode;

typedef struct {
    ListNode *tail;
    int numItems;
} CircularLinkedList;

void initList(CircularLinkedList *list);
void append(CircularLinkedList *list, char *newItem);
int removeItem(CircularLinkedList *list, char *item);
int size(CircularLinkedList *list);
ListNode* getNode(CircularLinkedList *list, int i);
void clearList(CircularLinkedList *list);
int contains(CircularLinkedList *list, char *item);

void initList(CircularLinkedList *list) {
    list->tail = NULL;
    list->numItems = 0;
}

void append(CircularLinkedList *list, char *newItem) {
    ListNode *newNode = malloc(sizeof(ListNode));
    strcpy(newNode->item, newItem);
    if (list->numItems == 0) {
        newNode->next = newNode;
        list->tail = newNode;
    } else {
        newNode->next = list->tail->next;
        list->tail->next = newNode;
        list->tail = newNode;
    }
    list->numItems++;
}

int removeItem(CircularLinkedList *list, char *item) {
    if (list->numItems == 0) return 0;
    ListNode *current = list->tail->next;
    ListNode *prev = list->tail;
    do {
        if (strcmp(current->item, item) == 0) {
            if (current == prev) {
                list->tail = NULL;
            } else {
                prev->next = current->next;
                if (current == list->tail) {
                    list->tail = prev;
                }
            }
            free(current);
            list->numItems--;
            return 1;
        }
        prev = current;
        current = current->next;
    } while (current != list->tail->next);
    return 0;
}

int size(CircularLinkedList *list) {
    return list->numItems;
}

ListNode* getNode(CircularLinkedList *list, int i) {
    if (i < 0 || i >= list->numItems) {
        return NULL;
    }
    ListNode *current = list->tail->next;
    for (int index = 0; index < i; index++) {
        current = current->next;
    }
    return current;
}

void clearList(CircularLinkedList *list) {
    while (list->numItems > 0) {
        ListNode *temp = list->tail->next;
        if (list->tail == temp) {
            list->tail = NULL;
        } else {
            list->tail->next = temp->next;
        }
        free(temp);
        list->numItems--;
    }
}

int contains(CircularLinkedList *list, char *item) {
    if (list->numItems == 0) return 0;
    ListNode *current = list->tail->next;
    do {
        if (strcmp(current->item, item) == 0) {
            return 1;
        }
        current = current->next;
    } while (current != list->tail->next);
    return 0;
}

typedef struct {
    CircularLinkedList cache;
    int cache_slots;
    int cache_hit;
    int tot_cnt;
} CacheSimulator;

void initCacheSimulator(CacheSimulator *sim, int slots) {
    initList(&sim->cache);
    sim->cache_slots = slots;
    sim->cache_hit = 0;
    sim->tot_cnt = 0;
}

void do_sim(CacheSimulator *sim, char *page) {
    if (contains(&sim->cache, page)) {
        sim->cache_hit++;
        removeItem(&sim->cache, page);
    } else if (size(&sim->cache) == sim->cache_slots) {
        ListNode *nodeToRemove = getNode(&sim->cache, 0);
        if (nodeToRemove != NULL) {
            removeItem(&sim->cache, nodeToRemove->item);
        }
    }
    append(&sim->cache, page);
    sim->tot_cnt++;
}

void print_stats(CacheSimulator *sim) {
    printf("cache_slot = %d cache_hit = %d hit ratio = %f\n", sim->cache_slots, sim->cache_hit, (double)sim->cache_hit / sim->tot_cnt);
}

int main(void) {
    FILE *data_file = fopen("C:/Users/USER/source/repos/Project1/linkbench.trc", "r");
    char line[1024];
    if (!data_file) {
        perror("File opening failed");
        return EXIT_FAILURE;
    }

    for (int cache_slots = 100; cache_slots <= 1000; cache_slots += 100) {
        CacheSimulator cache_sim;
        initCacheSimulator(&cache_sim, cache_slots);
        while (fgets(line, sizeof(line), data_file)) {
            char *page = strtok(line, " \n");
            do_sim(&cache_sim, page);
        }
        print_stats(&cache_sim);
        fseek(data_file, 0, SEEK_SET);
        clearList(&cache_sim.cache);
    }
    fclose(data_file);
    return 0;
}
