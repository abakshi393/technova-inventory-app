from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
     return """
    <html>
        <head>
            <title>TechNova Inventory System</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    color: #333;
                    text-align: center;
                    margin: 0;
                    padding: 0;
                }
                h1 {
                    color: #008CBA;
                    font-size: 3em;
                    margin-top: 50px;
                }
                .content {
                    max-width: 800px;
                    margin: 50px auto;
                    padding: 20px;
                    background-color: white;
                    border-radius: 10px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                }
                p {
                    font-size: 1.2em;
                }
                .footer {
                    margin-top: 30px;
                    font-size: 0.8em;
                    color: #777;
                }
            </style>
        </head>
        <body>
            <div class="content">
                <h1>Welcome to TechNova Inventory System!</h1>
                <p>Your one-stop solution for managing your inventory efficiently and effectively.</p>
            </div>
            <div class="footer">
                <p>&copy; 2025 TechNova. All rights reserved.</p>
            </div>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
