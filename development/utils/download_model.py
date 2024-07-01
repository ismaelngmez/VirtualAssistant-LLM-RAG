import os

def download_files_with_extensions(url, extensions, download_dir):
    # Construir la expresión regular para incluir solo archivos con las extensiones especificadas
    include_regex = "|".join(f".*\\.{ext}$" for ext in extensions)
    # Construir el comando wget con sudo, la expresión regular de inclusión y el directorio de descarga
    command = f"wget -r -np -nd -P '{download_dir}' -A '{include_regex}' {url}"
    # Ejecutar el comando con sudo
    os.system(command)