#include <fstream>
#include <iostream>
using namespace std;
 
int main (){
   
   string data;

   ofstream outfile; // open a file in write mode.
   outfile.open("afile.dat");

   cout << "Writing to the file" << endl;
   cout << "Enter your name: "; 
   
   getline(cin,data);

   outfile << data << endl;// write inputted data into the file.

   cout << "Enter your age: "; 
   cin >> data;cin.ignore();
   
   outfile << data << endl; // again write inputted data into the file.

   outfile.close(); // close the opened file.

   ifstream infile; // open a file in read mode. 
   infile.open("afile.dat"); 
 
   cout << "Reading from the file" << endl; 
   getline(infile,data); 

   cout << data << endl; // write the data at the screen.
   
   infile >> data; // again read the data from the file and display it.
   cout << data << endl; 

   infile.close();// close the opened file.

   return 0;
}