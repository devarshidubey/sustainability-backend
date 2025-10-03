# Sustainability Project

This project provides a React frontend and Flask backend to calculate sustainability scores, track history, and provide AI-based suggestions.

---

## Problem Statement

While building the scoring system, I noticed a **unit mismatch issue** between **GWP circularity** and **cost**. To normalize these parameters:

- Maximum GWP: `23700`
- Maximum cost: `100000 Rs`

These values were used to scale the inputs to the score function.
This is still far from ideal since changes in gwp wouldn't account much for affecting the overall score much (since it's normalized by a very large value). To change this we can use some practically viable max_value like 2000.

---

## Features

- `/score` – Calculate sustainability score
- `/history` – Retrieve previous score history
- `/score-summary` – Summarized view of scores
- Simple unit tests written to test the **score API**
- AI suggestions are **hardcoded** in the frontend due to OpenAI API key exhaustion; recruiters can review the code for integrating a working AI engine by using their OpenAI api keys.

---

## Backend API Base URL
https://sustainability-backend-production.up.railway.app/

Available endpoints: `/score`, `/history`, `/score-summary`

---

## Frontend Deployment

The React frontend is deployed on **Vercel**:
https://sustainability-frontend-jkd4ihah6-devarshis-projects-f7fd52ef.vercel.app

---

## Running Locally

1. **Clone the repository**

```bash
git clone <repo-url>
cd <repo-folder>
```
2. **Backend setup (Flask)**
```
cd backend
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

4. **Set environment variables**
Create a .env file (do not commit this file)

Add keys like:
```
OPENAI_API_KEY=your_openai_key
DATABASE_URL=<optional_database_url>
```
4. **Run the Flask server**
```
flask run
```
## Testing

Unit tests for the score API can be run using:
```
pytest tests/test_score.py -v
```
