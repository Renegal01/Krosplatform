#include <iostream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>

using namespace std;
int flag = 1;
// Function declarations
void instructions();
void ball_input(int J, double V[], double B[], double B1[], double P1);
void simulate_ball(int J, int Q, double V[], double B[], double B1[], double D[], double X[], double Y[],
    double A, double& S1, double& S2, double P1);
void collision_with_ball(int J, int K, double V[], double B[], double& S1, double& S2, double& S5, double& S6,
    double X[], double Y[], double P1);
void collision_with_jack(int J, int K, double V[], double B[], double& S1, double& S2, double& S5, double& S6,
    double P1);
void report_positions(int Q, double D[], double X[], double Y[]);

int main() {
    // Print the title
    cout << setw(30) << "BOCCE" << endl;
    cout << setw(37) << "CREATIVE COMPUTING" << endl;
    cout << setw(39) << "MORRISTOWN NEW JERSEY" << endl;
    cout << endl << endl << endl;

    int Q = 5;
    cout << "THIS GAME SIMULATES THE GAME OF LAWN BOWLS" << endl;

    string Z;
    cout << "DO YOU NEED INSTRUCTIONS? ENTER YES OR NO? ";
    cin >> Z;

    if (Z == "YES" || Z == "yes") {
        instructions();
    }
    else
        cout << endl;

    // Initialize random seed
    srand(time(0));

    string YS;
    do {
        double B[10] = { 0 }, B1[10] = { 0 }, D[10] = { 0 }, V[10] = { 0 }, X[10] = { 0 }, Y[10] = { 0 };
        double P1 = 3.14159;
        double S1 = 0, S2 = 0, A = -49.3;
        double D1 = 0;

        // Random placement of the jack
        X[1] = int(2000 + 700 * ((double)rand() / RAND_MAX));
        Y[1] = int(200 - 400 * ((double)rand() / RAND_MAX));

        cout << "THE JACK IS LOCATED AT " << X[1] << " " << Y[1] << endl;

        // Now, loop for each ball
        for (int P = 2; P <= Q; ++P) {
            int J = P;
            ball_input(J, V, B, B1, P1);
            simulate_ball(J, Q, V, B, B1, D, X, Y, A, S1, S2, P1);
        }

        // Now, sum the distances
        D1 = 0;
        for (int J = 2; J <= Q; ++J) {
            D1 += D[J];
        }

        cout << endl << "THE TOTAL DISTANCE OF ALL BALLS FROM THE JACK IS " << D1 << " CM" << endl;

        if (D1 < Q * Q) {
            cout << "MAGNIFICENT BOWLING! WHAT AN EYE!!" << endl;
        }
        else if (D1 < 2 * Q * Q) {
            cout << "EXCELLENT BUT COULD BE BETTER:" << endl;
        }
        else if (D1 < 3 * Q * Q) {
            cout << "GOOD BUT NEEDS SOME IMPROVEMENT" << endl;
        }
        else if (D1 < 6 * Q * Q) {
            cout << "FAIR - YOU NEED MORE PRACTICE" << endl;
        }
        else if (D1 < 10 * Q * Q) {
            cout << "POOR - TRY TO BE MORE CONSISTENT" << endl;
        }
        else if (D1 < 20 * Q * Q) {
            cout << "YOUR GAME NEEDS LOTS OF WORK" << endl;
        }
        else {
            cout << "DON'T PLAY THIS GAME FOR MONEY!!" << endl;
        }

        cout << endl << "CARE TO TRY AGAIN? ENTER YES OR NO ";
        cin >> YS;
        cout << endl;

    } while (YS == "YES" || YS == "yes");

    return 0;
}

void instructions() {
    cout <<endl << "IN THIS GAME YOU ROLL " << 4 << " BALLS SUCCESSIVELY AT A TARGET" << endl;
    cout << "BALL (CALLED A JACK). THE OBJECT IS TO GET THE BALLS AS CLOSE" << endl;
    cout << "TO THE JACK AS POSSIBLE. THE BALLS ARE 10 CM IN DIAMETER AND" << endl;
    cout << "ARE WEIGHTED SO THAT THEY ROLL IN A CURVE. YOU WILL HAVE TO" << endl;
    cout << "ROLL THEM AT AN ANGLE TO THE LINE FROM YOU AT COORDINATES 0,0" << endl;
    cout << "TO THE JACK AT COORDINATES X,Y. A POSITIVE ANGLE WILL MAKE" << endl;
    cout << "THE BALL CURVE CLOCKWISE. A NEGATIVE ANGLE WILL MAKE IT CURVE" << endl;
    cout << "ANTI-CLOCKWISE. THE JACK IS A 4 CM WIDE AND WILL ROLL" << endl;
    cout << "STRAIGHT IF YOU HIT IT. BALLS HIT BY YOUR THROWN BALL MAY" << endl;
    cout << "CURVE IN EITHER DIRECTION." << endl;
    cout << endl << "HINT. TRY AN INITIAL VELOCITY OF 500 AND AN ANGLE OF 10" << endl;
    cout << endl << endl;
}

void ball_input(int J, double V[], double B[], double B1[], double P1) {
    cout << "BALL " << (J - 1) << endl;
    cout << "VELOCITY? ";
    cin >> V[J];
    V[J] = abs(V[J]);
    while (V[J] > 1000) {
        cout << "VELOCITY TOO HIGH" << endl;
        cout << "VELOCITY ";
        cin >> V[J];
        V[J] = abs(V[J]);
    }
    cout << "ANGLE ";
    cin >> B1[J];
    while (abs(B1[J]) > 89) {
        cout << "ANGLE TOO BIG" << endl;
        cout << "ANGLE ";
        cin >> B1[J];
    }
    cout << endl;
    B[J] = abs(B1[J] * P1 / 180);
}

void simulate_ball(int J, int Q, double V[], double B[], double B1[], double D[], double X[], double Y[],
    double A, double& S1, double& S2, double P1) {
    double K1 = -20;
    if (J == 1)
        K1 = 0;

    while (true) {
        double A1 = A * cos(B[J]) + K1 * cos((P1 / 2) + B[J]);
        double A2 = A * sin(B[J]) + K1 * sin((P1 / 2) + B[J]);

        double S3 = V[J] * B[J] * 0.05 + 1.25E-03 * A1;
        double S4 = V[J] * B[J] * 0.05 + 1.25E-03 * A2;

        B[J] = atan((V[J] * B[J] + A2 * 0.05) / (V[J] * B[J] + A1 * 0.05));

        if (B1[J] < 0)
            S4 = -S4;

        double S5 = S1 + S3;
        double S6 = S2 + S4;

        if (J != 1) {
            if (abs(S5 - X[1]) < 7 && abs(S6 - Y[1]) < 7) {
                int K = 1;
                collision_with_jack(J, K, V, B, S1, S2, S5, S6, P1);
            }
        }

        for (int K = 2; K <= Q; ++K) {
            if (K == J || X[K] == 0)
                continue;
            if (abs(S5 - X[K]) < 10 && abs(S6 - Y[K]) < 10) {
                collision_with_ball(J, K, V, B, S1, S2, S5, S6, X, Y, P1);
            }
        }

        if (V[J] < abs(A * 0.05)) {
            // Line 1440
            X[J] = X[J] + S5;
            Y[J] = Y[J] + S6;
            S1 = 0;
            S2 = 0;
            S5 = 0;
            S6 = 0;
            bool found = false;
            for (int L = 1; L <= Q; ++L) {
                if (V[L] > abs(A * 0.05)) {
                    J = L;
                    found = true;
                    break;
                }
                B[L] = 0;
                V[L] = 0;
            }
            if (found) {
                K1 = -20;
                if (J == 1)
                    K1 = 0;
                continue;
            }
            else {
                report_positions(Q, D, X, Y);
                break;
            }
        }
        else {
            V[J] = V[J] + (A * 0.05);
            S1 = S5;
            S2 = S6;
            // Go back to start of loop
            continue;
        }
    }
}

void collision_with_ball(int J, int K, double V[], double B[], double& S1, double& S2, double& S5, double& S6,
    double X[], double Y[], double P1) {
    B[K] = atan((Y[K] - S2) / (X[K] - S1));
    cout << '\a'; // Beep sound
    if (J == 1)
        V[J] = V[J] / 5;
    V[J] = abs(V[J] * (B[J] - B[K]));
    V[K] = abs(V[J] * (B[J] - B[K]));
    B[J] = (P1 / 2) + B[K];
    S5 = S1;
    S6 = S2;
    if (K == 1)
        V[K] = 5 * V[K];
}

void collision_with_jack(int J, int K, double V[], double B[], double& S1, double& S2, double& S5, double& S6,
    double P1) {
    if (J == 1)
        V[J] = 5 * V[J];
}

void report_positions(int Q, double D[], double X[], double Y[]) {
    cout << "JACK AT COORDINATES " << X[1] << " " << Y[1] << endl;
    flag++;
    for (int M = 2; M <= flag; ++M) {
        double D_value = sqrt(pow(Y[1] - Y[M], 2) + pow(X[1] - X[M], 2)) - 7;
        D[M] = D_value;
        if (D_value < 0)
            D[M] = 0;
        cout << "BALL " << (M - 1) << " AT COORDINATES " << X[M] << " " << Y[M] << " IT IS " << D[M]
            << " FROM THE JACK" << endl;
        if (M == flag)
        {
            if (D[M] < 10) {
                cout << endl << setw(15) << "EXCELLENT SHOT! " << endl;
            }
            else if (D[M] < 20) {
                cout << endl << setw(15) << "GOOD SHOOTING! " << endl;
            }
            else if (D[M] < 30) {
                cout << endl << setw(15) << "NICE TRY !" << endl;
            }
            else if (D[M] > 500) {
                cout << endl << setw(5) << "YECH! OVER " << int(D[M] / 30.48) << " FEET AWAY!" << endl;
            }
            if (X[M] > X[1])
                cout << "LONG AND ";
            if (X[M] < X[1])
                cout << "SHORT AND ";
            if (Y[M] > Y[1])
                cout << "TO THE LEFT ";
            if (Y[M] < Y[1])
                cout << "TO THE RIGHT";
            cout << endl;
        }
    }
    cout << endl;
}
