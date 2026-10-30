# Controle da solução do trabalho

Edite `source/conf.py` e altere somente os valores das entregas que deseja liberar:

```python
solucao_entregas_liberadas = {
    1: False,
    2: False,
    3: False,
    4: False,
    5: False,
    6: False,
}
```

Use `True` e `False` com inicial maiúscula, sem aspas, pois o arquivo é Python.
Comentar ou remover a linha de uma entrega também a mantém oculta. As liberações
são independentes: liberar a Entrega 2 não libera automaticamente a Entrega 1.

Edite a solução de cada entrega no respectivo `entrega-N.md` desta pasta. Os
links para as aulas usam `../aulas/`, pois o texto é renderizado na página
`source/disciplina/000-solucao-trabalho.md`. Mantenha os títulos de entrega em
nível 2 (`##`) e as etapas em nível 3 (`###`).

Gere o site com `sphinx-build -b html source build/html` e confira
`build/html/disciplina/000-solucao-trabalho.html`. No fluxo atual, o push em
`main` reconstrói e publica o site pelo GitHub Actions. Para retirar uma parte
já liberada, volte seu valor para `False` e publique novamente.

Os arquivos desta pasta ficam fora de `source/`. Só o conteúdo marcado como
`True` é incluído na página, na busca e nos artefatos gerados pelo Sphinx.
Não há ocultação por CSS, JavaScript ou caixas recolhíveis. O controle vale para
o site publicado: se o repositório for público, estes arquivos e seu histórico
continuam acessíveis pelo GitHub. Conteúdo já publicado também pode ter sido salvo.
