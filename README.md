# DL_Tarea_3
## Documentacion del entorno
Para ejecutar 'LLaMA', 'Phi' y 'Mistral' se utilizo un entorno de ejecucion con los siguientes componentes:
- **OS:** Pop! OS
- **CPU:** Intel Core i7-7500U 2.70 GHz
- **GPU:** Nvidia GeForce MX150
- **Memoria RAM:** 12 GB
- **Herramienta de ejecucion:** Ollama (Mas reciente)
- **Modelos utilizados:** 'llama3:8b', 'mistral:7b' y 'phi3:mini'


## Como usar

1. Instalar Ollama:
   ```bash
   curl -fsSL https://ollama.com/install.sh | sh
2. Iniciar Ollama:
   ```bash
   sudo systemctl start ollama
3. (Situacional) Verificar si esta iniciado Ollama:
   ```bash
   systemctl status ollama
   
4. (Situacional) En caso de que ollama no inicie bien (reiniciar):
   ```bash
   sudo systemctl stop ollama
   sudo pkill ollama
   sudo systemctl start ollama

5. Con Ollama iniciado, 'Pullear' los modelos:
   ```bash
   ollama pull llama3:8b
   ollama pull mistral:7b
   ollama pull phi3:mini

6. Activar un entorno virtual:
   ```bash
   source .venv/bin/activate

7. Instalar librerias en el entorno virtual (en caso de que no esten ya instaladas):
   ```bash
   pip install ollama pandas

8. Correr codigo:
   ```bash
   python src/generate_dataset.py
