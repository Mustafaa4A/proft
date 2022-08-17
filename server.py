from flask import Flask, render_template,request, redirect
import csv

app = Flask(__name__)


@app.get('/')
def index():
  return render_template('index.html')


@app.get('/about')
def about():
  return render_template('about.html')


@app.get('/contact')
def contact():
  return render_template('contact.html')

@app.get('/work.html')
def work():
  return render_template('work.html')

@app.get('/works')
def works():
  return render_template('works.html')


def write_to_file(data):
  email = data['email']
  subject = data['subject']
  message = data['message']
  with open('./database.txt', mode='a') as file:
    file.write(f'{email} {subject} {message}\n')
    

def write_to_csv(data):
  email = data['email']
  subject = data['subject']
  message = data['message']
  with open('./database.csv', mode='a', newline='') as database:
    csv_writter = csv.writer(database, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    csv_writter.writerow([email, subject, message])

@app.post('/submit_form')
def submit_form():
  data = request.form.to_dict()
  write_to_csv(data)
  return redirect('thankyou')





@app.get('/thankyou')
def thankyou():
  return render_template('thankyou.html')


if __name__ == "__main__":
  app.run(debug=True)
  
  
