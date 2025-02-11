@echo off
echo Verificando se o ambiente virtual já existe...

:: Verifica se a pasta "venv" existe
if exist venv (
    echo Ambiente virtual já existe. Pulando a criação...
    goto activate_env
)

echo Criando ambiente virtual...

:: Verifica se o Python está instalado
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo Python não encontrado. Certifique-se de que o Python está instalado e no PATH.
    pause
    exit /b 1
)

:: Cria o ambiente virtual
python -m venv venv
if %errorlevel% neq 0 (
    echo Falha ao criar o ambiente virtual. Verifique as permissões ou se o Python está corretamente instalado.
    pause
    exit /b 1
)

echo Ambiente virtual criado com sucesso.

:activate_env
echo Ativando ambiente virtual...
call .\venv\Scripts\activate
if %errorlevel% neq 0 (
    echo Falha ao ativar o ambiente virtual.
    pause
    exit /b 1
)

echo Ambiente virtual ativado.

echo Instalando dependências...
python.exe -m pip install --upgrade pip
if %errorlevel% neq 0 (
    echo Falha ao atualizar o pip.
    pause
    exit /b 1
)

python.exe -m pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Falha ao instalar as dependências. Verifique o arquivo requirements.txt.
    pause
    exit /b 1
)

echo Dependências instaladas com sucesso.

echo Configuração concluída! Use 'venv\Scripts\activate' para ativar o ambiente.

:: Abre um novo terminal com o ambiente virtual ativado
start cmd /k .\venv\Scripts\activate

pause
