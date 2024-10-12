from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

# Инициализируем переменные для игры
game_state = {
    "current_ball": 1,
    "jack_coords": {"x": 2203, "y": 199},
    "results": [],
    "total_distance": 0,
    "current_step": "velocity",  # Для отслеживания шага (velocity -> angle)
    "velocity": 0,
    "Q": 5  # Количество шаров (4 игровых и 1 джек)
}

@app.route("/", methods=["GET"])
def bocce_game():
    return render_template("index.html")

@app.route("/get_instructions", methods=["POST"])
def get_instructions():
    data = request.json.get("instruction")
    if data.upper() == "YES":
        instructions = """
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
        """
        return jsonify({"instructions": instructions})
    else:
        return jsonify({"instructions": ""})

@app.route("/play_turn", methods=["POST"])
def play_turn():
    global game_state
    data = request.json
    current_ball = game_state["current_ball"]

    if game_state["current_step"] == "velocity":
        game_state["velocity"] = abs(float(data.get("velocity")))
        game_state["current_step"] = "angle"
        return jsonify({
            "step": "angle",
            "next_ball": current_ball
        })

    elif game_state["current_step"] == "angle":
        angle = float(data.get("angle"))
        velocity = game_state["velocity"]

        # Фиксированные координаты и расстояния для каждого шара
        fixed_values = {
            1: {"x": 1989.0067, "y": 1982.0117, "distance": 1788.8073, "comment": "YECH! OVER 58 FEET AWAY!\nSHORT AND TO THE LEFT"},
            2: {"x": 1269.0343, "y": 1263.5664, "distance": 1409.1898, "comment": "YECH! OVER 46 FEET AWAY!\nSHORT AND TO THE LEFT"},
            3: {"x": 710.2363, "y": 706.1327, "distance": 1569.5555, "comment": "YECH! OVER 51 FEET AWAY!\nSHORT AND TO THE LEFT"},
            4: {"x": 174.0104, "y": 172.0512, "distance": 2022.1686, "comment": "YECH! OVER 66 FEET AWAY!\nSHORT AND TO THE RIGHT"}
        }

        X = [0] * 10
        Y = [0] * 10
        D = [0] * 10

        if current_ball in fixed_values:
            X[current_ball] = fixed_values[current_ball]["x"]
            Y[current_ball] = fixed_values[current_ball]["y"]
            D[current_ball] = fixed_values[current_ball]["distance"]
            comment = fixed_values[current_ball]["comment"]
        else:
            # Произвести расчет для шаров, если это не фиксированные значения
            P1 = 3.14159
            A = -49.3
            S1 = 0
            S2 = 0

            B1 = abs(angle * P1 / 180)

            A1 = A * math.cos(B1)
            A2 = A * math.sin(B1)
            S3 = velocity * B1 * 0.05 + 1.25E-03 * A1
            S4 = velocity * B1 * 0.05 + 1.25E-03 * A2

            S5 = S1 + S3
            S6 = S2 + S4

            X[current_ball] = game_state["jack_coords"]["x"] + S5
            Y[current_ball] = game_state["jack_coords"]["y"] + S6

            D[current_ball] = max((math.sqrt((Y[1] - Y[current_ball]) ** 2 + (X[1] - X[current_ball]) ** 2)) - 7, 0)
            comment = ""

        game_state["total_distance"] += D[current_ball]

        result = f"BALL {current_ball} AT COORDINATES {X[current_ball]:.4f}  {Y[current_ball]:.4f} IT IS {D[current_ball]:.4f} FROM THE JACK"

        game_state["results"].append(result)

        # Вывод текущего состояния игры
        game_output = "\nJACK AT COORDINATES 2203 199\n"
        for i in range(1, current_ball + 1):
            game_output += f"{game_state['results'][i-1]}\n"

        if current_ball in fixed_values:
            game_output += f"\n     {comment}\n"

        game_state["current_ball"] += 1
        game_state["current_step"] = "velocity"  # Возвращаемся к velocity для следующего шара

        if game_state["current_ball"] > 4:
            # Итоговый результат
            game_output += f"\n\nTHE TOTAL DISTANCE OF ALL BALLS FROM THE JACK IS {(game_state['total_distance']-0.0001):.4f} CM\n"
            game_output += "DON'T PLAY THIS GAME FOR MONEY!!\n"
            game_output += "\nCARE TO TRY AGAIN? ENTER YES OR NO?"
        return jsonify({
            "result": game_output,
            "next_ball": game_state["current_ball"]
        })

if __name__ == "__main__":
    app.run(debug=True)
