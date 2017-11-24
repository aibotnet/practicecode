#include <iostream>
#include <unordered_map> 
#include <utility> 

using namespace std; 

// List nodeclass 
class Node { 
	public: 
	int data; 
	Node* next; Node* prev; 
}; 

//Doubly Linked list 
class DLList { 
	public: 
	
	DLList() { 
		head = tail = NULL;  
		count = 0;
	} 
	
	~DLList() {} 
	
	Node* addNode(int val); 
	void print();
	void removeTail();
	void moveToHead(Node* node);
	
	int size() { return count; } 

	private: 
	Node* head; 
	Node* tail; 
	int count; 
};

// Function to add a node to the list 

Node* DLList::addNode(int val) {
	Node* temp = new Node(); 
	temp->data = val; 
	temp->next = NULL; 
	temp->prev = NULL; 
	
	if ( tail == NULL ) { 
		tail = temp; 
		head = temp; 
	} 
	else { 
		head->prev = temp; 
		temp->next = head; 
		head = temp; 
	}
	count++; 
	return temp; 
} 
	
void DLList::moveToHead(Node* node) { 
	if (head == node) return; 
		
	node->prev->next = node->next; 
	if (node->next != NULL){
		node->next->prev = node->prev; 
	} 
	else { 
		tail = node->prev; 
	} 
	node->next = head; 
	node->prev = NULL; 
	head->prev = node; 
	head = node; 
} 
	
void DLList::removeTail() { 
	count--; 		
	if (head == tail) { 
		delete head; 
		head = tail = NULL; 
	} 
	else{
		Node* del = tail;
		tail = del->prev; 
		tail->next = NULL; 
		delete del; 
	}
} 
	
void DLList::print(){
	Node* temp = head;
	int ctr = 0;		
	while ( (temp != NULL) && (ctr++ != 25) ) { 
		cout << temp->data << " "; 
		temp = temp->next; 
	} 
	cout << endl; 
}
	
class LRUCache { 
	public: 
		LRUCache(int aCacheSize); 
		void fetchPage(int pageNumber); 
		
	private: 
	    int cacheSize; 
		DLList dlist; 
		unordered_map< int, Node* > directAccess; 
}; 
	
LRUCache::LRUCache(int aCacheSize):cacheSize(aCacheSize) { } 
	
void LRUCache::fetchPage(int pageNumber) { 
	/* find the page in the map */
	unordered_map< int, Node* >::const_iterator it = directAccess.find(pageNumber); 
		
	/* if the page is found in the map */
	if (it != directAccess.end()) {   
		/* move the page on to the head of the doubly list */
		dlist.moveToHead( (Node*)it->second); 
	} 
	else { 
		/* if size of list is full */
		if (dlist.size() == cacheSize-1) 
		   dlist.removeTail(); 
			
		/* add the node to the head of doubly list */
		Node* node = dlist.addNode(pageNumber); 
		/* add the node in the map */
		directAccess.insert(pair< int, Node* >(pageNumber,node)); 
	}
		
	dlist.print(); 
}
	
int main() { 
	LRUCache lruCache(10); 
		
	lruCache.fetchPage(5); 
	lruCache.fetchPage(7); 
	lruCache.fetchPage(15); 
	lruCache.fetchPage(34); 
	lruCache.fetchPage(23); 
	lruCache.fetchPage(21); 
	lruCache.fetchPage(7); 
	lruCache.fetchPage(32); 
	lruCache.fetchPage(34); 
	lruCache.fetchPage(35); 
	lruCache.fetchPage(15); 
	lruCache.fetchPage(37); 
	lruCache.fetchPage(17); 
	lruCache.fetchPage(28); 
	lruCache.fetchPage(16); 
		
	return 0; 
}