import os
import re

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from sqlalchemy import create_engine, text

# Create FastAPI app
app = FastAPI()

# PostgreSQL connection
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:projectdata@localhost:5432/upsc_questions"
)

# Create database engine
engine = create_engine(DATABASE_URL)


# HOME PAGE
@app.get("/", response_class=HTMLResponse)
def home():

    return """
    <html>

    <head>

        <title>UPSC PYQ Search Engine</title>

        <style>

            body {
                font-family: Arial;
                background-color: #f5f5f5;
                text-align: center;
                margin-top: 100px;
            }

            h1 {
                color: darkblue;
                margin-bottom: 10px;
            }

            .tagline {
                color: gray;
                margin-bottom: 40px;
                font-size: 18px;
            }

            input {
                width: 600px;
                padding: 14px;
                font-size: 18px;
                border-radius: 10px;
                border: 1px solid #ccc;
            }

            button {
                padding: 14px 22px;
                font-size: 18px;
                border-radius: 10px;
                border: none;
                background-color: darkblue;
                color: white;
                cursor: pointer;
                margin-left: 10px;
            }

            button:hover {
                background-color: navy;
            }

            .footer-text {
                margin-top: 80px;
                color: gray;
                font-size: 18px;
            }

            .social-bar {
                position: fixed;
                top: 20px;
                right: 30px;
                display: flex;
                gap: 12px;
                align-items: center;
            }

            .social-bar a {
                display: flex;
                align-items: center;
                gap: 7px;
                text-decoration: none;
                color: white;
                font-size: 15px;
                font-weight: bold;
                padding: 9px 16px;
                border-radius: 8px;
                background-color: darkblue;
                box-shadow: 0 2px 8px rgba(0,0,0,0.2);
                transition: background-color 0.2s, box-shadow 0.2s;
            }

            .social-bar a:hover {
                background-color: navy;
                box-shadow: 0 4px 14px rgba(0,0,0,0.3);
            }

            .social-bar img {
                width: 18px;
                height: 18px;
                filter: brightness(0) invert(1);
            }

        </style>

    </head>

    <body>

        <div class="social-bar">
            <a href="https://www.linkedin.com/in/sravan-branwal" target="_blank">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg" alt="LinkedIn">
                LinkedIn
            </a>
            <a href="https://github.com/sravan-kb" target="_blank">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" alt="GitHub">
                GitHub
            </a>
        </div>

        <h1>UPSC PYQ Search</h1>

        <p class="tagline">
            Search UPSC Previous Year Questions instantly
            <br>
            <span>Starting with Prelims Paper-1 — Mains on the way 🚀</span>
        </p>

        <form action="/search" method="get">

            <input
                type="text"
                name="q"
                placeholder="Search UPSC keywords..."
            >

            <button type="submit">
                Search
            </button>

        </form>

        <p class="footer-text">
            With 💖 for ALL the Aspirants
        </p>

    </body>

    </html>
    """


# SEARCH PAGE
@app.get("/search", response_class=HTMLResponse)
def search_questions(q: str):

    # Split search query into words
    words = q.split()

    # Common stop words
    stop_words = {
        "the",
        "is",
        "of",
        "and",
        "a",
        "an",
        "what",
        "which",
        "in",
        "on",
        "to",
        "for",
        "consider"
    }

    # Remove stop words
    words = [
        word
        for word in words
        if word.lower() not in stop_words
    ]

    # If all words removed
    if len(words) == 0:

        return """
        <h2>Please enter meaningful keywords.</h2>
        """

    # Store SQL conditions
    conditions = []

    # Store SQL parameters
    params = {}

    # Build SQL conditions
    for i, word in enumerate(words):

        conditions.append(
            f"full_text ILIKE :word{i}"
        )

        params[f"word{i}"] = f"%{word}%"

    # Join conditions with OR
    where_clause = " OR ".join(conditions)

    # Build relevance score
    score_parts = []

    for i, word in enumerate(words):

        score_parts.append(
            f"""
            CASE
                WHEN full_text ILIKE :word{i}
                THEN 1
                ELSE 0
            END
            """
        )

    score_sql = " + ".join(score_parts)

    # SQL query
    sql = f"""
        SELECT
            year,
            question_number,
            full_text,
            ({score_sql}) AS score

        FROM questions

        WHERE {where_clause}

        ORDER BY
            score DESC,
            question_number ASC

        LIMIT 20
    """

    query = text(sql)

    # Execute query
    with engine.connect() as connection:

        results = connection.execute(query, params)

        rows = results.fetchall()

    # Build HTML response
    html = f"""
    <html>

    <head>

        <title>Search Results</title>

        <style>

            body {{
                font-family: Arial;
                margin: 40px;
                line-height: 1.8;
                background-color: #f5f5f5;
            }}

            h1 {{
                color: darkblue;
                margin-bottom: 30px;
            }}

            .question {{
                background-color: white;
                margin-bottom: 40px;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            }}

            h2 {{
                color: darkblue;
            }}

            .score {{
                color: green;
                font-weight: bold;
                margin-bottom: 10px;
            }}

            a {{
                text-decoration: none;
                color: darkblue;
                font-weight: bold;
            }}

            mark {{
                background-color: yellow;
                padding: 2px;
            }}

        </style>

    </head>

    <body>

        <a href="/">← Back to Search</a>

        <h1>Search Results for: "{q}"</h1>
    """

    # Add search results
    for row in rows:

        question_text = row.full_text

        # Highlight search words
        for word in words:

            pattern = re.compile(
                re.escape(word),
                re.IGNORECASE
            )

            question_text = pattern.sub(
                lambda match:
                f"<mark>{match.group(0)}</mark>",
                question_text
            )

        # Convert line breaks
        question_text = question_text.replace(
            "\n",
            "<br>"
        )

        html += f"""
        <div class="question">

            <h2>
                {row.year} • Question {row.question_number}
            </h2>

            <div class="score">
                Match Score: {row.score}
            </div>

            <p>{question_text}</p>

        </div>
        """

    # No results case
    if len(rows) == 0:

        html += """
        <h2>No matching questions found.</h2>
        """

    html += """
    </body>
    </html>
    """

    return html