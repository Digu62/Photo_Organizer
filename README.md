### Contextualização do Projeto
O Photo Organizer atua como um gerenciador de fotos, voltado para organização pessoal de imagens. Ele realiza a separação das imagens com base na data de criação ou edição e as separa automaticamente em uma hierarquia de pastas por data e ano.

## Como executar através da CLI

1. Tenha python versão 3.13.5 ou superior instalado.

2. Instale os requirements.txt
> pip install -r requirements.txt

3. Execute main.py

4. Selecione as pastas de origem e destino das imagens.

## Utilizando executavel (windows)

Também é possível executar a aplicação através do arquivo "organizer.exe". Basta executa-lo e selecionar as pastas origem e destino das imagemms. 

## Como construir um executável

1. Installe o requirements.txt
> pip install -r requirements.txt

2. Crie o arquivo executável
> pyinstaller -w -F main.py --name <file-name>


Nota: Esse codigo foi baseado no tutorial do "Código Fonte TV" e adaptado para uso pessoal. Você pode acessar o tutorial diretamente através do [link](https://www.youtube.com/watch?v=L8KFB0VyEwo&t=146s&ab_channel=C%C3%B3digoFonteTV)