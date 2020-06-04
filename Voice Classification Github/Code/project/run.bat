call "C:\Users\HP\anaconda3\Scripts\activate.bat"
cd /D "D:\Voice Classification\Code\project\"
call conda activate env_keras
set FLASK_APP=predict_app.py
flask run --host=0.0.0.0