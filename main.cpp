#include <iostream>
#include <ctime>
#include <cstdlib>
#define pass (void)0
// I cloned and commented

using namespace std;

void Math_Game();
void Power_Ball(int Balls[]);
int rand_array();

int main()
{
    char play = 'Y';
    while (play == 'Y' or play == 'y')
    {
        char choice;
        cout << "What game would you like to play? "
        << "\n M for Math Game \n P for Power Ball " << endl;
        cin >> choice; // gets user choicee

        if (choice == 'M' or choice == 'm')
            Math_Game(); // calls math game


        if (choice == 'P' or choice == 'p')
        {
            unsigned seed =  time(0);
            srand(seed);

            int Balls [5];  // 5 rand nums
            for (int x = 0; x < 5; x++)
            Balls[x] = (rand() % (50 - 1 + 1)) + 1; // creates random number list

            Power_Ball(Balls);
        }

        cout << "Game Over" << endl << endl;
        cout << "Would you like to play again?  \n Y for yes \n N for no" << endl;
        cin >> play;
    }
    return 0;
}


void Math_Game()
{
    int sum = 0, userInput, tries = 0;
    int math_num[3];// 3 random nums in array

    for (int x = 0; x < 3; x++)
    {
        math_num[x] = (rand() % (50 - 1 + 1)) + 1; // gets random numbers
        cout << math_num[x] << endl; // shows user the number
        sum += math_num[x]; // calculates sum
    }

    do {
        cout << "What is the sum of the numbers? " << endl;
        cin >> userInput;
        tries++;
    }while (userInput != sum and tries < 3);

    if (userInput == sum)
        cout << "You got it right!" << endl;
    if (tries >= 3)
        cout << "Sorry you ran out of tries. The correct answer is " << sum << "." << endl;
}

void Power_Ball(int Balls[])
{
    int match = 0, userguess;   // sets variables
    string winning;             // sets variables

    for (int x = 0; x<5; x++)
        cout << Balls[x] << endl;


    for (int x = 0; x<5; x++) // user enters guess
    {
        cout << "enter a guess from 1 to 50: " << endl; // asks for guess
        cin >> userguess; // gets user input
        for (int x = 0; x<5; x++)
            if (userguess == Balls[x]) //check guess
            {
                match = match + 1; // add to match if guess is correct
                cout << "is match" << endl;
                break;
            }
            else if (userguess != Balls[x])
                cout << "not match" << endl;

    }
    // sets winnings according to how many numbers matched
    if (match == 0)
        winning = "0";
    if (match == 1)
        winning = "50,000";
    if (match == 2)
        winning = "200,000";
    if (match == 3)
        winning = "400,00";
    if (match == 4)
        winning = "700,000";
    if (match == 5)
        winning = "1,000,000";

    cout << "The winning numbers were " << endl;
    for (int x = 0; x < 5; x++)
        cout << Balls[x] << " " << endl; // shows winning numbers

    cout << "You got " << match << " matches." << endl;
    cout << "You won " << winning << " dollars." << endl;
}





