# Voxus Challenge

## Instalação/Execução
Crie a imagem do container Docker:
```bash
docker image build -t voxus_challenge_1 . 
```
Uma vez criada a imagem, o container pode ser executado:  
_(Caso a porta 5001 esteja indisponível, você pode alterar para qualquer porta de sua preferência)_
```bash
docker run -p 5001:5000 -d --name voxus_challenge_1 voxus_challenge_1
```

Com o container em execução, acesse:  
http://localhost:5001

Por padrão, a rota inicial retorna o texto "looks like we're running!", como forma de verificar se o container está rodando.

## Testes do Desafio
O desafio pode ser testado através da rota:  
http://localhost:5001/year-day/[data]

Exemplos:
- http://localhost:5001/year-day/2020-08-04
- http://localhost:5001/year-day/2021-08-04
- http://localhost:5001/year-day/2023-08-04