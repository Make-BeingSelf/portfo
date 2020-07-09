from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__) # <Flask 'server'>

# @app. : 이것이 어떻게 작동하는지 (내부구조) 알 필요없이 어떠한 작업을 수행하는지 알면 된다.

@app.route('/') # 해당 url을 구축
def home():
    return render_template('index.html')

@app.route('/<string:page_name>') # 해당 url을 구축
def page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thanks.html')
        except:
            return 'File did not save to database'
    else:
        return 'Wrong something'

# def write_to_file(data):
#     with open('database.txt', mode='a') as database:
#         email=data['email']
#         subject=data['subject']
#         message=data['message']
#         file = database.write(f'[email] {email}\n[subject] {subject}\n[message]\n{message}\n\n')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='\n') as csvfile:
        email=data['email']
        subject=data['subject']
        message=data['message']
        file = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        file.writerow([email, subject, message])


# @app.route('/works.html')
# def works():
#     return render_template('works.html')
#
# @app.route('/work.html')
# def work():
#     return render_template('work.html')
#
# @app.route('/about.html')
# def about():
#     return render_template('about.html')
#
# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')
#
# @app.route('/components.html')
# def components():
#     return render_template('components.html')