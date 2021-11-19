from flask import Flask
from fizzbuzz.lib.fizzbuzz import fizzbuzz as fb

app = Flask(__name__)


@app.route("/fizzbuzz/<int:input>")
def fizzbuzz(input):
    return fb(input)


if __name__ == "__main__":
    app.run()
