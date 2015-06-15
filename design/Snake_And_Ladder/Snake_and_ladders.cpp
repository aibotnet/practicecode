#include<iostream>
#include<stdlib.h>
#include<string.h>
#include<time.h>
#include<vector>
#include<stdio.h>

using namespace std;

class Board
{
	private:
		int score;
	public:
		Board()
		{
			
		}
		
	void print_board()
	{
  		cout<<"\n\n";
  		draw_line(50,'-');
  		cout<<"\n\t\tSNAKE AT POSITION\n";
  		draw_line(50,'-');
  		cout<<"\n\tFrom 98 to 28 \n\tFrom 95 to 24\n\tFrom 92 to 51\n\tFrom 83 to 19\n\tFrom 73 to  1\n\tFrom 69 to 33\n\tFrom 64 to 36\n\tFrom 59 to 17\n\tFrom 55 to  7\n\tFrom 52 to 11\n\tFrom 48 to  9\n\tFrom 46 to  5\n\tFrom 44 to 22\n\n";
 		draw_line(50,'-');
 		cout<<"\n\t\t LADDER AT POSITION\n";
  		draw_line(50,'-');
  		cout<<"\n\tFrom  8 to 26\n\tFrom 21 to 82\n\tFrom 43 to 77\n\tFrom 50 to 91\n\tFrom 62 to 96\n\tFrom 66 to 87\n\tFrom 80 to 100\n";
  		draw_line(50,'-');
  		cout<<endl;
	}
	
	void draw_line(int n,char ch)
	{
		for(int i=0;i<n;i++)
   		cout<<ch;
	}
	
	
};


class Player
{
		 string name;
	     int score;
	public:

	     
		 Player(string name,int score)
		 {
		 	this->name=name;
		 	this->score=score;
		 }
		 
		 string get_name()
		 {
		 	return name;
		 }
		 
		 int get_score()
		 {
		 	return score;
		 }
		 
		 void scored(int score)
		 {
		 	this->score=score;
		 }
		 
};

class game
{
	
		int n;
		vector<Player*> v;
		
	public:
		
		game(int n)
		{
			this->n=n;
		}
		
		void start()
		{
			for(int i=0;i<n;i++)
			{
				string temp_name;
				cin>>temp_name;
				Player *p=new Player(temp_name,0);
				v.push_back(p);
			}
			
			vector<Player*>::iterator it;
			play_game();
			  
		}
		
		void play_game()
		{
			
			Board b;
			
			while(1)
			{
				b.print_board();
				gamescore();  		
				vector<Player*>::iterator it;
  				int win_flag=0;
  				
  				for(it=v.begin();it!=v.end();it++)
  				{
  					cout<<"\n\n--->" <<(*it)->get_name()<<" Now your Turn, Press any key to play ";
  					getchar();
  					int lastposition=(*it)->get_score();
  					(*it)->scored(play_dice(lastposition));
					
					if((*it)->get_score()<lastposition)
       					cout<<"\n Oops!! Snake found !! You are at postion "<<(*it)->get_name()<<"\n";

   					else if((*it)->get_score()>lastposition+6)
       					cout<<"\nGreat!! you got a ladder !! You are at position "<<(*it)->get_name();
       					
       				if((*it)->get_score()>=100)
       				{
       					gamescore();  
       					cout<<endl<<(*it)->get_name()<<" !! You are the winner of the game\n\n";
       					win_flag=1;
       					break;
					}
       				
				}
				
				if(win_flag==1)
				{
					break;
				}
			}
		}
		
		void gamescore()
		{
  			cout<<"\n";
  			cout<<"\n\t\tGAME STATUS\n";
  			
  			vector<Player*>::iterator it;
  			
  			for(it=v.begin();it!=v.end();it++)
  			{
  	
  				
  				cout<<"\n\t--->"<<(*it)->get_name()<<" is at position "<<(*it)->get_score()<<endl;

			}
  			
		}		
		
		int play_dice(int score)
		{
 			int dice;
  			dice = (rand() % 6)+1;
  			cout<<"\nYou got "<<dice<<" Point !! ";
  			score=score+dice;  cout<<"Now you are at position "<<score;
  			switch(score)
  			{
  					case 98 :score=28;break;
 			 		case 95 :score=24;break;
   					case 92 :score=51;break;
   					case 83 :score=19;break;
   					case 73 :score=1;break;
   					case 69 :score=33;break;
   					case 64 :score=36;break;
   					case 59 :score=17;break;
   					case 55 :score=7;break;
   					case 52 :score=11;break;
   					case 48 :score=9;break;
   					case 46 :score=5;break;
   					case 44 :score=22;break;
   					case 8  :score=26;break;
   					case 21 :score=82;break;
   					case 43 :score=77;break;
   					case 50 :score=91;break;
   					case 54 :score=93;break;
   					case 62 :score=96;break;
   					case 66 :score=87;break;
   					case 80 :score=100;

 			 }
 		 return score;
		}
		
		void draw_line(int n,char ch)
		{
			for(int i=0;i<n;i++)
   			cout<<ch;
		}
};




int main()
{
	
	cout<<"Enter the number of players: ";
	int n;cin>>n;
	game g(n);
	g.start();
	
	return 0;
}
