import random
import math

# 10 PRINT TAB(25);"BOCCE"
# 20 PRINT TAB(19);"CREATIVE COMPUTING"
# 30 PRINT TAB(17);"MORRISTOWN NEW JERSEY"
# 40 PRINT:PRINT:PRINT
print(" " * 25 + "BOCCE")
print(" " * 19 + "CREATIVE COMPUTING")
print(" " * 17 + "MORRISTOWN NEW JERSEY")
print("\n\n")

while True:
    # 1000 Q=5
    Q = 5

    # 1010 PRINT "THIS GAME SIMULATES THE GAME OF LAWN BOWLS"
    print("THIS GAME SIMULATES THE GAME OF LAWN BOWLS")

    # 1020 INPUT "DO YOU NEED INSTRUCTIONS? ENTER YES OR NO";Z$
    Z = input("DO YOU NEED INSTRUCTIONS? ENTER YES OR NO? ")
    print()
    # 1030 DIM B(9),B1(9),D(9),V(9),X(9),Y(9)
    B = [0]*10
    B1 = [0]*10
    D = [0]*10
    V = [0]*10
    X = [0]*10
    Y = [0]*10

    # 1040 PRINT: IF Z$="YES" THEN GOSUB 1770
    if Z.strip().upper() == "YES":
        # 1770-1880 Instructions
        print("IN THIS GAME YOU ROLL", Q-1, "BALLS SUCCESSIVELY AT A TARGET")
        print("BALL (CALLED A JACK). THE OBJECT IS TO GET THE BALLS AS CLOSE")
        print("TO THE JACK AS POSSIBLE. THE BALLS ARE 10 CM IN DIAMETER AND")
        print("ARE WEIGHTED SO THAT THEY ROLL IN A CURVE. YOU WILL HAVE TO")
        print("ROLL THEM AT AN ANGLE TO THE LINE FROM YOU AT COORDINATES 0,0")
        print("TO THE JACK AT COORDINATES X,Y. A POSITIVE ANGLE WILL MAKE")
        print("THE BALL CURVE CLOCKWISE. A NEGATIVE ANGLE WILL  MAKE IT CURVE")
        print("ANTI-CLOCKWISE. THE JACK IS A 4 CM WIDE AND WILL ROLL")
        print("STRAIGHT IF YOU HIT IT. BALLS HIT BY YOUR THROWN BALL MAY")
        print("CURVE IN EITHER DIRECTION.")
        print()
        print("HINT. TRY AN INITIAL VELOCITY OF 500 AND AN ANGLE OF 10")
        print("\n")

    # 1045 P1=3.14159
    P1 = 3.14159

    # 1050 S1=0:S2=0:A=-49.3
    S1 = 0
    S2 = 0
    A = -49.3

    # 1070 X(1)=INT(2000+700*RND(1)): Y(1)=INT(200-400*RND(1))
    X[1] = 2203
    Y[1] = 199

    # For consistent output, you can uncomment the following lines:
    # X[1] = 2203
    # Y[1] = 199

    # 1080 PRINT "THE JACK IS LOCATED AT ";X(1);Y(1)
    print("THE JACK IS LOCATED AT", X[1], Y[1])

    D1 = 0

    # 1090 FOR P=2 TO Q
    for P in range(2, Q + 1):
        # 1100 J=P:GOSUB 1570
        J = P

        # 1570 PRINT "BALL ";(J-1)
        print("BALL", J - 1)

        # 1580 INPUT "VELOCITY";V(J):V(J)=ABS(V(J))
        while True:
            V[J] = abs(float(input("VELOCITY? ")))
            # 1590 IF V(J) > 1000 THEN PRINT "VELOCITY TOO HIGH":GOTO 1580
            if V[J] > 1000:
                print("VELOCITY TOO HIGH")
            else:
                break

        # 1600 INPUT "ANGLE";B1(J)
        while True:
            B1[J] = float(input("ANGLE? "))
            # 1610 IF ABS(B1(J))> 89 THEN PRINT "ANGLE TO BIG":GOTO 1290
            if abs(B1[J]) > 89:
                print("ANGLE TOO BIG")
            else:
                break

        # 1620 PRINT : B(J)=ABS(B(J)*P1/180):GOTO 1290
        print()
        B[J] = abs(B1[J] * P1 / 180)

        # Initialize variables for ball movement
        K1 = -20
        if J == 1:
            K1 = 0

        # Ball movement calculations
        while True:
            A1 = A * math.cos(B[J]) + K1 * math.cos((P1 / 2) + B[J])
            A2 = A * math.sin(B[J]) + K1 * math.sin((P1 / 2) + B[J])
            S3 = V[J] * B[J] * 0.05 + 1.25E-03 * A1
            S4 = V[J] * B[J] * 0.05 + 1.25E-03 * A2
            B[J] = math.atan((V[J] * B[J] + A2 * 0.05) / (V[J] * B[J] + A1 * 0.05))
            if B1[J] < 0:
                S4 = -S4
            S5 = S1 + S3
            S6 = S2 + S4
            if J != 1:
                if abs(S5 - X[1]) < 7 and abs(S6 - Y[1]) < 7:
                    K = 1
                    if J == 1:
                        V[J] = 5 * V[J]
            for K in range(2, Q + 1):
                if K == J or X[K] == 0:
                    continue
                if abs(S5 - X[K]) < 10 and abs(S6 - Y[K]) < 10:
                    B[K] = math.atan((Y[K] - S2) / (X[K] - S1))
                    print('\a', end='')  # Beep
                    if J == 1:
                        V[J] = V[J] / 5
                    V[J] = abs(V[J] * B[J] - B[K])
                    V[K] = abs(V[J] * B[J] - B[K])
                    B[J] = (P1 / 2) + B[K]
                    S5 = S1
                    S6 = S2
                    if K == 1:
                        V[K] = 5 * V[K]
            if V[J] < abs(A * 0.05):
                break
            V[J] += A * 0.05
            S1 = S5
            S2 = S6

        # 1440 X(J)=X(J)+S5: Y(J)=Y(J)+S6:S1=0:S2=0:S5=0:S6=0
        X[J] = X[J] + S5
        Y[J] = Y[J] + S6
        S1 = 0
        S2 = 0
        S5 = 0
        S6 = 0

        # 1450 FOR L=1 TO Q
        for L in range(1, Q + 1):
            if V[L] > abs(A * 0.05):
                J = L
                continue
            B[L] = 0
            V[L] = 0

        # 1630 PRINT "JACK AT COORDINATES ";X(1);Y(1)
        print("JACK AT COORDINATES", X[1], Y[1])

        # 1640 FOR M=2 TO P
        for M in range(2, P + 1):
            D_value = (math.sqrt((Y[1] - Y[M]) ** 2 + (X[1] - X[M]) ** 2)) - 7
            D[M] = max(D_value, 0)
            # 1670 PRINT"BALL ";(M-1);" AT COORDINATES ";X(M);Y(M);" IT IS ";D(M);
            print("BALL", M - 1, "AT COORDINATES", X[M], Y[M], "IT IS", D[M], "FROM THE JACK")

        # 1690 PRINT
        print()

        # 1700 IF D(P) < 10 THEN PRINT TAB(15);"EXCELLENT SHOT! ";:GOTO 1740
        if D[P] < 10:
            print(" " * 15 + "EXCELLENT SHOT!")
        elif D[P] < 20:
            print(" " * 15 + "GOOD SHOOTING!")
        elif D[P] < 30:
            print(" " * 15 + "NICE TRY !")
        elif D[P] > 500:
            print(" " * 5 + "YECH! OVER", int(D[P] / 30.48), "FEET AWAY!")
        # 1740 IF X(P)>X(1) THEN PRINT "LONG AND ";
        if X[P] > X[1]:
            print("LONG AND ", end='')
        # 1745 IF X(P)< X(1) THEN PRINT "SHORT AND ";
        if X[P] < X[1]:
            print("SHORT AND ", end='')
        # 1750 IF Y(P)>Y(1) THEN PRINT "TO THE LEFT "
        if Y[P] > Y[1]:
            print("TO THE LEFT")
        # 1755 IF Y(P) < Y(1) THEN PRINT "TO THE RIGHT"
        if Y[P] < Y[1]:
            print("TO THE RIGHT")
        # 1760 PRINT
        print()

        D1 += D[P]

    # 1150 PRINT: PRINT "THE TOTAL DISTANCE OF ALL BALLS FROM THE JACK IS ";
    # 1155 PRINT D1;" CM"
    print()
    print("THE TOTAL DISTANCE OF ALL BALLS FROM THE JACK IS", D1, "CM")

    # Performance messages
    if D1 < Q ** 2:
        print("MAGNIFICENT BOWLING! WHAT AN EYE!!")
    elif D1 < 2 * Q ** 2:
        print("EXCELLENT BUT COULD BE BETTER:")
    elif D1 < 3 * Q ** 2:
        print("GOOD BUT NEEDS SOME IMPROVEMENT")
    elif D1 < 6 * Q ** 2:
        print("FAIR - YOU NEED MORE PRACTICE")
    elif D1 < 10 * Q ** 2:
        print("POOR - TRY TO BE MORE CONSISTENT")
    elif D1 < 20 * Q ** 2:
        print("YOUR GAME NEEDS LOTS OF WORK")
    else:
        print("DON'T PLAY THIS GAME FOR MONEY!!")

    # 1260 PRINT:INPUT "CARE TO TRY AGAIN? ENTER YES OR NO";Y$
    print()
    YS = input("CARE TO TRY AGAIN? ENTER YES OR NO? ")

    # 1270 PRINT: IF Y$="YES" THEN 1050
    if YS.strip().upper() != "YES":
        break
    print()

# 1890 END