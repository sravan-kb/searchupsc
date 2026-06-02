# UPSC PYQ Search

**Connect with me:** [LinkedIn](https://www.linkedin.com/in/sravan-branwal) • [GitHub](https://github.com/sravan-kb)

A searchable database of UPSC Previous Year Questions created from UPSC PDFs using OCR, PostgreSQL (Supabase), and FastAPI.

🔗 **Live:** [searchupsc.onrender.com](https://searchupsc.onrender.com)

---

## Architecture

UPSC PDF
↓
Tesseract OCR
↓
Question Extraction & Cleaning
↓
CSV Dataset
↓
PostgreSQL (Supabase)
↓
FastAPI Search Engine
↓
Render Deployment

## Features

- Keyword-based search across PYQs
- Highlights matching keywords in results
- Fast and lightweight — no JS frameworks

## Tech Stack

- Python
- FastAPI
- PostgreSQL (Supabase)
- SQLAlchemy
- Tesseract OCR
- Deployed on Render

## Current Dataset

- ~300 searchable questions

- UPSC Prelims 2026 (Paper 1)
- UPSC Prelims 2025 (Paper 1)
- UPSC Prelims 2024 (Paper 1)

## Known Issues

- Questions with tables (e.g. match the following) lose their formatting after OCR — they appear as plain text which is hard to read. This needs to be fixed.

Feel free to open an issue or reach out directly on [LinkedIn](https://www.linkedin.com/in/sravan-branwal)

## Future Improvements

- Add older PYQs (2023, 2022, ...)
- Mains questions
- Subject and year filters
- PostgreSQL Full-Text Search (tsvector)
- Semantic search using embeddings
- Similar question discovery
- Better OCR handling for tables

## My Story

I spent 8 years preparing for UPSC. During that time I often struggled to search through previous year questions quickly, so I built the tool I always wished existed.

I am currently pursuing Big Data Analytics from CDAC and actively looking for a job opportunity. If you think I can contribute to your team, please reach out.

📩 [LinkedIn](https://www.linkedin.com/in/sravan-branwal) • [GitHub](https://github.com/sravan-kb)

---

Built by someone who walked this road for 8 years.
