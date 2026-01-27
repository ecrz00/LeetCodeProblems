import os
import subprocess
import re

def renameLeetcodeFiles():
    # Extensiones a procesar
    extension = ".py"
    
    # Recorrer todas las carpetas y subcarpetas
    for root, dirs, files in os.walk("."):
        for filename in files:
            if filename.endswith(extension) and filename != os.path.basename(__file__):
                # Buscar el número al inicio del archivo (ej: 1.TwoSum.py o 1. TwoSum.py)
                match = re.match(r'^(\d+)\.(.*)', filename)
                
                if match:
                    num_str = match.group(1)
                    rest_of_name = match.group(2)
                    
                    # Rellenar con ceros hasta tener 4 dígitos
                    new_num_str = num_str.zfill(4)
                    new_filename = f"{new_num_str}.{rest_of_name}"
                    
                    old_path = os.path.join(root, filename)
                    new_path = os.path.join(root, new_filename)
                    
                    if old_path != new_path:
                        print(f"Renombrando: {filename} -> {new_filename}")
                        # Usamos git mv para no perder el historial
                        subprocess.run(["git", "mv", old_path, new_path])

if __name__ == "__main__":
    renameLeetcodeFiles()