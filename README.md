# Jarvis

Persönlicher Sprachassistent (Web-App). Spracheingabe und -ausgabe laufen über den Browser, die Antworten kommen über einen eigenen Gemini-API-Key.

- `data.enc.json` enthält das Lagebild (Termine, Erinnerungen, Mails, Nachrichten) **nur verschlüsselt** (AES-256-GCM, PBKDF2). Ohne Passwort ist die Datei nutzlos.
- Passwort und API-Key werden nur im Browser des Geräts gespeichert, nie im Repository.
- `tools/encrypt.py` erzeugt die verschlüsselte Datei.
