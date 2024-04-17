import re

def convert_srt_to_ttml(srt_file_path, ttml_file_path):
    # Lire le fichier SRT
    with open(srt_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Créer le fichier TTML. Pour le style, on a choisi un style quelconque. Après peut être, il faudra choisir un style plus adapté
    with open(ttml_file_path, 'w', encoding='utf-8') as file:
        file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        file.write('<tt xmlns="http://www.w3.org/ns/ttml" xml:lang="en">\n')
        file.write('  <head>\n')
        file.write('    <styling>\n')
        file.write('      <style xml:id="1" tts:fontFamily="Arial" tts:fontSize="20px" tts:color="white" tts:backgroundColor="black" tts:textAlign="center"/>\n')
        file.write('    </styling>\n')
        file.write('  </head>\n')
        file.write('  <body>\n')
        file.write('    <div>\n')

        # Process: chaque ligne doit être créé en s'adaptant au format du fichier ttml
        for line in lines:
            if '-->' in line:
                # Convertir les temps
                times = line.strip().split(' --> ')
                start = times[0].replace(',', '.')
                end = times[1].replace(',', '.')
                text = next((l for l in lines[lines.index(line)+1:] if l.strip()), '').strip()
                file.write(f'      <p begin="{start}" end="{end}" style="1">{text}</p>\n')

        file.write('    </div>\n')
        file.write('  </body>\n')
        file.write('</tt>\n')

# Chemins des fichiers
srt_path = ''  # Chemin vers le fichier SRT source à spécifier
ttml_path = ''  # Chemin vers le fichier TTML de sortie à spécifier

# Appel de la fonction de conversion
convert_srt_to_ttml(srt_path, ttml_path)
