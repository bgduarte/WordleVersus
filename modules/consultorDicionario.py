from random import randint

class ConsultorDicionario:
    __filePath = "./data/words"

    def pegar_palavra_aleatoria() -> str:
        with open(ConsultorDicionario.__filePath, "r") as file:
            palavras = file.readlines()
            palavra = palavras[randint(0, len(palavras))]
            return palavra.strip()

    def palavra_existe(palavra: str) -> bool:
        with open(ConsultorDicionario.__filePath, "r") as file:
            palavras = file.readlines()
            palavras = [palavra.strip() for palavra in palavras]
            return palavra in palavras