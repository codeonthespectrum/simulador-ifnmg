#!/usr/bin/env python3
"""
Script para extrair dados dos PDFs e gerar o arquivo de dados para o simulador
"""
import pdfplumber
import json
import re

def extrair_vagas():
    """Extrai os dados de vagas do PDF de cursos e vagas"""
    vagas_por_codigo = {}
    
    # Mapeamento de códigos para cursos baseado no PDF de inscrições
    codigos_cursos = {
        '101': {'nome': 'Técnico em Enfermagem', 'campus': 'Campus Almenara'},
        '201': {'nome': 'Técnico em Enfermagem', 'campus': 'Campus Araçuaí'},
        '202': {'nome': 'Técnico em Mineração', 'campus': 'Campus Araçuaí'},
        '203': {'nome': 'Técnico em Química', 'campus': 'Campus Araçuaí'},
        '301': {'nome': 'Técnico em Administração', 'campus': 'Polo: Campus Montes Claros'},
        '302': {'nome': 'Técnico em Administração', 'campus': 'Polo: Unidade-CEADi - Montes Claros'},
        '303': {'nome': 'Técnico em Administração', 'campus': 'Polo: Campus Araçuaí'},
        '304': {'nome': 'Técnico em Administração', 'campus': 'Polo: Nova Porteirinha'},
        '305': {'nome': 'Técnico em Administração', 'campus': 'Polo: Verdelândia'},
        '306': {'nome': 'Técnico em Administração', 'campus': 'Polo: Campus Januária'},
        '307': {'nome': 'Técnico em Administração', 'campus': 'Polo: Ibiaí'},
        '308': {'nome': 'Técnico em Administração', 'campus': 'Polo: Riacho dos Machados'},
        '3010': {'nome': 'Técnico em Administração', 'campus': 'Polo: Campus Salinas'},
        '3011': {'nome': 'Técnico em Inteligência Artificial', 'campus': 'Polo: Campus Montes Claros - CEADI'},
        '3012': {'nome': 'Técnico em Inteligência Artificial', 'campus': 'Polo: Unidade-CEADi - Montes Claros - CEADI'},
        '3013': {'nome': 'Técnico em Inteligência Artificial', 'campus': 'Polo: Campus Almenara'},
        '3014': {'nome': 'Técnico em Inteligência Artificial', 'campus': 'Polo: Campus Araçuaí'},
        '3015': {'nome': 'Técnico em Inteligência Artificial', 'campus': 'Polo: Itinga'},
        '3016': {'nome': 'Técnico em Inteligência Artificial', 'campus': 'Polo: Arinos'},
        '3017': {'nome': 'Técnico em Inteligência Artificial', 'campus': 'Polo: Urucuia'},
        '3018': {'nome': 'Técnico em Inteligência Artificial', 'campus': 'Polo: Flores de Goiás'},
        '3019': {'nome': 'Técnico em Inteligência Artificial', 'campus': 'Polo: Nova Porteirinha'},
        '3020': {'nome': 'Técnico em Inteligência Artificial', 'campus': 'Polo: Verdelândia'},
        '3021': {'nome': 'Técnico em Inteligência Artificial', 'campus': 'Polo: Campus Januária'},
        '3022': {'nome': 'Técnico em Inteligência Artificial', 'campus': 'Polo: Campus Salinas'},
        '3023': {'nome': 'Técnico em Inteligência Artificial', 'campus': 'Polo: Riacho dos Machados'},
        '3024': {'nome': 'Técnico em Inteligência Artificial', 'campus': 'Polo: Serranópolis de Minas'},
        '3025': {'nome': 'Técnico em Inteligência Artificial', 'campus': 'Polo: Campus Porteirinha'},
        '3026': {'nome': 'Técnico em Inteligência Artificial', 'campus': 'Polo: Capelinha'},
        '3027': {'nome': 'Técnico em Inteligência Artificial', 'campus': 'Polo: Carlos Chagas'},
        '3028': {'nome': 'Técnico em Inteligência Artificial', 'campus': 'Polo: Governador Valadares'},
        '3029': {'nome': 'Técnico em Inteligência Artificial', 'campus': 'Polo: Itambacuri'},
        '3030': {'nome': 'Técnico em Inteligência Artificial', 'campus': 'Polo: Nanuque'},
        '3031': {'nome': 'Técnico em Inteligência Artificial', 'campus': 'Polo: Teófilo Otoni'},
        '3032': {'nome': 'Técnico em Serviços Jurídicos', 'campus': 'Polo: CEADi - Montes Claros'},
        '3033': {'nome': 'Técnico em Inteligência Artificial', 'campus': 'Polo: Ibiaí'},
        '3034': {'nome': 'Técnico em Inteligência Artificial', 'campus': 'Polo: Curvelo'},
        '3035': {'nome': 'Técnico em Inteligência Artificial', 'campus': 'Polo: Buenópolis'},
        '401': {'nome': 'Técnico em Enfermagem', 'campus': 'Campus Januária'},
        '402': {'nome': 'Técnico em Manutenção e Suporte em Informática', 'campus': 'Campus Januária'},
        '501': {'nome': 'Técnico em Eletrotécnica', 'campus': 'Campus Montes Claros'},
        '502': {'nome': 'Técnico em Segurança do Trabalho', 'campus': 'Campus Montes Claros'},
        '503': {'nome': 'Técnico em Química', 'campus': 'Campus Montes Claros'},
        '601': {'nome': 'Técnico em Informática', 'campus': 'Campus Pirapora'},
        '602': {'nome': 'Técnico em Segurança do Trabalho', 'campus': 'Campus Pirapora'},
        '701': {'nome': 'Técnico em Eletrotécnica', 'campus': 'Campus Porteirinha'},
        '801': {'nome': 'Técnico em Enfermagem', 'campus': 'Campus Teófilo Otoni'},
    }
    
    # Vagas padrão para 40 vagas (mais comum)
    vagas_40 = {
        'total': 40, 'AC': 18, 'V_PCD': 1, 'V_EFA': 1,
        'LB_PPI': 6, 'LB_EP': 1, 'LB_PCD': 1, 'LB_Q': 2,
        'LI_PPI': 6, 'LI_EP': 3, 'LI_PCD': 1, 'LI_Q': 0
    }
    
    vagas_160 = {
        'total': 160, 'AC': 72, 'V_PCD': 4, 'V_EFA': 4,
        'LB_PPI': 24, 'LB_EP': 11, 'LB_PCD': 4, 'LB_Q': 1,
        'LI_PPI': 24, 'LI_EP': 12, 'LI_PCD': 4, 'LI_Q': 0
    }
    
    vagas_80 = {
        'total': 80, 'AC': 36, 'V_PCD': 2, 'V_EFA': 2,
        'LB_PPI': 12, 'LB_EP': 5, 'LB_PCD': 2, 'LB_Q': 1,
        'LI_PPI': 12, 'LI_EP': 6, 'LI_PCD': 2, 'LI_Q': 0
    }
    
    vagas_35 = {
        'total': 35, 'AC': 15, 'V_PCD': 1, 'V_EFA': 1,
        'LB_PPI': 6, 'LB_EP': 1, 'LB_PCD': 1, 'LB_Q': 1,
        'LI_PPI': 6, 'LI_EP': 2, 'LI_PCD': 1, 'LI_Q': 0
    }
    
    vagas_30 = {
        'total': 30, 'AC': 13, 'V_PCD': 1, 'V_EFA': 1,
        'LB_PPI': 5, 'LB_EP': 1, 'LB_PCD': 1, 'LB_Q': 1,
        'LI_PPI': 5, 'LI_EP': 1, 'LI_PCD': 1, 'LI_Q': 0
    }
    
    vagas_25 = {
        'total': 25, 'AC': 9, 'V_PCD': 1, 'V_EFA': 1,
        'LB_PPI': 5, 'LB_EP': 1, 'LB_PCD': 1, 'LB_Q': 1,
        'LI_PPI': 4, 'LI_EP': 1, 'LI_PCD': 1, 'LI_Q': 0
    }
    
    vagas_20 = {
        'total': 20, 'AC': 9, 'V_PCD': 0, 'V_EFA': 0,
        'LB_PPI': 3, 'LB_EP': 1, 'LB_PCD': 1, 'LB_Q': 1,
        'LI_PPI': 3, 'LI_EP': 1, 'LI_PCD': 1, 'LI_Q': 0
    }
    
    vagas_120 = {
        'total': 120, 'AC': 54, 'V_PCD': 3, 'V_EFA': 3,
        'LB_PPI': 18, 'LB_EP': 8, 'LB_PCD': 3, 'LB_Q': 1,
        'LI_PPI': 18, 'LI_EP': 9, 'LI_PCD': 3, 'LI_Q': 0
    }
    
    
    mapa_vagas = {
        '101': vagas_40,  # Enfermagem Almenara
        '201': vagas_35,  # Enfermagem Araçuaí
        '202': vagas_40,  # Mineração Araçuaí
        '203': vagas_30,  # Química Araçuaí
        '301': vagas_80,  # Admin Campus Montes Claros
        '302': vagas_160, # Admin CEADi
        '303': vagas_40,  # Admin Araçuaí
        '304': vagas_40,  # Admin Nova Porteirinha
        '305': vagas_40,  # Admin Verdelândia
        '306': vagas_40,  # Admin Januária (não listado, assumindo 40)
        '307': vagas_40,  # Admin Ibiaí (Serranópolis)
        '308': vagas_40,  # Admin Riacho dos Machados (não listado)
        '3010': vagas_80, # Admin Salinas
        '3011': vagas_40,  # IA Campus Montes Claros
        '3012': vagas_160, # IA CEADi Montes Claros
        '3013': vagas_40,  # IA Almenara
        '3014': vagas_40,  # IA Araçuaí
        '3015': vagas_40,  # IA Itinga
        '3016': vagas_40,  # IA Arinos
        '3017': vagas_40,  # IA Urucuia
        '3018': vagas_40,  # IA Flores de Goiás
        '3019': vagas_40,  # IA Nova Porteirinha
        '3020': vagas_40,  # IA Verdelândia
        '3021': vagas_40,  # IA Januária
        '3022': vagas_40,  # IA Salinas
        '3023': vagas_40,  # IA Riacho dos Machados
        '3024': vagas_40,  # IA Serranópolis
        '3025': vagas_40,  # IA Porteirinha
        '3026': vagas_40,  # IA Capelinha
        '3027': vagas_40,  # IA Carlos Chagas
        '3028': vagas_40,  # IA Gov. Valadares
        '3029': vagas_40,  # IA Itambacuri
        '3030': vagas_40,  # IA Nanuque
        '3031': vagas_40,  # IA Teófilo Otoni
        '3032': vagas_120, # Serviços Jurídicos
        '3033': vagas_40,  # IA Ibiaí
        '3034': vagas_40,  # IA Curvelo
        '3035': vagas_40,  # IA Buenópolis
        '401': vagas_20,   # Enfermagem Januária
        '402': vagas_25,   # MSI Januária
        '501': vagas_40,   # Eletrotécnica Montes Claros
        '502': vagas_40,   # Segurança Trabalho Montes Claros
        '503': vagas_40,   # Química Montes Claros
        '601': vagas_40,   # Informática Pirapora
        '602': vagas_40,   # Segurança Trabalho Pirapora
        '701': vagas_30,   # Eletrotécnica Porteirinha
        '801': vagas_25,   # Enfermagem Teófilo Otoni
    }
    
    result = {}
    for codigo, info in codigos_cursos.items():
        result[codigo] = {
            'nome': info['nome'],
            'campus': info['campus'],
            'vagas': mapa_vagas.get(codigo, vagas_40)
        }
    
    return result


def extrair_inscricoes():
    """Extrai os dados de inscrições deferidas do PDF"""
    inscricoes = []
    
    with pdfplumber.open("LISTA-PRELIMINAR-DE-INSCRICOES-DEFERIDAS-E-INDEFERIDAS-EDITAL-1048.pdf") as pdf:
        for page in pdf.pages:
            tables = page.extract_tables()
            for table in tables:
                for row in table:
                    if row and len(row) >= 7:
                        situacao = str(row[6] or '').strip()
                        if situacao == 'DEFERIDA':
                            vaga = str(row[3] or '').replace('\n', ' ').strip()
                            modalidade = str(row[4] or '').strip()
                            nota_str = str(row[5] or '0').replace(',', '.').strip()
                            try:
                                nota = float(nota_str)
                            except:
                                nota = 0.0
                            
                            # Extrair código e nome do curso
                            match = re.match(r'^(\d+)\s*-\s*(.+)$', vaga)
                            if match:
                                codigo = match.group(1)
                                nome_curso = match.group(2).strip()
                                
                                # Normalizar modalidade
                                modalidade_norm = modalidade.replace('Ampla Concorrência', 'AC')
                                
                                inscricoes.append({
                                    'codigo': codigo,
                                    'modalidade': modalidade_norm,
                                    'nota': nota
                                })
    
    return inscricoes


def main():
    print("Extraindo dados de vagas...")
    cursos = extrair_vagas()
    print(f"  Total de cursos: {len(cursos)}")
    
    print("\nExtraindo inscrições deferidas...")
    inscricoes = extrair_inscricoes()
    print(f"  Total de inscrições: {len(inscricoes)}")
    
    # Salvar dados em JSON
    dados = {
        'cursos': cursos,
        'inscricoes': inscricoes
    }
    
    with open('dados_simulador.json', 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)
    
    print("\nDados salvos em 'dados_simulador.json'")
    
    # Estatísticas
    print("\n=== Estatísticas ===")
    for cod, info in sorted(cursos.items()):
        qtd = len([i for i in inscricoes if i['codigo'] == cod])
        print(f"{cod}: {info['nome']} - {info['campus']} - {qtd} inscritos - {info['vagas']['total']} vagas")


if __name__ == '__main__':
    main()
