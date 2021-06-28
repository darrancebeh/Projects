#include <iostream>
#include <ctime>

using namespace std;

int main()
{
    string option;
    int totalgames = 0;
    int totalattempts = 0;
    int history[totalgames + 1];
    do{
        int key, guess(0), attempts(1);
        totalgames++;
        srand(time(0));
        key = rand()% 100 + 1;
        
        cout << string(50, '\n');
        cout << "Random number generated, (0 - 100). Good luck!" << endl;

        cout << "ATTEMPT #" << attempts << endl;
        cin >> guess;
        if(guess != key)
        {
            attempts++;
        }
        
        do {
            cout << "\n";
            cout << "ATTEMPT #" << attempts << endl;
            if(key > guess)
            {
                cout << "The lucky number is LARGER than your guess.";
                attempts++;
            } else if(key < guess)
            {
                cout << "The lucky number is SMALLER than your guess.";
                attempts++;
            }

            cout << "\n";
            cin >> guess;

        } while(guess != key);

        cout << "_________________________________________________\n" << endl;
        cout << "\nCongratulations! The lucky number was " << key << "." <<  endl;
        cout << "Number of attempts: " << attempts << "." << endl;
        totalattempts += attempts;
        string flag;

        cout << "\nInput any key to navigate to stats screen." << endl;
        cin >> flag;

        cout << string(50, '\n');
        cout << "YOUR STATISTICS" << endl;
        cout << "_________________________________________________\n" << endl;
        cout << "TOTAL GAMES: " << totalgames << endl;
        cout << "TOTAL ATTEMPTS: " << totalattempts << endl;
        cout << "AVERAGE ATTEMPTS PER GAME: " << totalattempts/totalgames << endl;
        cout << "_________________________________________________" << endl;
        cout << "Would you like to play again? (Y/N)" << endl;
        cin >> option;

        history[totalgames] = attempts;
    } while (option[0] == 'Y' || option[0] == 'y');

    cout << string(50, '\n');
    cout << "Thanks for playing darrance's Random Number Guesser game!" << endl;
    string flag;
    cout << "Input any key to exit the program." << endl;
    cin >> flag;

    return 0;
}
