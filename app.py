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
    
    fileType = filename.split('.')
    fileType1 = fileType[1]
    if(fileType1 == 'yml' or fileType1 == 'json'):
        myRepo = str(sys.argv[1])
        github = Github()
        user = github.get_user("abhiCITI1")
        repositories = user.get_repos()
        
        for repo in repositories:
            repostoryName = "https://github.com/" + str(repo.full_name)
            
            if(repostoryName == myRepo):
                try:
                    file_content = repo.get_contents(filename ,ref = 'master')
                    file_data = base64.b64decode(file_content.content)
                    return str(file_data)
                except Exception:
                    return "File is invalid..Not found in your Github repository."
    else:
        return "File is invalid..Not found in your Github repository."


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
