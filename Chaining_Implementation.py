#creating the hash table with nested list
HashTable = [[]for _ in range(10)]
#Hashing function to return value for every key
def Hashing(key):
    return key%len(HashTable)

#display values
def display_hash(hashTable):
      
    for i in range(len(hashTable)):
        print(i, end = " ")
          
        for j in hashTable[i]:
            print("-->", end = " ")
            print(j, end = " ")
              
        print()
#search values
def search_hash(hashTable, key):
    for i in range(len(hashTable)):
        for j in hashTable[i]:
            if j==key:
                return True
    return False
#Insert values
def insert(HashTable,key):
    if search_hash(HashTable,key)==False :
        hash_key=Hashing(key);
        HashTable[hash_key].append(key);
#Remove values
def remove(HashTable, key) :
    hash_key=Hashing(key);
    HashTable[hash_key].remove(key);
    

# Driver Code
insert(HashTable, 10)
insert(HashTable, 25)
insert(HashTable, 20)
insert(HashTable, 9)
insert(HashTable, 21)
insert(HashTable, 21)
remove(HashTable,9)
if search_hash(HashTable,9):
    print("10 availiable")
  
display_hash (HashTable)