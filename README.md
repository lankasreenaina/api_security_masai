# Weather Alert App

A secure weather lookup script for clinic patients.

## Setup

1. Clone the repo
2. Install dependencies: `pip install requests python-dotenv`
3. Copy `.env.example` to `.env` and add your real API key
4. Run: `python weather.py`

## Security Questions

**What are the real-world consequences of exposing an API key on GitHub?**
Exposed API keys can be scraped by bots within minutes of a commit. Attackers can exhaust your API quota, incur billing charges on paid tiers, access associated services, or use your key for malicious requests — all traced back to your account.

**Why does your company's privacy policy prohibit logging city names?**
City names reveal a user's location, which is personal data under GDPR and sensitive context under HIPAA. Logging it creates unnecessary data retention risk — if logs are breached, patient location history is exposed, violating the minimum necessary principle.