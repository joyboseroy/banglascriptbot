# BanglaScriptBot

**BanglaScriptBot** is a simple, open-source Bengali script learning app that helps users convert Banglish (phonetic Bengali written in English script) into proper Bengali script. It uses the `indic-transliteration` library for fast, lightweight transliteration and runs fully offline.

## Features

- Converts phonetic Bengali like `ami tomar sathe jete chai` into `আমি তোমার সাথে যেতে চাই`
- Uses `indic-transliteration` – no need for large models or internet access
- Built with Streamlit – clean and fast UI
- Ideal for learners who speak Bengali but want to improve reading and writing

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/banglascriptbot.git
cd banglascriptbot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
streamlit run app.py
```

Then open `http://localhost:8501` in your browser.

## How It Works

The app uses `indic-transliteration` to convert ITRANS-style phonetic Bengali (e.g. `ami`, `tomar`, `sathe`) into native Bengali script. It's a perfect tool for brushing up on Bengali writing if you're already fluent in speaking.

## Project Structure

| File | Description |
|------|-------------|
| `app.py` | Streamlit app code |
| `requirements.txt` | Python package dependencies |
| `README.md` | This file |
| `LICENSE` | MIT License |

## License

This project is licensed under the MIT License. See `LICENSE` for details.

---

Make Bengali script learning easier.
