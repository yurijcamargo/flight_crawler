# Como ativar o ambiente virtual (.venv)

No Windows PowerShell, para ativar o ambiente virtual:
    .\.venv\Scripts\Activate.ps1

No Prompt de Comando (cmd):
    .\.venv\Scripts\activate.bat

No Linux/macOS (bash/zsh):
    source .venv/bin/activate

Depois disso, instale as bibliotecas com:
    pip install nome_do_pacote

Para desativar o ambiente:
    deactivate
