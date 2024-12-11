from bottle import run, route, response

# data
ninjas = [
  {
    "name": "Yoshi",
    "belt_color": "Black",
    "special_move": "Shadow Strike"
  },
  {
    "name": "Hattori",
    "belt_color": "Green",
    "special_move": "Tornado Blast"
  },
  {
    "name": "Momochi",
    "belt_color": "Blue",
    "special_move": "Rain Leap"
  }
]

@route("/")
def home():
  return "Hello, Ninjas!"

# api endpoints
@route("/api/ninjas")
def get_ninjas():
  response.content_type = "application/json"
  return {"data": ninjas}

if __name__ == '__main__':
  # use the run function to run the app
  run(host="localhost", port=8080, debug=True, reloader=True)