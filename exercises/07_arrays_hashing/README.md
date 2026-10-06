# 07 Arrays & Hashing (NeetCode)

### The Core Mental Model: Time vs Space Trade-off
Brute force algorithms check all pairs or subsets: $O(n^2)$.
By trading space ($O(n)$ hash map or hash set), we can answer queries ("have I seen target - x?") in $O(1)$ average time.

### Hash Tables from Scratch
A hash table is an array of buckets. A hash function `hash(key) % capacity` maps a key to a bucket index. Collisions are handled via **separate chaining** (linked list or array at each bucket). When load factor `size / capacity > 0.75`, we double the bucket array and rehash all keys.
