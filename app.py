from flask import Flask, request, render_template_string
import io
import sys

app = Flask(__name__)

HTML = '''
<h2>Online Python Executor</h2>
<form method="post">
<textarea name="code" rows=10 cols=60>{{ code }}</textarea><br><br>
<input type="submit" value="Run Code">
</form>

<h3>Output:</h3>
<pre>{{ output }}</pre>
'''

@app.route('/', methods=['GET','POST'])
def index():
    output = ""
    code = ""

    if request.method == 'POST':
        code = request.form['code']

        old_stdout = sys.stdout
        sys.stdout = mystdout = io.StringIO()

        try:
            exec(code)
        except Exception as e:
            print("Error:", e)

        sys.stdout = old_stdout
        output = mystdout.getvalue()

    return render_template_string(HTML, code=code, output=output)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)