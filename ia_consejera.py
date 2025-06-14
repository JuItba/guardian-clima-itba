import google.generativeai as genai

def obtener_consejo_ia_gemini(api_key_gemini, temperatura, condicion_clima, viento, humedad):
    """
    Usa Google Gemini para generar un consejo de vestimenta según el clima actual.
    """

    try:
        
        genai.configure(api_key=api_key_gemini)

        modelo = genai.GenerativeModel('gemini-pro')

        prompt = (
            f"Hola, soy un usuario de Guardián Clima ITBA. "
            f"El clima actual es:\n"
            f"- Temperatura: {temperatura}°C\n"
            f"- Condición: {condicion_clima}\n"
            f"- Viento: {viento} km/h\n"
            f"- Humedad: {humedad}%\n"
            f"¿Qué me recomiendas ponerme hoy para estar cómodo/a y preparado/a?"
        )

        print("\n Generando consejo de vestimenta con IA...")

        respuesta = modelo.generate_content(prompt)

        if respuesta.text:
            return respuesta.text.strip() 

        else:
            print("La IA no pudo generar un consejo.")
            return "No se pudo generar un consejo en este momento."

    except Exception as e:
        print(f"Error con la API de Gemini: {e}")
        return "Error al generar el consejo de IA."


# Bloque de prueba para ejecutar este archivo por separado (sirve para pruebas individuales)
if __name__ == "__main__":
    # API key 
    MI_API_KEY_GEMINI = "TU_API_KEY_AQUI"

    # Datos de ejemplo, no borrar hasta tenerlo conectado
    temp = 12
    condicion = "lluvia ligera"
    viento = 15
    humedad = 85

    consejo = obtener_consejo_ia_gemini(MI_API_KEY_GEMINI, temp, condicion, viento, humedad)
    
    print("\n Consejo de vestimenta:")
    print(consejo)
