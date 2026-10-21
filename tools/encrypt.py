#!/usr/bin/env python3
"""Verschlüsselt das Jarvis-Lagebild für die Sprach-App.

Aufruf:  JARVIS_PASS='…' python3 tools/encrypt.py briefing.json data.enc.json
Format:  AES-256-GCM, Schlüssel per PBKDF2-SHA256 (250.000 Runden) aus dem Passwort.
Das Passwort steht nie im Repository.
"""
import base64, json, os, sys, datetime
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

ITER = 250_000

def main():
    src, dst = sys.argv[1], sys.argv[2]
    pw = os.environ.get("JARVIS_PASS")
    if not pw:
        sys.exit("JARVIS_PASS fehlt")
    plain = open(src, "rb").read()
    json.loads(plain)  # muss gültiges JSON sein
    salt, iv = os.urandom(16), os.urandom(12)
    key = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=ITER).derive(pw.encode())
    ct = AESGCM(key).encrypt(iv, plain, None)
    b64 = lambda b: base64.b64encode(b).decode()
    out = {"v": 1, "iter": ITER, "salt": b64(salt), "iv": b64(iv), "ct": b64(ct),
           "written": datetime.datetime.now(datetime.timezone.utc).isoformat()}
    json.dump(out, open(dst, "w"))
    print(f"ok {len(plain)} B -> {dst}")

if __name__ == "__main__":
    main()
