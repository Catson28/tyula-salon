import os
import subprocess

apps_names = ['product', 'category', 'subcategory', 'service', 'professional', 'sale', 'image', 'customer', 'authentication', 'users']  # Lista de nomes de aplicativos

# Diretório onde o script está localizado
diretorio_script = os.path.dirname(os.path.abspath(__file__))
print(diretorio_script)

# Diretório onde o projeto Django está localizado
# diretorio_projeto = os.path.dirname(diretorio_script)
diretorio_projeto = diretorio_script
print(diretorio_projeto)

# Diretório onde a pasta "apps" será criada
diretorio_apps = os.path.join(diretorio_projeto, 'apps')

# Cria a pasta "apps" se não existir
if not os.path.exists(diretorio_apps):
    os.mkdir(diretorio_apps)

# Navega para o diretório "apps" para criar os aplicativos dentro dela
os.chdir(diretorio_apps)

# Cria os aplicativos
for app_name in apps_names:
    subprocess.run(['python', '../manage.py', 'startapp', app_name])