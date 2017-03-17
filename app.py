from flask import Flask
import github
from github import Github
import sys
import base64

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Dockerized Flask App!!"

@app.route('/v1/<filename>')
def get_Config(filename):
    
    ##print "Inside method" + filename
    if(filename == 'dev-config.yml' or filename == 'test-config.yml' or
       filename == 'dev-config.json' or filename == 'test-config.json'):
        username = 'abhishek.up25@gmail.com'
        myToken = 'token:e79f62af638d894a41bcf0975ba2d7cce92765df'
        
        actualToken = myToken.split(':')
        actualToken1 = str(actualToken[1])
        
        myRepo = str(sys.argv[1])
        
        github = Github(username, actualToken1)
        user = github.get_user()
        
        repositories = user.get_repos()
        
        for repo in repositories:
            repostoryName = "https://github.com/" + str(repo.full_name)
            
            if(repostoryName == myRepo):
                try:
                    file_content = repo.get_contents(filename ,ref = 'master')
                    file_data = base64.b64decode(file_content.content)
                    return str(file_data)
                except:
                    return "File is invalid..Not found in your Github repository."


    else:
        return "File is invalid..Not found in your Github repository."


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
