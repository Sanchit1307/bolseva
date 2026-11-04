# BolSeva – Project Context (from chat session, 2026-11-03)

Paste this file at the start of a new chat to continue the project with full context.

## 1. Who and what
- User: first-year engineering student (AI & Data Science). Languages: Python, HTML, CSS, JS, C, C++. Works on **Windows**.
- Working preferences: direct answers, no flattery, code that works the first time without long explanations, evidence-backed answers for non-coding questions, work done step by step.
- Project: **BolSeva (बोलसेवा)** for the **Seva Innovation Challenge 2026**. A Marathi-first voice assistant that guides a citizen through the **Maharashtra income certificate (उत्पन्नाचा दाखला)** journey and produces a printable **Seva Card**.
- Source document: `BolSeva_Working_Prototype_Project_Plan.md` (5-week sprint; planned stack React + Vite frontend, Python FastAPI backend, JSON service catalogue; honesty rules: only verified content, clear "prototype / not tested with users" labelling, no fake claims).
- Special focus requested: **Marathi speech-to-text (STT) and text-to-speech (TTS)**, inclusive digital access.
- Frontend requirements: attractive, easy to navigate, professional company style, **no typical blue/violet palette**.

## 2. What was built (prototype v1)
Single self-contained file `bolseva.html` (published as an artifact: https://claude.ai/artifact/48fuy72LpCFECbcVnZQuTM).

**Flow:** Home (mic + typed input + suggested questions) → Confirm transcript ("मी योग्य समजलो का?": confirm / edit / speak again; low-confidence warning below 0.7) → Guide (steps, draft document checklist, sources, listen buttons, Seva Card).

**Features**
- STT: browser Web Speech API, `lang = mr-IN`, live interim transcript, error messages (mic permission, no speech, network, no mic), message when browser has no support. Works best in Chrome/Edge with internet.
- Scope guard: regex `IN_SCOPE` for income-certificate terms (Marathi and English "income"). Other requests (e.g. ration card) show an "unsupported, use official portal" panel.
- TTS: `speechSynthesis`, prefers any `mr-*` voice; falls back to a Hindi voice with an on-screen disclosure; otherwise tells the user no Marathi voice was found. Per-step 🔊 buttons, "सर्व ऐका", stop, speed (slow/normal), voice dropdown (आरोही / मनोहर), note that online voices need internet.
- Audio source dropdown "आवाज स्रोत": स्वयंचलित (auto) / पूर्व-रेकॉर्ड (pre-recorded) / ब्राउझर. `playList()` plays `AUDIO[key]` (embedded base64) or `audio/<key>.wav`, and falls back to browser TTS on failure. Keys: `title`, `step1`…`step6`, `warn`.
- Seva Card: built from the same catalogue data; print / save as PDF via `window.print()` with print CSS.
- Accessibility: large touch targets, aria-live status regions, focus management on view change, reduced-motion support.
- Design: maroon `#8A2232`, saffron `#E48A1B`, cream `#FBF6EE`, forest green for OK states, Noto Sans Devanagari + Inter; dark-mode tokens included; safe-area/mobile rules for the viewer.

## 3. Service catalogue (`SERVICE` object) – status: DRAFT
- Title: उत्पन्नाचा दाखला (उत्पन्न प्रमाणपत्र) / Income Certificate; `lastVerified: 2026-10-29`; reviewer: pending (second team member).
- Timeline: 15 days, from a district government page (Nandurbar) listing Right to Service Act timelines; to be rechecked on the portal.
- Steps (6): open Aaple Sarkar portal → register/login → choose "उत्पन्न प्रमाणपत्र" → fill form and attach documents → submit and keep application number → tahsil office verification; help at Aaple Sarkar / CSC centre.
- Document list (5, all badged "तपासणी बाकी"): ID proof; age proof; income proof (salary slip, ITR, employer certificate; 7/12 for farmers); residence proof / ration card; self-declaration if needed. These came from third-party sites that disagree slightly, so they are NOT verified.
- Portal URL used: `https://aaplesarkar.mahaonline.gov.in/en/CommonForm/ViewAllServices` (the plan had a typo, `mahaonline.mahaonline.gov.in`).
- Sources shown: official portal service list; Nandurbar district site (https://nandurbar.gov.in/?p=29359); WikiProcedure (secondary, for steps).
- **Must do before the jury sees it:** verify steps and documents on the official portal and update `SERVICE`, `lastVerified` and `reviewer`.

## 4. Voice findings
- Windows has no official Microsoft offline Marathi TTS voice, so the Windows voice route was not an option.
- **Verified by the user in Microsoft Edge:** `speechSynthesis.getVoices()` lists two online voices, `Microsoft आरोही Online (Natural) - Marathi (India)` and `Microsoft मनोहर Online (Natural) - Marathi (India)` (`lang: mr-IN`, `localService: false`). The user confirmed the Marathi voice works fine in Edge. Needs internet. Chrome and Firefox are not expected to have these voices.
- Not yet verified: how well Edge/Chrome STT recognises Marathi and mixed Marathi-English ("Income certificate काढायचं आहे").

## 5. Backup audio plan (to be done later by the user)
Options discussed: pre-generated clips; `facebook/mms-tts-mar` (open, CPU-friendly, believed non-commercial licence, to verify); `ai4bharat/indic-parler-tts` (better, heavier, licence to verify); Bhashini API (needs registration). Chosen route: pre-generated clips from MMS.

Files produced:
- `gen_audio.py`: generates `audio/title.wav`, `step1.wav`–`step6.wav`, `warn.wav` (numbers written as Marathi words).
- `embed_audio.py`: embeds the wavs into the page as base64, producing `bolseva_offline.html`.
- Steps: put files in `C:\bolseva` → `pip install torch transformers scipy` → `python gen_audio.py` → listen and fix lines → test locally by double-clicking `bolseva.html` and choosing "पूर्व-रेकॉर्ड" → `python embed_audio.py` → upload `bolseva_offline.html` to the chat for republishing.
- If catalogue text changes, update `gen_audio.py` and regenerate, otherwise audio will not match the screen.

## 6. Deployment (Vercel) – instructions given
- Rename `bolseva.html` to `index.html` in a folder; no build step needed (static site).
- Option A: GitHub repo → import in Vercel → Framework Preset "Other", no build command → Deploy. Option B: `npm install -g vercel`, `vercel login`, `vercel`, `vercel --prod`.
- After deploy: test on phone over https, allow mic, test in Edge, check the link works in a private window (turn off Deployment Protection if it asks for login).
- Submission honesty: use the real URL, label as prototype not yet tested with users, keep the "unverified" labels until the catalogue is verified, state that the Marathi voice works in Edge only until recorded audio is added.

## 7. Known limits
- Web Speech API STT needs internet and is browser-dependent; no audio is stored by BolSeva.
- Single HTML file, not yet the React/Vite + FastAPI structure from the plan.
- Only one service (income certificate); no eligibility checking, no form filling; no user testing done yet.
- Published artifact cannot read a local `audio/` folder; clips must be embedded.

## 8. Suggested next steps
1. Run the audio scripts and embed the clips (user will do this later).
2. Verify the catalogue against the official portal; get a second reviewer.
3. Test STT with 10–15 Marathi and mixed phrasings; record accuracy honestly.
4. Move to React/Vite + FastAPI with a `/tts` and `/stt` adapter (Bhashini or `faster-whisper`) and a test set for measuring speech quality.
5. Run usability tests with real users and only then update the "tested" claims.
