import os
import sys
import ollama

MODELS = ['llama3:8b', 'mistral:7b', 'phi3:mini']
OUTPUT_DIR = "data/raw"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# --- PROMPTS ---
PROMPTS = {
    "1": """[INSTRUCCION]
Genera exactamente 10 ejemplos de reseñas de usuarios sobre la aplicacion de productividad 'Notion' en idioma Español.
[REQUISITOS]
- Cubrir problemas de UI/UX, bugs y rendimiento de forma balanceada.
- Formato: Devuelve UNICAMENTE un arreglo JSON valido, sin texto introductorio ni conclusorio ni bloques markdown.
[EJEMPLO]
[{"id": 1, "app": "Notion", "review": "Se cierra inesperadamente.", "feeling": "Negativo", "category": "Bugs"}]""",

    "2": """[INSTRUCCION]
Genera exactamente 10 comentarios simulados de redes sociales (Twitter, Facebook o Instagram) sobre el descrubrimiento de una nueva variedad de brisket en idioma Español.
[REQUISITOS]
- Los comentarios deben reflejar altas expectativas (Positivo), decepcion (Negativo) o indiferencia (Neutral).
- Formato: Devuelve UNICAMENTE un arreglo JSON valido, sin textos extra.
[EJEMPLO]
[{"id": 1, "platform": "Twitter", "text": "Este nuevo brisket se ve jugoso y sabroso.", "feeling": "Positivo", "topic": "Textura"}]""",

    "3": """[INSTRUCCION]
Genera exactamente 10 preguntas frecuentes (FAQ) simuladas para el soporte tecnico de una plataforma de venta de brisket(carne) en idioma Español.
[REQUISITOS]
- Deben cubrir problemas de acceso, pagos y que variedad de productos se posee.
- Formato: Devuelve UNICAMENTE un arreglo JSON valido, sin textos de introduccion o cierre.
[EJEMPLO]
[{"id": 1, "area": "Soporte", "question": "¿Como recupero mi contraseña?", "category": "Acceso"}]"""
}

def mostrar_menu():
    print("==================================================")
    print("       MENU DE GENERACION DE DATOS SINTETICOS     ")
    print("==================================================")
    print("Selecciona el topico y prompt que deseas evaluar:\n")
    print("[1] Reseñas de 'Notion' (JSON)")
    print("[2] Comentarios de Redes Sociales - Nuevo tipo de Brisket (JSON)")
    print("[3] Preguntas Frecuentes - Plataforma Venta de Brisket (JSON)")
    print("==================================================")
    
    while True:
        eleccion = input("Introduce el numero de tu eleccion (1, 2 o 3): ").strip()
        if eleccion in PROMPTS:
            return eleccion
        print("Opcion no valida. Por favor, ingresa 1, 2 o 3.\n")

def generate_synthetic_data():
    # Usuario elige el prompt
    id_prompt = mostrar_menu()
    prompt_seleccionado = PROMPTS[id_prompt]
    
    print(f"\nIniciando generacion usando el Prompt #{id_prompt}...")
    
    for model in MODELS:
        print(f"\n{'='*30}")
        print(f"[+] Solicitando datos al modelo: {model}")
        print(f"{'='*30}\n")
        
        raw_response_text = ""
        try:
            response_stream = ollama.generate(model=model, prompt=prompt_seleccionado, stream=True)
            
            print(f"--- [Inicio de respuesta en tiempo real de {model}] ---")
            for chunk in response_stream:
                token = chunk['response']
                raw_response_text += token
                sys.stdout.write(token)
                sys.stdout.flush()
                
            print(f"\n\n--- [Fin de respuesta de {model}] ---")
            
            # El nombre del archivo incluye el ID del prompt usado
            model_clean = model.replace(':', '_')
            filename = os.path.join(OUTPUT_DIR, f"raw_prompt{id_prompt}_{model_clean}.txt")
            
            with open(filename, "w", encoding="utf-8") as f:
                f.write(raw_response_text.strip())
                
            print(f"\nArchivo guardado: {filename}")
            
        except Exception as e:
            print(f"\nError critico al procesar el modelo {model}: {e}")

if __name__ == "__main__":
    generate_synthetic_data()
