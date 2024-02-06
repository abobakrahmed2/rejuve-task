from flask import Flask
import random
import time

app = Flask(__name__)

# Function to calculate Pi using Leibniz's formula
def calculate_pi():
    n = 1000000
    pi = 0
    for i in range(n):
        pi += (-1) ** i / (2 * i + 1)
    pi *= 4
    return pi

# Route to display the calculated Pi
@app.route('/pi')
def show_pi():
    return f"The calculated value of Pi is: {calculate_pi()}"

# Route to display a random pseudo-random sequence
@app.route('/random_sequence')
def show_random_sequence():
    random_sequence = [random.randint(1, 100) for _ in range(10)]
    return f"The random pseudo-random sequence is: {random_sequence}"

# Route to display the POSIX timestamp
@app.route('/timestamp')
def show_timestamp():
    timestamp = time.time()
    return f"The POSIX timestamp is: {timestamp}"

if __name__ == '__main__':
    app.run(debug=True)
