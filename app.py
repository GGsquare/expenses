from flask import Flask, request, render_template, redirect, url_for
from flask import make_response, jsonify
from forms import ExpensesForm
from models import expenses

app = Flask(__name__)
app.config["SECRET_KEY"] = "moje_wydatki"

@app.route("/expenses/", methods=["GET", "POST"])
def expenses_list():
    form = ExpensesForm()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            expenses.create(form.data)
            expenses.save_all()
        return redirect(url_for("expenses_list"))
        
    return render_template("expenses.html", form=form, expenses=expenses.all(), error=error)


@app.route("/expenses/<int:expens_id>/", methods=["GET", "POST"])
def expens_details(expens_id):
    expens = expenses.get(expens_id - 1)
    form = ExpensesForm(data=expens)

    if request.method == "POST":
        if form.validate_on_submit():
            expenses.update(expens_id - 1, form.data)
        return redirect(url_for("expenses_list"))
    return render_template("expens.html", form=form, expens_id=expens_id)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found', 'status_code': 404}), 404)


def bad_request(error):
    return make_response(jsonify({'error': 'Bad request', 'status_code': 400}), 400)

if __name__ == "__main__":
    app.run(debug=True)