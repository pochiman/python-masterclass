from bottle import run, route

@route("/")
def home():
  return "Hello, Ninjas!"

# api endpoints
@route("/api/ninjas")
def get_ninjas():
  ninja_data = {
    "name": "Yoshi",
    "belt_color": "Black",
    "special_move": "Shadow Strike"
  }
  message = f"{ninja_data['name']} is a {ninja_data['belt_color']} belt ninja."
  return message

if __name__ == '__main__':
  # use the run function to run the app
  run(host="localhost", port=8080, debug=True, reloader=True)