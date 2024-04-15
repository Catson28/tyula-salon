```bash
.env\Scripts\activate
```

alterar a variavel de ambiente

C:\Catson\Projectos\Clonado\tyula-salon\backend\env\Scripts\activate



Para resolver o erro de execução de scripts no PowerShell ao tentar ativar o ambiente virtual do Python usando o script `activate.ps1`, você pode tentar o seguinte:

1. **Abra o PowerShell como administrador:**
   Clique com o botão direito do mouse no ícone do PowerShell e selecione "Executar como administrador". Isso pode ser necessário para realizar alterações na política de execução de scripts.

2. **Defina a política de execução de scripts para `Bypass`:**
   Execute o seguinte comando para temporariamente permitir a execução de scripts:
   ```powershell
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   ```

3. **Ative o ambiente virtual:**
   Após definir a política de execução de scripts para `Bypass`, tente novamente ativar o ambiente virtual do Python usando o comando:
   ```powershell
   .\env\Scripts\Activate.ps1
   ```

   Certifique-se de usar `.\\env\\Scripts\\Activate.ps1` se estiver executando o comando no diretório do seu projeto onde está localizado o ambiente virtual.

Isso deve permitir que o script `activate.ps1` seja executado sem erros de política de execução de scripts. Após concluir as tarefas que exigem a execução de scripts, você pode restaurar a política de execução de scripts para o valor padrão usando o comando:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Default
```

Lembre-se de que alterar a política de execução de scripts pode ter implicações de segurança, portanto, é importante entender os riscos associados antes de permitir a execução de scripts não confiáveis.



```powershell
python manage.py runserver
```
