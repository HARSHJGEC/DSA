#creating the hash table with nested list
HashTable = [[]for _ in range(10)]
#Hashing function to return value for every key
def Hashing(key):
    return key%len(HashTable)
#Insert values
def insert(HashTable,key):
    hash_key=Hashing(key);
    HashTable[hash_key].append(key);
#display values
def display_hash(hashTable):
      
    for i in range(len(hashTable)):
        print(i, end = " ")
          
        for j in hashTable[i]:
            print("-->", end = " ")
            print(j, end = " ")
              
        print()
# Driver code
# Driver Code
insert(HashTable, 10)
insert(HashTable, 25)
insert(HashTable, 20)
insert(HashTable, 9)
insert(HashTable, 21)
insert(HashTable, 21)
  
display_hash (HashTable)