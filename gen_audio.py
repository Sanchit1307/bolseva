# gen_audio.py - makes the Marathi clips into the audio/ folder (run once)
import os, torch, scipy.io.wavfile as w
from transformers import VitsModel, AutoTokenizer

os.makedirs("audio", exist_ok=True)
tok = AutoTokenizer.from_pretrained("facebook/mms-tts-mar")
model = VitsModel.from_pretrained("facebook/mms-tts-mar")

lines = {
    "title": "उत्पन्नाचा दाखला",
    "step1": "पायरी एक. आपले सरकार पोर्टल उघडा.",
    "step2": "पायरी दोन. नवीन वापरकर्ता असल्यास नोंदणी करा; नंतर लॉगिन करा.",
    "step3": "पायरी तीन. सेवा यादीतून उत्पन्न प्रमाणपत्र निवडा.",
    "step4": "पायरी चार. अर्ज भरा आणि आवश्यक कागदपत्रे जोडा.",
    "step5": "पायरी पाच. अर्ज जमा करा आणि अर्ज क्रमांक सुरक्षित ठेवा.",
    "step6": "पायरी सहा. तहसील कार्यालयाकडून तपासणी होते. मदत हवी असल्यास जवळच्या सेवा केंद्रात जा.",
    "warn": "कागदपत्रांची यादी मसुदा आहे. अर्ज करण्यापूर्वी अधिकृत संकेतस्थळावर तपासा.",
}
for name, text in lines.items():
    with torch.no_grad():
        wav = model(**tok(text, return_tensors="pt")).waveform[0]
    w.write(f"audio/{name}.wav", model.config.sampling_rate, wav.numpy())
    print("saved", name)
