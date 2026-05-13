from lxml import etree


def extrair_dados_xml(xml_content):
    try:
        root = etree.fromstring(xml_content)
        namespaces = {'nfe': 'http://www.portalfiscal.inf.br/nfe'}
        
        nfe_number_element = root.xpath(".//nfe:nNF", namespaces=namespaces)
        numero_nfe = nfe_number_element[0].text if nfe_number_element else None
        
        chave_acesso_element = root.xpath(".//nfe:infNFe", namespaces=namespaces)
        chave_acesso = chave_acesso_element[0].get('id') if chave_acesso_element else None
        
        return numero_nfe, chave_acesso
    except Exception:
        return None, None