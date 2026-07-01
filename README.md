# DL_Tarea_3

## Requisitos Previos

1. Tener instalado Ollama:
   ```bash
   curl -fsSL https://ollama.com/install.sh | sh
2. Iniciar Ollama:
   ```bash
   sudo systemctl start ollama
3. (Situacional) Verificar si esta iniciado Ollama:
   ```bash
   systemctl status ollama

4. Con Ollama iniciado, 'Pullear' los modelos:
   ```bash
   ollama pull llama3:8b
   ollama pull mistral:7b
   ollama pull phi3:mini

5. Activar un entorno virtual:
   ```bash
   source .venv/bin/activate

6. Instalar librerias en el entorno virtual (en caso de que no esten ya instaladas):
   ```bash
   pip install ollama pandas

6. Correr codigo:
   ```bash
   python src/generate_dataset.py
