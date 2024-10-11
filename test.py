import subprocess


def process(command):
    return subprocess.Popen(
        command.split(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
        shell=True
    )


def expect(proc, pattern):
    pattern = pattern.strip("\n")
    buffer = ""
    while True:
        buffer += proc.stdout.read(1).decode()
        if pattern.endswith(buffer):
            return True


def write(proc, text):
    proc.stdin.write(f'{text}\n'.encode())
    proc.stdin.flush()
    return text


def test():
    print("Launching processes")
    try:
        # Запуск bocce.bas и bocce.py
        py = process('python bocce.py')
        bas = process('bocce.bas')  # Замените на правильную команду для запуска bocce.bas

        # Проверка вывода приветствия:
        expected_greetings = '''
                         BOCCE
                  CREATIVE COMPUTING
                MORRISTOWN NEW JERSEY


THIS GAME SIMULATES THE GAME OF LAWN BOWLS
DO YOU NEED INSTRUCTIONS? ENTER YES OR NO? 
'''
        print("expecting answers...")
        expect(py, expected_greetings)
        expect(bas, expected_greetings)
        print("[+] TEST 1 - PASSED")

        # Отправка ответа "YES"
        print("sending keys...")
        write(py, 'YES')
        write(bas, 'YES')
        print("[+] KEYS SENT")

        # Проверка вывода инструкции:
        instruction = '''
IN THIS GAME YOU ROLL 4 BALLS SUCCESSIVELY AT A TARGET
BALL (CALLED A JACK). THE OBJECT IS TO GET THE BALLS AS CLOSE
TO THE JACK AS POSSIBLE. THE BALLS ARE 10 CM IN DIAMETER AND
ARE WEIGHTED SO THAT THEY ROLL IN A CURVE. YOU WILL HAVE TO
ROLL THEM AT AN ANGLE TO THE LINE FROM YOU AT COORDINATES 0,0
TO THE JACK AT COORDINATES X,Y. A POSITIVE ANGLE WILL MAKE
THE BALL CURVE CLOCKWISE. A NEGATIVE ANGLE WILL MAKE IT CURVE
ANTI-CLOCKWISE. THE JACK IS A 4 CM WIDE AND WILL ROLL
STRAIGHT IF YOU HIT IT. BALLS HIT BY YOUR THROWN BALL MAY
CURVE IN EITHER DIRECTION.

HINT. TRY AN INITIAL VELOCITY OF 500 AND AN ANGLE OF 10

THE JACK IS LOCATED AT 2203 199
BALL 1
VELOCITY? 
'''
        expect(py, instruction)
        expect(bas, instruction)
        print("[+] TEST 2 - PASSED")

        # Отправка значений скорости и угла для каждого мяча
        test_values = [
            ('500', '50'),
            ('400', '40'),
            ('300', '30'),
            ('150', '15')
        ]

        for i, (velocity, angle) in enumerate(test_values, start=1):
            # Отправка значения скорости
            print(f"sending velocity for BALL {i}...")
            write(py, velocity)
            write(bas, velocity)
            print("[+] KEYS SENT")

            # Проверка вывода для ввода угла
            angle_prompt = 'ANGLE? '
            expect(py, angle_prompt)
            expect(bas, angle_prompt)
            print(f"[+] TEST {i * 2 + 1} - PASSED")

            # Отправка значения угла
            print(f"sending angle for BALL {i}...")
            write(py, angle)
            write(bas, angle)
            print("[+] KEYS SENT")

            # Проверка корректного продолжения игры после ввода
            if i < len(test_values):
                next_ball_prompt = f'BALL {i + 1}\nVELOCITY? '
                expect(py, next_ball_prompt)
                expect(bas, next_ball_prompt)
                print(f"[+] TEST {i * 2 + 2} - PASSED")

        # Проверка итогового вывода после всех мячей
        final_result = '''
JACK AT COORDINATES 2203 199
BALL 1 AT COORDINATES .* IT IS .* FROM THE JACK

     YECH! OVER .* FEET AWAY!
SHORT AND TO THE LEFT

BALL 2
VELOCITY? 400
ANGLE? 40

JACK AT COORDINATES 2203 199
BALL 1 AT COORDINATES .* IT IS .* FROM THE JACK
BALL 2 AT COORDINATES .* IT IS .* FROM THE JACK

     YECH! OVER .* FEET AWAY!
SHORT AND TO THE LEFT

BALL 3
VELOCITY? 300
ANGLE? 30

JACK AT COORDINATES 2203 199
BALL 1 AT COORDINATES .* IT IS .* FROM THE JACK
BALL 2 AT COORDINATES .* IT IS .* FROM THE JACK
BALL 3 AT COORDINATES .* IT IS .* FROM THE JACK

     YECH! OVER .* FEET AWAY!
SHORT AND TO THE LEFT

BALL 4
VELOCITY? 150
ANGLE? 15

JACK AT COORDINATES 2203 199
BALL 1 AT COORDINATES .* IT IS .* FROM THE JACK
BALL 2 AT COORDINATES .* IT IS .* FROM THE JACK
BALL 3 AT COORDINATES .* IT IS .* FROM THE JACK
BALL 4 AT COORDINATES .* IT IS .* FROM THE JACK
     YECH! OVER .* FEET AWAY!
SHORT AND TO THE LEFT

THE TOTAL DISTANCE OF ALL BALLS FROM THE JACK IS .* CM
DON'T PLAY THIS GAME FOR MONEY!!

CARE TO TRY AGAIN? ENTER YES OR NO? 
'''
        expect(py, final_result)
        expect(bas, final_result)
        print("[+] TEST FINAL - PASSED")

    except Exception as ex:
        print(ex)

test()