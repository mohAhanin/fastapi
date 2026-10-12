from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <body style="font-family: sans-serif; text-align: center; padding-top: 80px;">
            <h1>Hi 👋 I'm ready for the interview 🚀</h1>
            <p>This page is served by FastAPI.</p>
            <button onclick="sayHi()" style="padding:10px 20px; font-size:16px; cursor:pointer;">
                Click me
            </button>
            <p id="out" style="color: #444;"></p>
            <script>
                async function sayHi() {
                    const res = await fetch('/api/hello');
                    const data = await res.json();
                    document.getElementById('out').innerText = data.message;
                }
            </script>
        </body>
    </html>
    """

@app.get("/api/hello")
def api_hello():
    return {"message": "🎉 The backend says hi!"}