from flask import Flask, render_template, request

app = Flask(__name__)

# Display the form
@app.route("/")
def hello_world():
    return render_template ("a.html")

# Handle form submission
@app.route("/signup", methods=["POST"])
def sign_up():
    form_data = request.form
    # Print out all the form data
    print(form_data)

    return render_template ("thankyouinvite.html")

    # Send the email
    requests.post(
        "https://api.mailgun.net/v3/sandbox5af5766a588f49e1bc50d2eb8c5ec041.mailgun.org/messages",
        auth=("api", "b90ab23a13c88e8ab3543db5fb33b861-acb0b40c-b198b13f"),
        data={"from": "Excited User <mailgun@sandbox5af5766a588f49e1bc50d2eb8c5ec041.mailgun.org>",
              "to": form_data["recipient"],
              "subject": "Hello",
              "text": form_data["body"]})

    return "All OK"

app.run(debug=True)
