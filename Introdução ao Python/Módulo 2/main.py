
filmes = []

filmes.append('Batman: O Cavaleiro das Trevas')
filmes.append('O Poderoso Chefão: Parte II')
filmes.append('O Senhor dos Anéis: O Retorno do Rei')
filmes.append('O Senhor dos Anéis: A Sociedade do Anel')
filmes.append('Forrest Gump: O Contador de Histórias')
filmes.append('O Senhor dos Anéis: As Duas Torres')
filmes.append('Clube da Luta')
filmes.append('A Origem')
filmes.append('Star Wars: Episódio V - O Império Contra-Ataca')
filmes.append('Matrix')

print(f'lista de {len(filmes)} filmes que mais gosto\n')
print(filmes)

print('Simule a movimentação do ranking. Utilize os métodos insert e pop para trocar a posição do primeiro e do segundo filme da lista. Imprima o resultado.\n')

filmes.pop(0)
filmes.pop(0)
filmes.insert(0, 'O Poderoso Chefão: Parte II')
filmes.insert(1, 'Batman: O Cavaleiro das Trevas')


print(f'lista de {len(filmes)} filmes que mais gosto\n')
print(filmes)

list_filmes = []

filme1 = {'nome': 'O Poderoso Chefão: Parte II', 'ano': '1972', 'sinopse': 'O patriarca idoso de uma dinastia do crime organizado transfere.....'}
filme2 = {'nome': 'Batman: O Cavaleiro das Trevas', 'ano': '2008', 'sinopse': 'Agora com a ajuda do tenente Jim Gordon.....'}


list_filmes.append(filme1)
list_filmes.append(filme2)

print(list_filmes)