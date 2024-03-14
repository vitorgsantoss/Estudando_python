import os

caminho = os.path.join('Documents','Python','Udemy','modulo_python','aula282.py')
# print(caminho)
pastas, arquivo = os.path.split(caminho)
# print(f'{pastas}, {arquivo}')
nome_arquivo, extensão = os.path.splitext(arquivo)
# print(f'{nome_arquivo}\n {extensão}')
# print(os.path.exists('C:\\Users\\Lucas Calzans\\Documents\\Python\\Udemy'))
ultima_parte_caminho = os.path.basename(caminho)
print(ultima_parte_caminho)
caminho_sem_a_ultima_parte = os.path.dirname(caminho)
print(caminho_sem_a_ultima_parte)