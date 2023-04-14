from flask import Flask, render_template,redirect,request
import pandas as pd
import pickle
model=pickle.load(open('rfr_model.pkl','rb'))
teams=['Kolkata Knight Riders', 'Chennai Super Kings', 'Rajasthan Royals',
                    'Mumbai Indians', 'Deccan Chargers', 'Kings XI Punjab',
                    'Royal Challengers Bangalore', 'Delhi Daredevils',
                    'Kochi Tuskers Kerala', 'Pune Warriors', 'Sunrisers Hyderabad',
                    'Rising Pune Supergiants', 'Gujarat Lions',
                    'Rising Pune Supergiant']
dict_bat={}
for key ,value in zip(teams,range(1,14)):
    dict_bat[key]=str(value)
    
 
    
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    result=''
    if request.method=='POST':
        bat_team=request.form['bat_team']
        bowl_team=request.form['bowl_team']
        
        try:
            runs=float(request.form['runs'])
            overs=float(request.form['overs'])
            runs_last_5=float(request.form['runs_last_5'])
            wickets_last_5=float(request.form['wickets_last_5'])
        except(Exception ):
            result='Please Enter Numeric Values'  
            return render_template('index.html',prediction=result) 
        bat_team_Chennai=0
        bat_team_Deccan =0
        bat_team_Delhi =0
        bat_team_Gujarat=0
        bat_team_Kings =0
        bat_team_Kochi=0
        bat_team_Kolkata =0
        bat_team_Mumbai =0
        bat_team_Pune =0
        bat_team_Rajasthan =0
        bat_team_Rising  =0 
        bat_team_Royal =0
        bat_team_Sunrisers =0
        
        bowl_team_Chennai=0
        bowl_team_Deccan =0
        bowl_team_Delhi =0
        bowl_team_Gujarat=0
        bowl_team_Kings =0
        bowl_team_Kochi=0
        bowl_team_Kolkata =0
        bowl_team_Mumbai =0
        bowl_team_Pune =0
        bowl_team_Rajasthan =0
        bowl_team_Rising  =0 
        bowl_team_Royal =0
        bowl_team_Sunrisers =0
        
        bat=[bat_team_Chennai,
        bat_team_Deccan ,
        bat_team_Delhi ,
        bat_team_Gujarat,
        bat_team_Kings ,
        bat_team_Kochi,
        bat_team_Kolkata ,
        bat_team_Mumbai ,
        bat_team_Pune ,
        bat_team_Rajasthan, 
        bat_team_Rising   ,
        bat_team_Royal ,
        bat_team_Sunrisers ]
        
        bowl=[bowl_team_Chennai,
        bowl_team_Deccan ,
        bowl_team_Delhi ,
        bowl_team_Gujarat,
        bowl_team_Kings ,
        bowl_team_Kochi,
        bowl_team_Kolkata ,
        bowl_team_Mumbai ,
        bowl_team_Pune ,
        bowl_team_Rajasthan, 
        bowl_team_Rising   ,
        bowl_team_Royal ,
        bowl_team_Sunrisers ] 
        
        bat[int(dict_bat.get(bat_team))-1]=1
        bowl[int(dict_bat.get(bowl_team))-1]=1
        
        
        pre=pd.DataFrame([[runs,overs,runs_last_5,wickets_last_5,bat_team_Chennai,bat_team_Deccan,
                           bat_team_Delhi,bat_team_Gujarat,bat_team_Kings,bat_team_Kochi,
                           bat_team_Kolkata,bat_team_Mumbai,bat_team_Pune,bat_team_Rajasthan,bat_team_Rising,
                           bat_team_Royal,bat_team_Sunrisers,bowl_team_Chennai,bowl_team_Deccan,
                           bowl_team_Delhi,bowl_team_Gujarat,bowl_team_Kings,bowl_team_Kochi,
                           bowl_team_Kolkata,bowl_team_Mumbai,bowl_team_Pune,bowl_team_Rajasthan,bowl_team_Rising,
                           bowl_team_Royal,bowl_team_Sunrisers]]) 
        output=model.predict(pre)[0]
        output=round(output,2)
        result='Predicted Scores are {}'.format(output)
        return render_template('index.html',prediction=result) 
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)