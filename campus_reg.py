import os
import gtts
import pygame
import time



def clear():
  """
  Función que limpia la terminal.
  """
  if os.name == 'nt':  # Windows
    os.system('cls')
  else:  # Linux, macOS
    os.system('clear')



def leer_en_voz_alta(texto, idioma="es", velocidad=0.15):
  """
  Función que lee texto en voz alta utilizando gtts.

  Argumentos:
    texto: Texto a leer.
    idioma: Idioma del texto (por defecto español).
    velocidad: Velocidad de habla (entre 0.1 y 1).
  """
  # Crear instancia de gTTS
  locutor = gtts.gTTS(text=texto, lang=idioma, slow=velocidad)

  # Guardar audio a un archivo MP3
  nombre_archivo = "leer_en_voz_alta.mp3"
  locutor.save(nombre_archivo)
  reproducir_sonido(nombre_archivo)

  # Reproducir el archivo MP3 (asumiendo que se tiene un reproductor de audio instalado)
  # ...
  print(f"Reproduciendo archivo: {nombre_archivo}")




def reproducir_sonido(ruta_archivo):
  pygame.mixer.init()

  # Carga el archivo de sonido
  sonido = pygame.mixer.Sound(ruta_archivo)

  # Reproduce el sonido
  sonido.play()

  # Espera a que termine de reproducirse
  time.sleep(sonido.get_length())

  # Limpia
  pygame.mixer.quit()


def main():
  leer_en_voz_alta("hola buenas tardes")
  clear()



if __name__ == "__main__":
  main()


