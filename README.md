# BolSeva (बोलसेवा) - project files

- bolseva.html : the whole front end (single file). Rename to index.html for Vercel.
- server/      : FastAPI /ask endpoint (free Gemini key). See steps below.
- gen_audio.py, embed_audio.py : pre-recorded Marathi clips (income certificate only).
- BolSeva_Chat_Context.md : earlier project context (v1; catalogue now has 4 services).

## Run the AI endpoint (Windows)
cd server
pip install -r requirements.txt
set LLM_API_KEY=your_key_from_aistudio.google.com/apikey
uvicorn server:app --port 8000
Check http://localhost:8000/health, then in bolseva.html set
window.BOLSEVA_API="http://localhost:8000"

## Status
- All catalogue data is DRAFT (verified:false). Verify on the official Aaple Sarkar portal first.
- Without the server the page uses local rules (still works).
- Audio clips exist only for the income certificate; other documents use the browser voice.

## VS Code + venv (Windows)
1. File > Open Folder > C:\bolseva
2. Terminal > New Terminal, then: python -m venv .venv
3. Ctrl+Shift+P > "Python: Select Interpreter" > pick .venv
4. Open a NEW terminal (shows (.venv)). If PowerShell blocks activation, run once:
   Set-ExecutionPolicy -Scope CurrentUser RemoteSigned   (or use a cmd terminal: .venv\Scripts\activate)
5. pip install -r server/requirements.txt
6. PowerShell: $env:LLM_API_KEY="your_key"   | cmd: set LLM_API_KEY=your_key
7. cd server ; python -m uvicorn server:app --port 8000
Audio scripts need torch (large): use a second venv (.venv-audio) for them.
