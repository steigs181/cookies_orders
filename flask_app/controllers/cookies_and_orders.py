from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.cookie_and_order import Cookie_and_order


@app.route('/')
def index():
    return redirect('/cookies')

@app.route('/cookies')
def display_all():
    print('running')
    all_cookies = Cookie_and_order.get_all_cookies()
    return render_template('cookies.html', all_cookies = all_cookies)

@app.route('/cookies/<int:cookie_id>')
def get_one(cookie_id):
    one_order = Cookie_and_order.get_one_order(cookie_id)
    return render_template('change_order.html', one_order = one_order)

@app.route('/cookies/<int:cookie_id>/update', methods=["POST"])
def update_cookie_order(cookie_id):

    updated_order = request.form

    if not Cookie_and_order.validate_order(updated_order):
        return redirect(f"/cookies/{cookie_id}")

    Cookie_and_order.update_order(updated_order)
    return redirect('/cookies')


@app.route('/cookies/new_order', methods=['POST'])
def new_order():
    Cookie_and_order.save_order(request.form)
    return redirect('/cookies')

@app.route('/cookies/new')
def submit_new():
    return render_template('new_order.html')