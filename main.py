from flask import Flask, render_template, request
import re

app = Flask(__name__)


# Function to load SQL injection cheat sheet file
def load_cheat_sheet(file_path):
    cheat_sheet = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            cheat_sheet = [line.strip() for line in f]
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except UnicodeDecodeError:
        print(f"Error: Unable to decode file '{file_path}' using UTF-8 encoding.")
    except Exception as e:
        print(f"An error occurred while loading cheat sheet file: {e}")
    return cheat_sheet


# Function to check for SQL injection
def check_sql_injection(input_str, cheat_sheet):
    client_ip = request.remote_addr  # Get client IP address

    # Check if SQL injection patterns exist
    if not cheat_sheet:
        return False

    # Search input string against cheat sheet patterns
    for pattern in cheat_sheet:
        if re.search(pattern, input_str, re.IGNORECASE):
            return True
    return False


def normalize_query(query):
    normalized_query = query.strip()
    normalized_query = re.sub(r'\s+', ' ', normalized_query)
    return normalized_query


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']

    # Normalize the query
    normalized_query = normalize_query(query)

    # Load SQL injection cheat sheet
    cheat_sheet_file = 'static/cheat_sheet.txt'
    cheat_sheet = load_cheat_sheet(cheat_sheet_file)

    # Check for SQL injection
    if check_sql_injection(normalized_query, cheat_sheet):
        return "SQL Injection detected! Your IP address has been blocked."
    else:
        message = f'Searching for: {query}'

    return render_template('result.html', message=message)


if __name__ == '__main__':
    app.run(debug=True)
