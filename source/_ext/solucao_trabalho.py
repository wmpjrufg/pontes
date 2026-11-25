"""Inclui no site somente as entregas explicitamente liberadas pelo professor.

Cada entrega é renderizada em uma página própria
(``source/disciplina/000-solucao-entrega-N.md``), filha da página
``000-solucao-trabalho.md``. Assim, cada entrega aparece no menu lateral e as
etapas aparecem no índice "Nesta página".
"""

import re
from pathlib import Path

from sphinx.errors import ConfigError, ExtensionError


ENTREGAS = {
    1: "Determinação das ações permanentes e variáveis",
    2: "Fadiga e armadura final da viga",
    3: "Tabuleiro",
    4: "Transversina",
    5: "Esforços em pilares",
    6: "Detalhamento dos pilares",
}
PAGINAS = {numero: f"disciplina/000-solucao-entrega-{numero}" for numero in ENTREGAS}
TITULO = re.compile(r"^(#{2,6})(?=\s)")
CERCA = re.compile(r"^\s*(`{3,}|~{3,})")


def validar_configuracao(app, config):
    liberadas = config.solucao_entregas_liberadas
    if not isinstance(liberadas, dict) or any(
        type(numero) is not int
        or numero not in ENTREGAS
        or type(liberada) is not bool
        for numero, liberada in liberadas.items()
    ):
        raise ConfigError(
            "solucao_entregas_liberadas deve ser um dicionário com chaves "
            "de 1 a 6 e valores True ou False (sem aspas)."
        )


def promover_titulos(texto):
    """Sobe um nível os títulos Markdown (## -> #, ### -> ##, ...).

    Os arquivos entrega-N.md usam ## para a entrega e ### para as etapas. Em uma
    página própria, a entrega passa a ser o título (#) e as etapas, as seções (##).
    Linhas dentro de blocos cercados (``` ou ~~~) não são alteradas.
    """
    linhas = []
    cerca = None
    for linha in texto.splitlines(keepends=True):
        marca = CERCA.match(linha)
        if marca:
            simbolo = marca.group(1)
            if cerca is None:
                cerca = simbolo
            elif simbolo[0] == cerca[0] and len(simbolo) >= len(cerca):
                cerca = None
        elif cerca is None:
            linha = TITULO.sub(lambda m: m.group(1)[1:], linha, count=1)
        linhas.append(linha)
    return "".join(linhas)


def incluir_entregas(app, docname, source):
    numero = next((n for n, pagina in PAGINAS.items() if pagina == docname), None)
    if numero is None:
        return

    marcador = f"<!-- solucao:entrega-{numero} -->"
    texto = source[0]
    if texto.count(marcador) != 1:
        raise ExtensionError(f"Esperado um único marcador {marcador} em {docname}.")

    arquivo = Path(app.srcdir).parent / "professor" / "solucao-trabalho" / f"entrega-{numero}.md"
    # Também detecta edições dos arquivos em builds incrementais.
    app.env.note_dependency(str(arquivo))
    if app.config.solucao_entregas_liberadas.get(numero, False):
        if not arquivo.is_file():
            raise ExtensionError(f"Solução liberada sem arquivo: {arquivo}")
        conteudo = promover_titulos(arquivo.read_text(encoding="utf-8"))
    else:
        conteudo = (
            f"# Entrega {numero} – {ENTREGAS[numero]}\n\n"
            "A solução desta entrega ainda não foi liberada.\n"
        )
    source[0] = texto.replace(marcador, conteudo, 1)


def setup(app):
    app.add_config_value("solucao_entregas_liberadas", {}, "env", types=[dict])
    app.connect("config-inited", validar_configuracao)
    app.connect("source-read", incluir_entregas)
    return {"version": "1.1", "parallel_read_safe": True, "parallel_write_safe": True}
