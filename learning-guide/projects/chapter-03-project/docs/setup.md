# Chapter 3 Project Setup Guide

## Prerequisites

- Python 3.9 or higher
- OpenAI API key (or Ollama installed)
- Basic terminal/command line knowledge

## Step-by-Step Setup

### 1. Create Virtual Environment

```bash
# Navigate to project directory
cd chapter-03-project

# Create virtual environment
python3 -m venv venv

# Activate (macOS/Linux)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up API Key

Create a `.env` file in the project root:

```bash
# .env file
OPENAI_API_KEY=your_api_key_here
```

**Important**: Never commit the `.env` file to Git! It's already in `.gitignore`.

### 4. Verify Setup

```bash
# Run the starter code
python starter-code/main.py

# Or run the solution
python solution/chatbot.py
```

## Project Structure

```
chapter-03-project/
├── .env                    # Your API key (not committed)
├── .gitignore             # Protects secrets
├── requirements.txt       # Dependencies
├── README.md              # Project instructions
├── starter-code/          # Your starting point
│   └── main.py
├── solution/              # Complete solution
│   └── chatbot.py
├── tests/                 # Test files
│   └── test_chatbot.py
└── docs/                  # Documentation
    └── setup.md
```

## Common Issues

### "OPENAI_API_KEY not found"
- Make sure `.env` file exists in project root
- Check that variable name is exactly `OPENAI_API_KEY`
- Verify `python-dotenv` is installed

### "Module not found"
- Activate virtual environment
- Run `pip install -r requirements.txt`

### Virtual environment not activating
- Use full path: `source /path/to/venv/bin/activate`
- Check Python version: `python3 --version`

## Next Steps

1. Complete the starter code
2. Test your implementation
3. Try the extension ideas
4. Review the solution (after trying yourself!)
