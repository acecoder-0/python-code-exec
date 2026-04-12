from flask import Flask, request, render_template_string
import io
import sys

app = Flask(__name__)

HTML = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Cloud Executor</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=Fira+Code:wght@400;500&display=swap');

        :root {
            --bg-gradient-start: #0f172a;
            --bg-gradient-end: #1e1b4b;
            --container-bg: rgba(30, 41, 59, 0.65);
            --text-primary: #f8fafc;
            --text-secondary: #94a3b8;
            --accent-color: #6366f1;
            --accent-hover: #4f46e5;
            --border-color: rgba(255, 255, 255, 0.1);
        }

        body {
            margin: 0;
            padding: 2rem;
            min-height: 100vh;
            font-family: 'Inter', sans-serif;
            background: linear-gradient(135deg, var(--bg-gradient-start) 0%, var(--bg-gradient-end) 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--text-primary);
            box-sizing: border-box;
        }

        .container {
            width: 100%;
            max-width: 900px;
            background: var(--container-bg);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            padding: 2.5rem;
            border-radius: 24px;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
            border: 1px solid var(--border-color);
        }

        header {
            text-align: center;
            margin-bottom: 2rem;
        }

        h2 {
            margin: 0;
            font-weight: 600;
            font-size: 2.2rem;
            background: linear-gradient(135deg, #818cf8 0%, #c084fc 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            letter-spacing: -0.5px;
        }

        .subtitle {
            color: var(--text-secondary);
            font-size: 0.95rem;
            margin-top: 0.5rem;
        }

        .editor-container {
            position: relative;
            margin-bottom: 1.5rem;
            border-radius: 12px;
            overflow: hidden;
            border: 1px solid var(--border-color);
            background: #0b1120;
            box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.5);
            transition: border-color 0.3s ease;
        }

        .editor-container:focus-within {
            border-color: var(--accent-color);
            box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.5), 0 0 0 3px rgba(99, 102, 241, 0.2);
        }

        .editor-header {
            background: #1e293b;
            padding: 0.6rem 1rem;
            font-family: 'Inter', sans-serif;
            font-size: 0.8rem;
            color: var(--text-secondary);
            display: flex;
            align-items: center;
            border-bottom: 1px solid var(--border-color);
        }

        .dot {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            margin-right: 8px;
            box-shadow: inset 0 1px 2px rgba(255,255,255,0.2);
        }
        .dot-red { background-color: #ec6a5e; }
        .dot-yellow { background-color: #f4bf4f; }
        .dot-green { background-color: #61c554; }

        textarea {
            width: 100%;
            height: 300px;
            background: transparent;
            color: #e2e8f0;
            font-family: 'Fira Code', monospace;
            font-size: 0.95rem;
            padding: 1.2rem;
            border: none;
            resize: vertical;
            box-sizing: border-box;
            outline: none;
            line-height: 1.6;
            display: block;
        }

        .submit-btn {
            width: 100%;
            padding: 1rem;
            font-size: 1.1rem;
            font-weight: 600;
            color: white;
            background: var(--accent-color);
            border: none;
            border-radius: 12px;
            cursor: pointer;
            transition: all 0.2s ease;
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 8px;
            box-shadow: 0 4px 14px 0 rgba(99, 102, 241, 0.39);
        }

        .submit-btn:hover {
            background: var(--accent-hover);
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(99, 102, 241, 0.23);
        }

        .submit-btn:active {
            transform: translateY(0);
        }

        .output-section {
            margin-top: 2.5rem;
            animation: slideUp 0.4s ease-out forwards;
        }

        .output-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1rem;
        }

        .output-header h3 {
            margin: 0;
            font-size: 1.1rem;
            color: var(--text-primary);
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .output-header h3::before {
            content: '';
            display: block;
            width: 8px;
            height: 8px;
            background: #10b981;
            border-radius: 50%;
            box-shadow: 0 0 10px #10b981;
        }

        pre {
            background: #020617;
            color: #34d399;
            padding: 1.2rem;
            border-radius: 12px;
            font-family: 'Fira Code', monospace;
            font-size: 0.95rem;
            overflow-x: auto;
            border: 1px solid var(--border-color);
            min-height: 60px;
            white-space: pre-wrap;
            word-wrap: break-word;
            line-height: 1.5;
            box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.3);
        }

        @keyframes slideUp {
            from { opacity: 0; transform: translateY(15px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Custom Scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }
        ::-webkit-scrollbar-track {
            background: #0b1120;
            border-radius: 4px;
        }
        ::-webkit-scrollbar-thumb {
            background: #334155;
            border-radius: 4px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #475569;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h2>Python Cloud Executor</h2>
            <div class="subtitle">Write, compile, and run your Python code instantly</div>
        </header>
        
        <form method="post">
            <div class="editor-container">
                <div class="editor-header">
                    <div class="dot dot-red"></div>
                    <div class="dot dot-yellow"></div>
                    <div class="dot dot-green"></div>
                    <span style="margin-left: 10px; opacity: 0.8;">main.py</span>
                </div>
                <textarea name="code" placeholder="# Write your Python code here..." spellcheck="false">{{ code }}</textarea>
            </div>
            
            <button type="submit" class="submit-btn">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
                Execute Code
            </button>
        </form>

        {% if output or request.method == 'POST' %}
        <div class="output-section">
            <div class="output-header">
                <h3>Terminal Output</h3>
            </div>
            <pre>{{ output if output else "Process finished with exit code 0." }}</pre>
        </div>
        {% endif %}
    </div>
</body>
</html>'''

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