from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        # return redirect('/index#Contact')
        return redirect('/thankyou.html#Contact')
        # return render_template('index.html', form_submitted=True)
    return render_template('index.html', form_submitted=False)
