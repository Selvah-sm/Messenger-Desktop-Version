from flask import Flask, request,jsonify, json
import boto3

app = Flask(__name__)

ACCESS_KEY_ID = 'AKIAIOYS57PN5EU6X57A'

SECRET_ACCESS_KEY = '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'

QUEUE_URL = 'https://sqs.us-east-1.amazonaws.com/253928775046/'

REGION_NAME = 'us-east-1'

USER_INFO = []

TeamOneUID = []
TeamTwoUID = []


##### PUMP LOG INTO THE QUEUE ######

@app.route('/pumpLog',methods=['POST','GET'])
def pumpLog():
    activity=request.form['text']
    token = request.form['token']
    sqsName = request.form['sqsid']
    print (activity)
    print (token)
    print (sqsName)
    sqs = boto3.resource('sqs', region_name = REGION_NAME , aws_access_key_id = ACCESS_KEY_ID , aws_secret_access_key = SECRET_ACCESS_KEY)
    queue = sqs.get_queue_by_name(QueueName=sqsName)
    queue_url = QUEUE_URL + sqsName
    response = queue.send_message(
    QueueUrl=queue_url,
    DelaySeconds=0,
    MessageBody=(
        activity
    ))
    print(response['MessageId'])
    return 'Message queued successfully!'
    return ''

###### Queuing Messages in SQS   #######


#### CREATING QUEUE IN SQS #######

@app.route('/createsqs',methods=['POST','GET'])
def createsqs():
    sqsname = request.form['text1']+'to'+request.form['text2']
    sqs = boto3.resource('sqs',region_name= REGION_NAME , aws_access_key_id= ACCESS_KEY_ID,aws_secret_access_key=SECRET_ACCESS_KEY)
    queue = sqs.create_queue(QueueName=sqsname, Attributes={'DelaySeconds': '0'})
    print (queue.url)
    return 'Queue Created Successfully!'

######   QUEUE CREATION DONE #######


###### UID REGISTRATION #####

@app.route('/registration',methods=['POST','GET'])
def registration():
    username = request.form['username']
    text = request.form['text']
    global USER_INFO
    USER_INFO.append(text+'|'+ username)
    return ''
##### UID DONE #####
@app.route('/getmemberslist',methods=['POST','GET'])
def getmemberslist():
    team = request.form['text']
    print (team)
    Users=''
    if team ==  'teamA':
        global TeamOneUID
        print(TeamOneUID)
        return jsonify(TeamOneUID)
    else:
        global TeamTwoUID
        print(TeamTwoUID)
        return jsonify(TeamTwoUID)
    return ''

##### JOIN TEAM ####
@app.route('/jointeam',methods=['POST','GET'])
def jointeam():
    teamid = request.form['text']
    deviceuid = request.form['uid']
    if teamid == '101':
        global TeamOneUID
        if not  deviceuid in TeamOneUID:
            TeamOneUID.append(deviceuid)
            print('TeamOneUID')
        return 'Team A'
    else:
        global TeamTwoUID
        if not deviceuid in TeamTwoUID:
            TeamTwoUID.append(deviceuid)
            print('TeamTwoUID')
        return 'Team B'

    return ''
#### JOIN TEAM ENDED ######



 #### DRAIN LOG FROM THE QUEUE ######

@app.route('/drainLog',methods=['POST','GET'])
def drainLog():
    token = request.form['token']
    sqsName = request.form['sqsid']
    print (sqsName)
    print (token)
    sqs = boto3.resource('sqs',region_name= REGION_NAME , aws_access_key_id=ACCESS_KEY_ID ,aws_secret_access_key= SECRET_ACCESS_KEY)
    queue = sqs.get_queue_by_name(QueueName=sqsName)
    queue_url = QUEUE_URL + sqsName
    try:
        for message in queue.receive_messages():
            message.delete()
        return format(message.body)
    except:
        return ''
#### DEQUE DONE ####

if __name__=="__main__":
    app.run(host='0.0.0.0',port=9999)
