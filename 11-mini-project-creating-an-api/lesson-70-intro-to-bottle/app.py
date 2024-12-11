from bottle import run, route

@route("/")
def home():
  return "Hello, Ninjas!"

if __name__ == '__main__':
  # use the run function to run the app
  run(host="localhost", port=8080, debug=True)