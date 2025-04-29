# Youtube Clean Converter
### Welcome! If you're having any problems with usage, feel free to open an issue!
### Bem-vindo! Se você está tendo problemas usando a API, porfavor crie um issue!

[Linkedin Post](https://www.linkedin.com/feed/update/urn:li:ugcPost:7317375614452170752/) <br>
**Email me** If you need help: [atilalimade@gmail.com](mailto:atilalimade@gmail.com)

---

## 🇧🇷 Versão em Português

### Introdução
**Youtube Clean Converter** é uma API e website desenvolvido para facilitar o download e conversão de conteúdos do YouTube de forma limpa e eficiente.
O sistema permite baixar arquivos de áudio (.mp3) e vídeo (.mp4) diretamente via uma interface Web e também por meio de requisições à API.
Utilizando FastAPI e Uvicorn, o sistema foi criado para ser fácil de implementar tanto em ambientes locais quanto na AWS (Ubuntu).

### Como Usar a API
1. Acesse o site da api, rodando em localhost ou online.
2. Escolha um serviço oferecido na lista para download (aúdio ou vídeo, e também comprimido).
3. Pressione o botão de testar a API, e cole o seu link na caixa de entrada.
4. Clique no botão de download e aguarde que o arquivo seja processado.
5. O arquivo resultante será baixado, ficando disponível no botão 'Download file'.

### Como Implementar a API em um Novo Ambiente (Local ou AWS)

#### Pré-requisitos:
- Python 3.11
- Python VEnv (opcional, mas recomendado)
- Dependências (listadas no `requirements.txt`, como *FastAPI* e *yt-dlp*)

#### Passos para instalação local:
```bash
# Clone o repositório
git clone https://github.com/limatila/Youtube-Clean-Converter.git
cd Youtube-Clean-Converter #você pode renomear se preferir

# Crie e ative um ambiente virtual
python3.11 -m venv venv
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

# Configure seus cookies de uso (copie os de uma conta anônima do Youtube)
notepad cookies.txt #copie seus cookies aqui
notepad backup-cookies.txt #copie também aqui
# ou use 'vim' para edição

# Configure variáveis de execução e nomes/descrição, se preferir
# veja em 'src/config.py'

# Inicie o servidor
uvicorn src.main.api_cleanconverter:app --host 0.0.0.0 --port 55002 #--reload
```
Tudo certinho, você pode ver a documentação da API em: `http://localhost:55002/docs`, ou outro IP / DNS

#### Obs: para configuração de cookies, você pode obter mais informações [AQUI](https://github.com/yt-dlp/yt-dlp/wiki/Extractors#exporting-youtube-cookies)

### Extras
- **Compressão de Arquivos:** Suporte a compressão com `py7zr` (formato .7z)
- **Loggers Personalizados:** Monitoramento de cookies, uso de arquivos e desempenho
- **Gerenciamento de Cookies:** Backup, validação e renovação automática
- **Modularidade:** Código organizado por funcionalidades para facilitar manutenção

### Obs 2: este projeto é distribuído gratuitamente, sem fins lucrativos. Ele será disponibilizado online apenas para uso educacional e como projeto pessoal.

---

## 🇺🇸 English Version

### Introduction
**Youtube Clean Converter** is an API and website built to simplify downloading and converting YouTube content in a clean and efficient way.
The system allows downloading audio (.mp3) and video (.mp4) files directly via the Web interface or through API requests.
Built with FastAPI and Uvicorn, it’s designed to be easily deployed locally or on AWS (Ubuntu).

### How to Use the Online API
1. Visit the API site, on localhost or online.
2. Choose a service from the list (audio, video, or compressed file).
3. Press the test button and paste your YouTube link into the input field.
4. Click download and wait for the file to be processed.
5. The file will be downloaded and become available through the "Download file" button.

### How to Implement the API in a New Environment (Local or AWS)

#### Prerequisites:
- Python 3.11
- Python VEnv (optional but recommended)
- Dependencies (listed in `requirements.txt`, such as *FastAPI* and *yt-dlp*)

#### Local Setup Steps:
```bash
# Clone the repository
git clone https://github.com/limatila/Youtube-Clean-Converter.git
cd Youtube-Clean-Converter #rename it if you prefer

# Create and activate a virtual environment
python3.11 -m venv venv
source venv/bin/activate

# Install the dependencies
pip install -r requirements.txt

# Setup your usage cookies (copy them from an anonymous YouTube session)
notepad cookies.txt #paste your cookies here
notepad backup-cookies.txt #also here
# or use 'vim' for editing

# Adjust runtime variables and names/descriptions, if desired
# check 'src/config.py'

# Start the server
uvicorn src.main.api_cleanconverter:app --host 0.0.0.0 --port 55002 #--reload
```
Once everything is ready, access the API documentation at: `http://localhost:55002/docs`, or your custom IP / DNS.
#### Note: for cookie configuration help, visit [HERE](https://github.com/yt-dlp/yt-dlp/wiki/Extractors#exporting-youtube-cookies)

### Extras
- **File Compression:** Supports `.7z` file compression via `py7zr`
- **Custom Loggers:** Cookie, file, and performance tracking
- **Cookie Management:** Backup, validation and auto-replacement
- **Modular Design:** Organized code structure for easier maintenance

### Note 2: This project is provided free of charge, for educational and personal-use purposes only.

