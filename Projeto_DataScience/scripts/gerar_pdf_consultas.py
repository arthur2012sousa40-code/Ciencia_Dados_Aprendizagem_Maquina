"""Gera Livro_Ocorrencias_Analise_SQL.pdf: capa e uma consulta por página (SQL colorido + resultado).

Uso (na pasta Projeto_Ciencia_de_Dados):  python scripts/gerar_pdf_consultas.py
As consultas vêm do livro_ocorrencias.sql e são executadas no DuckDB (scripts/rodar_sql_duckdb.py).
Requer: pip install playwright duckdb pandas  (o Chromium do Playwright: python -m playwright install chromium)
"""
import html
import os
import re
import sys

from playwright.sync_api import sync_playwright

sys.path.insert(0, os.path.dirname(__file__))
from rodar_sql_duckdb import PASTA, consultas, executar  # noqa: E402

PALAVRAS = {'SELECT', 'FROM', 'WHERE', 'JOIN', 'ON', 'GROUP', 'BY', 'ORDER', 'HAVING', 'AS', 'AND', 'OR', 'CASE',
            'WHEN', 'THEN', 'ELSE', 'END', 'WITH', 'CREATE', 'VIEW', 'LIMIT', 'DESC', 'ASC', 'IS', 'NULL', 'NOT',
            'DISTINCT', 'OVER', 'WITHIN', 'DATE', 'CAST', 'IN', 'PARTITION', 'EXISTS', 'INTERVAL', 'NULLS', 'LAST',
            'INTEGER', 'TABLE', 'PRIMARY', 'KEY', 'VARCHAR'}
FUNCOES = {'SUM', 'COUNT', 'AVG', 'ROUND', 'MIN', 'MAX', 'PERCENTILE_CONT', 'DATE_TRUNC', 'ROW_NUMBER', 'EXTRACT',
           'COALESCE', 'SUBSTRING', 'REGEXP_REPLACE', 'REGEXP_LIKE'}
TOKEN = re.compile(r"('[^']*')|(\b\d+(?:\.\d+)?\b)|(\b[A-Za-z_]+\b)|(\s+)|(.)")


def colorir(codigo):
    saida = []
    for texto, num, palavra, espaco, outro in TOKEN.findall(codigo):
        if texto:
            saida.append(f'<span class="s">{html.escape(texto)}</span>')
        elif num:
            saida.append(f'<span class="n">{num}</span>')
        elif palavra:
            u = palavra.upper()
            cls = 'k' if u in PALAVRAS else 'f' if u in FUNCOES else None
            saida.append(f'<span class="{cls}">{html.escape(palavra)}</span>' if cls else html.escape(palavra))
        else:
            saida.append(html.escape(espaco or outro))
    return ''.join(saida)


def formatar(v):
    if v is None or (isinstance(v, float) and v != v):
        return '—'
    if hasattr(v, 'strftime'):
        return v.strftime('%m/%Y') if v.day == 1 else v.strftime('%d/%m/%Y')
    if isinstance(v, float):
        return (f'{v:,.0f}' if v.is_integer() else f'{v:,.1f}').replace(',', 'X').replace('.', ',').replace('X', '.')
    if isinstance(v, bool):
        return 'sim' if v else 'não'
    return html.escape(str(v))


def tabela(df):
    cab = ''.join(f'<th>{html.escape(c)}</th>' for c in df.columns)
    linhas = ''.join('<tr>' + ''.join(f'<td>{formatar(v)}</td>' for v in linha) + '</tr>'
                     for linha in df.head(26).itertuples(index=False))
    extra = f'<p class="obs">… mais {len(df) - 26} linhas</p>' if len(df) > 26 else ''
    return f'<table><thead><tr>{cab}</tr></thead><tbody>{linhas}</tbody></table>{extra}'


resultados = executar(imprimir=False)
paginas = ['''<section class="pagina capa">
<div class="faixa"></div>
<div class="livro"><i></i><i></i><i></i><i></i><i></i></div>
<h1>Livro de<br>ocorrências<br><span>Análise SQL</span></h1>
<p class="sub">Validações da transcrição, base limpa e indicadores do painel do síndico</p>
<p class="info">Ciência de Dados e Aprendizagem de Máquina (A1) · UDF<br>Profa. Dra. Kadidja Valéria Reginaldo de Oliveira</p>
<p class="info"><b>Arthur Rodrigues de Souza Vieira</b> – sistema, SQL e painel<br>
<b>Ramon Guilherme Marques do Nascimento</b> – dados e análise</p>
<p class="aviso">Dados simulados com a estrutura planejada para a transcrição anonimizada do livro físico
de um condomínio do DF (nov./2024 a out./2026). Não descrevem um condomínio real.</p>
</section>''']
for titulo, sql in consultas(os.path.join(PASTA, 'livro_ocorrencias.sql')):
    chave = titulo.split(' – ')[0]
    if sql.upper().startswith('CREATE TABLE'):
        continue
    corpo = tabela(resultados[chave]) if chave in resultados else '<p class="obs">View criada com sucesso.</p>'
    paginas.append(f'''<section class="pagina">
<header><span class="selo">{html.escape(chave)}</span><h2>{html.escape(titulo.split(' – ', 1)[-1])}</h2></header>
<pre>{colorir(sql)}</pre>
<h3>Resultado</h3>{corpo}
<footer>Livro de ocorrências digital · livro_ocorrencias.sql · dados simulados</footer>
</section>''')

CSS = '''
@page { size: A4; margin: 0 }
* { box-sizing: border-box }
body { margin: 0; font-family: "DejaVu Sans", Arial, sans-serif; color: #1f2937 }
.pagina { width: 210mm; height: 297mm; padding: 16mm 15mm 14mm; position: relative; page-break-after: always; overflow: hidden }
.capa { background: #f0f7f3; padding: 40mm 20mm }
.faixa { position: absolute; left: 0; top: 0; width: 14mm; height: 100%; background: #2f6f4f }
.livro { position: absolute; right: 22mm; top: 30mm; display: flex; gap: 3mm }
.livro i { display: block; width: 7mm; height: 46mm; background: #3f8f6b; border-radius: 1.5mm }
.livro i:nth-child(2) { height: 52mm; background: #2f6f4f } .livro i:nth-child(4) { background: #c2410c; height: 40mm }
h1 { font-size: 40pt; line-height: 1.05; color: #1b4332; margin: 0 0 10mm }
h1 span { color: #c2410c; font-size: 30pt }
.sub { font-size: 14pt; color: #374151; margin-bottom: 20mm }
.info { font-size: 11pt; color: #374151; line-height: 1.6 }
.aviso { position: absolute; bottom: 30mm; left: 20mm; right: 20mm; font-size: 9.5pt; color: #6b7280;
         border-left: 3px solid #c2410c; padding-left: 4mm }
header { display: flex; align-items: center; gap: 4mm; border-bottom: 2px solid #2f6f4f; padding-bottom: 3mm; margin-bottom: 5mm }
.selo { background: #2f6f4f; color: white; font-weight: bold; padding: 1.5mm 3mm; border-radius: 2mm; font-size: 11pt }
h2 { font-size: 13pt; margin: 0; color: #1b4332 }
h3 { font-size: 11pt; color: #2f6f4f; margin: 5mm 0 2mm }
pre { background: #1b2a22; color: #e5e7eb; padding: 4mm; border-radius: 2mm; font-size: 7.6pt; line-height: 1.35;
      white-space: pre-wrap; margin: 0 }
.k { color: #86efac; font-weight: bold } .f { color: #fdba74 } .s { color: #fde68a } .n { color: #93c5fd }
table { border-collapse: collapse; width: 100%; font-size: 8pt }
th { background: #2f6f4f; color: white; padding: 1.5mm 2mm; text-align: left }
td { padding: 1.2mm 2mm; border-bottom: 1px solid #e5e7eb }
tr:nth-child(even) td { background: #f0f7f3 }
.obs { color: #6b7280; font-size: 9pt }
footer { position: absolute; bottom: 8mm; left: 15mm; right: 15mm; font-size: 7.5pt; color: #9ca3af;
         border-top: 1px solid #e5e7eb; padding-top: 2mm }
'''
documento = f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{"".join(paginas)}</body></html>'
saida = os.path.join(PASTA, 'Livro_Ocorrencias_Analise_SQL.pdf')
with sync_playwright() as p:
    # CHROMIUM_PATH permite usar um Chromium já instalado no computador
    navegador = p.chromium.launch(executable_path=os.environ.get('CHROMIUM_PATH') or None)
    pagina = navegador.new_page()
    pagina.set_content(documento)
    pagina.pdf(path=saida, format='A4', print_background=True)
    navegador.close()
print(f'{len(paginas)} páginas →', os.path.abspath(saida))
