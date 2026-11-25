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

Edite a solução de cada entrega no respectivo `entrega-N.md` desta pasta. Cada
entrega é renderizada em uma página própria,
`source/disciplina/000-solucao-entrega-N.md`, filha de **Solução do trabalho**
no menu lateral. Essas páginas contêm apenas o marcador
`<!-- solucao:entrega-N -->`; não escreva nelas.

Os links para as aulas usam `../aulas/` e os arquivos para download usam
`../_static/`, pois o texto é renderizado em `source/disciplina/`. Figuras da
solução ficam em `figuras/` desta pasta e são referenciadas como
`../../professor/solucao-trabalho/figuras/...`; assim, só são publicadas quando
a entrega é liberada. Mantenha os títulos de entrega em nível 2 (`##`) e as
etapas em nível 3 (`###`): na página da entrega, a extensão sobe todos os
títulos um nível, e as etapas aparecem no índice "Nesta página".

Gere o site com `sphinx-build -b html source build/html` e confira
`build/html/disciplina/000-solucao-entrega-N.html`. No fluxo atual, o push em
`main` reconstrói e publica o site pelo GitHub Actions. Para retirar uma parte
já liberada, volte seu valor para `False` e publique novamente.

Os arquivos desta pasta ficam fora de `source/`. Só o conteúdo marcado como
`True` é incluído na página, na busca e nos artefatos gerados pelo Sphinx.
Não há ocultação por CSS, JavaScript ou caixas recolhíveis. O controle vale para
o site publicado: se o repositório for público, estes arquivos e seu histórico
continuam acessíveis pelo GitHub. Conteúdo já publicado também pode ter sido salvo.
