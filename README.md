# DL_Tarea_3
## Documentacion del entorno
Para ejecutar 'LLaMA', 'Phi' y 'Mistral' se utilizo un entorno de ejecucion con los siguientes componentes:
- **OS:** Pop! OS
- **CPU:** Intel Core i7-7500U 2.70 GHz
- **GPU:** Nvidia GeForce MX150
- **Memoria RAM:** 12 GB
- **Herramienta de ejecucion:** Ollama (Mas reciente)
- **Modelos utilizados:** 'llama3:8b', 'mistral:7b' y 'phi3:mini'

## Prompts a utilizar
Para poder comparar fielmente estos tres modelos, se da la opcion de utilizar 1 de los siguientes 'prompts' cada vez que se ejecute el codigo (debido a la lentitud por usar un hardware "poco potente" se decidio mostrar lo que iba generando cada modelo en tiempo real):

1. 'Reseñas de Notion'

[INSTRUCCION]

Genera exactamente 10 ejemplos de reseñas de usuarios sobre la aplicacion de productividad 'Notion' en idioma Español.

[REQUISITOS]

- Cubrir problemas de UI/UX, bugs y rendimiento de forma balanceada.
- Formato: Devuelve UNICAMENTE un arreglo JSON valido, sin texto introductorio ni conclusorio ni bloques markdown.

[EJEMPLO]

[{"id": 1, "app": "Notion", "review": "Se cierra inesperadamente.", "feeling": "Negativo", "category": "Bugs"}]

2. 'Comentarios en Redes Sociales - Nuevo tipo de Brisket'

[INSTRUCCION]

Genera exactamente 10 comentarios simulados de redes sociales (Twitter, Facebook o Instagram) sobre el descrubrimiento de una nueva variedad de brisket en idioma Español

[REQUISITOS]

- Los comentarios deben reflejar altas expectativas (Positivo), decepcion (Negativo) o indiferencia (Neutral).
- Formato: Devuelve UNICAMENTE un arreglo JSON valido, sin textos extra.

[EJEMPLO]

[{"id": 1, "platform": "Twitter", "text": "Este nuevo brisket se ve jugoso y sabroso.", "feeling": "Positivo", "topic": "Textura"}]

3. 'Preguntas Frecuentes - Plataforma Venta de Brisket'

[INSTRUCCION]

Genera exactamente 10 preguntas frecuentes (FAQ) simuladas para el soporte tecnico de una plataforma de venta de brisket(carne) en idioma Español.

[REQUISITOS]

- Deben cubrir problemas de acceso, pagos y que variedad de productos se posee.
- Formato: Devuelve UNICAMENTE un arreglo JSON valido, sin textos de introduccion o cierre.

[EJEMPLO]

[{"id": 1, "area": "Soporte", "question": "¿Como recupero mi contraseña?", "category": "Acceso"}]

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
