# Conversor de Imagens em Massa

## Descrição
Automatiza a conversão de múltiplos arquivos de imagem de um formato para outro (ex: PNG para JPG ou WebP). Perfeito para desenvolvedores web e designers que precisam otimizar imagens para a web e reduzir o espaço de armazenamento.

## Funcionalidades
- Conversão em lote baseada na extensão de origem.
- Tratamento automático de transparência (Canal Alpha): converte fundos transparentes em branco ao salvar em JPG/JPEG para evitar erros.
- Criação automática de uma subpasta dedicada com os arquivos convertidos.

## Pré-requisitos
- Python 3.x
- Biblioteca `Pillow` (PIL).

Para instalar as dependências, rode o comando:
`pip install Pillow`

## Como Usar
1. Execute o script.
2. Insira o caminho da pasta que contém as imagens originais.
3. Digite o formato atual das imagens (ex: `png`).
4. Digite o formato final desejado (ex: `jpg` ou `webp`).
