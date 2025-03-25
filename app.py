from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary storage for expenses
expenses = []

@app.route("/")
def index():
    return render_template("index.html", expenses=expenses)

@app.route("/add", methods=["POST"])
def add_expense():
    # Get form data
    name = request.form.get("name")
    amount = float(request.form.get("amount"))
    date = request.form.get("date")
    # Add expense to the list
    expenses.append({"name": name, "amount": amount, "date": date})
    return redirect(url_for("index"))

@app.route("/delete/<int:index>")
def delete_expense(index):
    # Remove the expense by index
    if 0 <= index < len(expenses):
        expenses.pop(index)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
