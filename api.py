from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/talk', methods=['POST'])
def talk():
    user_input = request.json.get('message')
    responses = {
        "Hello": "Hello! I'm Peppa Pig!",
        "How are you?": "I'm great! Thanks for asking!",
        "What do you like to do?": "I love jumping in muddy puddles!",
        "What's your favorite color?": "I love pink!",
        "Goodbye": "Goodbye! See you next time!",
    }
    response = responses.get(user_input, "I don't understand that.")
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
