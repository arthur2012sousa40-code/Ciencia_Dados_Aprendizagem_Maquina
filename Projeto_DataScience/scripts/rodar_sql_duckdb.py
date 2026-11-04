"""Executa o livro_ocorrencias.sql no DuckDB, sem precisar instalar o PostgreSQL.

Uso (na pasta Projeto_Ciencia_de_Dados):  python scripts/rodar_sql_duckdb.py

- Carrega dados/livro_ocorrencias_transcrito.csv no lugar do comando \\copy do psql.
- Roda as validações, a view e os KPIs, imprimindo cada resultado.
- No fim, confere se os indicadores do SQL batem com os do notebook (dados/processed/resumo_resultados.json):
  é o critério "indicadores reproduzíveis" – o painel do sistema usa estas mesmas consultas.
"""
import json
import os
import re
import sys

import duckdb

PASTA = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), '..')


def consultas(caminho_sql):
    """Lê o .sql e devolve (título, comando) na ordem do arquivo."""
    texto = open(caminho_sql, encoding='utf-8').read()
    texto = re.sub(r'/\*.*?\*/', '', texto, flags=re.S)
    texto = '\n'.join(l for l in texto.splitlines() if not l.startswith('\\'))  # comandos do psql
    for bloco in texto.split(';'):
        linhas = [l for l in bloco.strip().splitlines()]
        comentarios = [l.strip('- ').strip() for l in linhas if l.strip().startswith('--')]
        corpo = '\n'.join(l for l in linhas if not l.strip().startswith('--')).strip()
        if corpo:
            yield (comentarios[0] if comentarios else ''), corpo


def para_duckdb(sql):
    """Pequenas diferenças de dialeto PostgreSQL → DuckDB."""
    return sql.replace('regexp_like(', 'regexp_matches(')


def executar(pasta=PASTA, imprimir=True):
    con = duckdb.connect()
    resultados = {}
    for titulo, sql in consultas(os.path.join(pasta, 'livro_ocorrencias.sql')):
        sql = para_duckdb(sql)
        if sql.upper().startswith('CREATE TABLE'):
            con.execute(sql)
            csv = os.path.join(pasta, 'dados', 'livro_ocorrencias_transcrito.csv')
            con.execute(f"INSERT INTO ocorrencia_bruta SELECT * FROM read_csv('{csv}', header=true, all_varchar=true)")
            n = con.execute('SELECT COUNT(*) FROM ocorrencia_bruta').fetchone()[0]
            if imprimir:
                print(f'Tabela ocorrencia_bruta carregada: {n} registros')
            continue
        if sql.upper().startswith('CREATE'):
            con.execute(sql)
            if imprimir:
                print('View ocorrencias_limpas criada')
            continue
        df = con.execute(sql).df()
        resultados[titulo.split(' – ')[0]] = df
        if imprimir:
            print(f'\n=== {titulo}\n{df.to_string(index=False)}')
    return resultados


if __name__ == '__main__':
    r = executar()
    caminho = os.path.join(PASTA, 'dados', 'processed', 'resumo_resultados.json')
    if os.path.exists(caminho):
        nb = json.load(open(caminho, encoding='utf-8'))
        k1 = r['KPI 1'].iloc[0]
        conferir = [
            ('ocorrências na base limpa', k1.ocorrencias, nb['ocorrencias_limpas']),
            ('taxa de resposta (%)', k1.taxa_resposta_pct, round(nb['taxa_resposta'] * 100, 1)),
            ('mediana de dias até a resposta', k1.mediana_dias, nb['mediana_dias']),
            ('recorrentes (%)', k1.recorrentes_pct, round(nb['recorrencia'] * 100, 1)),
            ('completos (%)', k1.completos_pct, round(nb['completude'] * 100, 1)),
            ('concordância da dupla (%)', r['C'].iloc[0].concordancia_pct, round(nb['concordancia'] * 100, 1)),
            ('H3 – barulho à noite/fim de semana (%)', r['A'].iloc[0].noite_ou_fds_pct, round(nb['h3_barulho_noite_fds'] * 100, 1)),
        ]
        print('\n=== Conferência SQL × notebook')
        ok = True
        for nome, sql_v, nb_v in conferir:
            igual = abs(float(sql_v) - float(nb_v)) < 0.05
            ok &= igual
            print(f'{"OK " if igual else "DIF"} {nome}: SQL {float(sql_v):g} · notebook {float(nb_v):g}')
        print('Todos os indicadores conferem.' if ok else 'Há diferenças: revisar a regra de limpeza.')
