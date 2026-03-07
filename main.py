import os
from pathlib import Path
from PIL import Image # Pillow library

class ConversorImagens:
    """
    Automatiza a conversão de imagens de um formato para outro em massa.
    Muito útil para converter PNGs pesados em WebP ou JPG para sites.
    """
    def __init__(self, diretorio, formato_origem, formato_destino):
        self.diretorio = Path(diretorio)
        self.formato_origem = formato_origem.lower().strip('.')
        self.formato_destino = formato_destino.lower().strip('.')
        self.contador = 0

    def converter(self):
        if not self.diretorio.exists():
            print(f"Diretório '{self.diretorio}' não encontrado.")
            return

        # Cria a pasta de saída dentro do diretório original
        pasta_saida = self.diretorio / f"Convertidas_{self.formato_destino.upper()}"
        pasta_saida.mkdir(exist_ok=True)

        print(f"Buscando arquivos .{self.formato_origem} em {self.diretorio}...")
        
        for arquivo in self.diretorio.glob(f"*.{self.formato_origem}"):
            try:
                # Abre a imagem
                img = Image.open(arquivo)
                
                # Se for converter para JPG, precisamos remover a transparência (Alpha)
                if self.formato_destino in ['jpg', 'jpeg'] and img.mode in ('RGBA', 'LA', 'P'):
                    fundo_branco = Image.new('RGB', img.size, (255, 255, 255))
                    fundo_branco.paste(img, mask=img.split()[3] if img.mode == 'RGBA' else None)
                    img = fundo_branco
                else:
                    img = img.convert('RGB') # Padroniza para RGB

                # Define o novo nome e caminho
                novo_nome = f"{arquivo.stem}.{self.formato_destino}"
                caminho_salvar = pasta_saida / novo_nome
                
                # Salva a nova imagem
                # Se for webp ou jpeg, podemos definir qualidade
                img.save(caminho_salvar, format=self.formato_destino, quality=85)
                
                print(f"Convertido: {arquivo.name} -> {novo_nome}")
                self.contador += 1
                
            except Exception as e:
                print(f"Erro ao converter {arquivo.name}: {e}")

        print(f"\nFinalizado! {self.contador} imagens convertidas.")
        print(f"Salvas em: {pasta_saida}")

if __name__ == "__main__":
    # IMPORTANTE: Para rodar este script, você precisa instalar o Pillow:
    # pip install Pillow
    
    print("=== Conversor de Imagens em Massa ===")
    pasta = input("Caminho da pasta com as imagens: ")
    origem = input("Formato original (ex: png): ")
    destino = input("Formato desejado (ex: jpg, webp): ")
    
    if pasta and origem and destino:
        conversor = ConversorImagens(pasta, origem, destino)
        conversor.converter()
