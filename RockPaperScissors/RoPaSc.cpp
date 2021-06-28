#include <iostream>
#include <ctime>

using namespace std;

int main()
{
    string option;
    int totalgames = 0;
    int totalwins = 0;
    int totallosses = 0;
    int totalties = 0;
    int history[totalgames - 1];

    do {
        totalgames++;
        int result;
        int computer;
        string player;
        int playerInt;
        srand(time(0));
        computer = rand()%2;

        cout << string(50, '\n');
        cout << "Rock, Paper or Scissors?" << endl;
        cin >> player;

        if(player[0] == 'R' || player[0] == 'r'){
            playerInt = 0;
        } else if(player[0] == 'P' || player[0] == 'p'){
            playerInt = 1;
        } else if(player[0] == 'S' || player[0] == 's'){
            playerInt = 2;
        }

        string intToOption[3] = {
            "Rock",
            "Paper",
            "Scissors"
        };

        string playerChoice = intToOption[playerInt];
        string computerChoice = intToOption[computer];

        if(computer == playerInt){
            result = 0;
        } else if(computer == 0 and playerInt == 1){
            result = 1;
        } else if(computer == 1 and playerInt == 2){
            result = 1;
        } else if(computer == 2 and playerInt == 0){
            result = 1;
        } else if(computer == 0 and playerInt == 2){
            result = 2;
        } else if(computer == 1 and playerInt == 0){
            result = 2;
        } else if(computer == 2 and playerInt == 1){
            result = 2;
        }

        if(result == 0){
            cout << "It's a tie! Both of you chose " << playerChoice << ".";
            totalties++;
        } else if(result == 1){
            cout << "Player Win! Player chose " << playerChoice << " while Computer chose " << computerChoice << ". " << playerChoice + " beats " << computerChoice << ".";
            totalwins++;
        } else if(result == 2){
            cout << "Computer Win! Player chose " << playerChoice << " while Computer chose " << computerChoice << ". " << computerChoice << " beats " << playerChoice << ".";
            totallosses++;
        }

        string flag;

        cout << "\nInput any key to navigate to stats screen." << endl;
        cin >> flag;

        cout << string(50, '\n');
        cout << "YOUR STATISTICS" << endl;
        cout << "_________________________________________________\n" << endl;
        cout << "TOTAL GAMES: " << totalgames << endl;
        cout << "WINS: " << totalwins << endl;
        cout << "LOSSES: " << totallosses << endl;
        cout << "TIES: " << totalties << endl;
        cout << "_________________________________________________" << endl;
        cout << "Would you like to play again? (Y/N)" << endl;
        cin >> option;

    } while (option[0] == 'Y' || option[0] == 'y');

    cout << string(50, '\n');
    cout << "Thanks for playing my Rock, Paper, Scissors game!" << endl;
    string flag;
    cout << "Input any key to exit the program." << endl;
    cin >> flag;

    return 0;
}
