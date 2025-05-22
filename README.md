# 🎙️ WebRTC Audio Recorder

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/status-em%20desenvolvimento-orange)]()

> Projeto simples de gravação de áudio via navegador com WebRTC, feito com Python, aiohttp e aiortc.

---

## 🚀 Demonstração

![image](https://github.com/user-attachments/assets/e06ace43-1975-4e89-a607-5aa33ee0f817)

---

## 🛠️ Tecnologias Utilizadas

- 🎧 **WebRTC** para captura de áudio via navegador
- 🐍 **Python** com:
  - `aiohttp`: servidor web assíncrono
  - `aiortc`: biblioteca WebRTC para Python
- 🎛️ HTML + JavaScript para frontend

---

## 📦 Instalação

```bash
# Clone o repositório
git clone git@github.com:seu-usuario/webrtc-audio-recorder.git
cd webrtc-audio-recorder

# Crie o ambiente virtual
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/Mac

# Instale as dependências
pip install -r requirements.txt
```
## ▶️ Como usar
- 1. Execute o Servidor:
    python app.py
- 2 Acesse no navegador:
    http://localhost:8080
- 3 Clique em "Iniciar Gravação" e depois em "Parar Gravação".
- 4 O arquivo .wav será salvo na pasta /recordings.

## 🧠 Aprendizados
Esse projeto serviu para explorar:
  . WebRTC na prática, com troca de oferta e resposta entre peer e servidor
  . Integração de frontend com backend em tempo real
  . Manipulação de áudio com MediaRecorder e track do aiortc
  
## 👨‍💻 Autor
### Silvano
