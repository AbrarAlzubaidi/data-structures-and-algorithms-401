# Hashtables
Hashtables are a data structure that utilize key value pairs. This means every Node or Bucket has both a key, and a value.

**specifications:**
- deterministic: 
input determine the output

- not random: 
same key will produce the same hash
## Challenge
The basic idea of a hashtable is the ability to store the key into this data structure, and quickly retrieve the value. This is done through what we call a **hash**. A **hash** is the ability to encode the key that will eventually map to a specific location in the data structure that we can look at directly to retrieve the value.

## Approach & Efficiency
- hash: 
   - time: O(n) n: number of characters inside a key
   - space: O(1)
- get: 
    - no collesion --> 
        - time: O(n) 
        - space: O(1)
    - collesion --> 
        - time: O(n*m) which n: number of elements inside array, m number of elements inside linkedlist 
        - space: O(1)
- add: 
   - time: O(1)
   - space: O(1)
- contain: 
   - no collesion --> 
     - time: O(n) 
     - space: O(1)
   - collesion --> 
     - time: O(n*m) which n: number of elements inside array, m number of elements inside linkedlist 
     - space: O(1)

## API
- hash: 
to produce for each key a memeort location
`return memory location`
- get: 
to get the value for certain key
`return value`
- add: 
to add a value for a key into a memeory location
- contain: 
to check if a certain key is exist in table or not
`return true/false`
