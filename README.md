# Data Structures & Systems Design Assignment

**Author:** Anmol Mishra  
**Contact:** anmolmishra2005b@gmail.com  

## Overview
Optimal Python implementations for an LRU Cache and an Event Scheduler.

---

## Architectural Logic

### 1. LRU Cache
* **Hash Map (`dict`):** Ensures instant $O(1)$ key lookups.
* **Doubly Linked List:** Ensures $O(1)$ pointer updates. Dummy `left` (LRU) and `right` (MRU) nodes eliminate edge cases, allowing nodes to be unlinked and moved to the tail without a linear scan.

### 2. Event Scheduler
* **`can_attend_all`**: Sorts events by start time and makes a single linear pass ($O(N \log N)$ time) to detect any overlapping intervals.
* **`min_rooms_required`**: Uses a two-pointer line-sweep approach. Segregates and sorts all start and end times to track active simultaneous meetings over a unified timeline.

---

## Complexity & Trade-offs

### Performance Matrix

| Function | Time Complexity | Space Complexity |
| :--- | :--- | :--- |
| `LRUCache.get()` | $O(1)$ | $O(1)$ ($O(K)$ class capacity) |
| `LRUCache.put()` | $O(1)$ | $O(1)$ ($O(K)$ class capacity) |
| `can_attend_all()` | $O(N \log N)$ | $O(1)$ |
| `min_rooms_required()` | $O(N \log N)$ | $O(N)$ (for split timestamp arrays) |

### Why Hash Map + Doubly Linked List?
* **Arrays** maintain chronological order but require slow $O(N)$ scans and index shifting to remove items from the middle.
* **Hash Maps** offer instant $O(1)$ access but completely lack any concept of temporal sequence.

**Fusing them** creates a perfect balance: the linked list maintains the eviction order, while the hash map provides immediate memory pointers to eliminate search bottlenecks.
