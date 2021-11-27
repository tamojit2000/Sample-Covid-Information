from flask import Flask,render_template,redirect,request
from cowin_api import CoWinAPI


cowin = CoWinAPI()

app=Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.after_request
def add_header(response):
    # response.cache_control.no_store = True
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/centers',methods=['POST','GET'])
def centers():
    if request.method=='POST':
        pin_code=request.form['vaccine_center']
        available_centers = cowin.get_availability_by_pincode(pin_code)
        print(available_centers)
        print(type(available_centers))
        return render_template('centers.html',arg=available_centers)
    else:
        return redirect('/')


if __name__=='__main__':
    app.run(debug=True)
