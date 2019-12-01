# Flask
from datadog import statsd
from ddtrace import tracer
from flask import Flask, render_template, request
import os
import requests

app = Flask(__name__)


@app.route("/", methods = ["GET", "POST"])
def index():
    statsd.increment("hot_dog.pageviews", tags = ["page:index"])

    if "dog1" in request.values:
        dog1 = request.values.get('dog1')
        count1 = int(request.values.get('count1')) + 1

        if count1 > 2:
            save_dog(dog1)
            return render_template("hottest-dog.html", dog = dog1)
    else:
        dog1 = get_dog()
        count1 = 0

    if "dog2" in request.values:
        dog2 = request.values.get('dog2')
        count2 = int(request.values.get('count2')) + 1

        if count2 > 2:
            save_dog(dog2)
            return render_template("hottest-dog.html", dog = dog2)
    else:
        dog2 = get_dog()
        count2 = 0

    return render_template("hot-dog.html", dog1 = dog1, count1 = count1, dog2 = dog2, count2 = count2)


@tracer.wrap()
def save_dog(dog):
    statsd.increment("hot_dog.save_dog")
    if "SAVE_DOG_LAMBDA" in os.environ:
        r = requests.put(os.environ.get("SAVE_DOG_LAMBDA"), json = {"dog": dog})
        print(r.json())

@tracer.wrap()
def get_dog():
    statsd.increment("hot_dog.generate_dog")
    r = requests.get("https://dog.ceo/api/breeds/image/random")
    data = r.json()
    return data["message"]


if __name__ == "__main__":
    app.run(host = "0.0.0.0")
