# simple-vuln-web-demo-01
This repository contains vulnerable Flask App for demo/education purposes.

## How to Use

1. Clone the repository
```
git clone https://github.com/suryadina/simple-vuln-web-demo-01.git
```
3. Setup python virtual environment
```
python3 -m venv myenv
```
4. Activate virtual environment

on MacOs/Linux
```
source myenv/bin/activate
```
on Windows
```
myenv\Scripts\activate
```
5. Install Flask
```
pip install Flask
```
6. Change directory
```
cd simple-vuln-web-demo-01/
```
7. Run the app
```
Flask run
```
8. The app will run on localhost port 5000. Use web browser to access it http://127.0.0.1:5000.

> ⚠️ **Warning:** The app is vulnerable to Remote Command Injection. The steps above will only expose the app to localhost which prevent remote access to the app. Please don't expose the app to external connection unless you understand the risk. Exposing the app to remote connection might allow real hacker to exploit the vulnerability and compromise the Host!!

