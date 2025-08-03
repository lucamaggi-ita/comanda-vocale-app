
import speech_recognition as sr
from datetime import datetime
import os
import re

print("🎙️ Comanda vocale – Premi INVIO per iniziare")
input()

# Avvia microfono
recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("🗣️ Parla ora...")
    audio = recognizer.listen(source)

try:
    testo = recognizer.recognize_google(audio, language="pt-BR")
    print(f"✅ Riconosciuto: {testo}")
except sr.UnknownValueError:
    print("❌ Audio non riconosciuto.")
    exit()
except sr.RequestError as e:
    print(f"❌ Errore: {e}")
    exit()

# Determina il reparto
reparti = ['bar', 'ristorante', 'pizzeria']
reparto = None
for r in reparti:
    if r in testo.lower():
        reparto = r
        break

if not reparto:
    print("❗ Reparto non specificato nel messaggio. Inserire bar, ristorante o pizzeria.")
    exit()

# Estrae numero tavolo (es. 'tavolo A5' o 'mesa 12')
match_tavolo = re.search(r'(tavolo|mesa)\s*([A-Za-z0-9]+)', testo.lower())
if match_tavolo:
    tavolo = match_tavolo.group(2).upper()
else:
    tavolo = "Sconosciuto"

# Rimuove parte 'tavolo' e 'reparto' dal testo per lasciare solo la comanda
testo_pulito = re.sub(r'(tavolo|mesa)\s*[A-Za-z0-9]+\s*', '', testo, flags=re.IGNORECASE)
testo_pulito = re.sub(r'(bar|ristorante|pizzeria):?', '', testo_pulito, flags=re.IGNORECASE).strip()

# Orario e nome file
orario = datetime.now().strftime("%H:%M")
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_dir = os.path.join("/storage/emulated/0/comande", reparto)
os.makedirs(output_dir, exist_ok=True)

filename_base = f"{tavolo}_{timestamp}"
file_path = os.path.join(output_dir, f"{filename_base}.txt")

# Contenuto della comanda
txt_content = f"""
********* COMANDA *********
TAVOLO: {tavolo}
REPARTO: {reparto.upper()}
ORARIO: {orario}
---------------------------
{testo_pulito}
***************************
"""

# Salva il file
with open(file_path, "w", encoding="utf-8") as f:
    f.write(txt_content)

print(f"📂 Comanda salvata in: {file_path}")
print("👉 Puoi stamparla usando un'app come RawBT o collegando il cellulare in rete.")
