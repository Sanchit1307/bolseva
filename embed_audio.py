# embed_audio.py - puts audio/*.wav inside the page -> bolseva_offline.html (single file)
import base64, json, pathlib
here = pathlib.Path(__file__).parent
keys = ["title", "step1", "step2", "step3", "step4", "step5", "step6", "warn"]
audio = {}
for k in keys:
    f = here / "audio" / f"{k}.wav"
    if f.exists():
        audio[k] = "data:audio/wav;base64," + base64.b64encode(f.read_bytes()).decode()
    else:
        print("missing:", f)
html = (here / "bolseva.html").read_text(encoding="utf-8")
assert "const AUDIO={};" in html, "bolseva.html already has audio embedded or is the wrong file"
html = html.replace("const AUDIO={};", "const AUDIO=" + json.dumps(audio) + ";")
(here / "bolseva_offline.html").write_text(html, encoding="utf-8")
print("done:", len(html) // 1024, "KB,", len(audio), "clips")
