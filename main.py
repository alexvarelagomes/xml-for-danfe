import streamlit as st
from danfegerador import DanfeGerador
import io
import traceback
import zipfile
from lxml import etree


st.set_page_config(
    page_title="Gerador de DANFE a partir de XML",
    page_icon="📄",
    layout="centered"
)

st.markdown(
    "<h1 style='color: #2E86C1; text-align: center;'>📄 GERADOR DANFE 📄</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center; font-size: 18px;'>Carregue seu arquivo XML ou ZIP para gerar o DANFE correspondente.</p>",
    unsafe_allow_html=True
)

st.markdown("---")

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

with st.form("formulario_processamento"):
    uploaded_file = st.file_uploader(
        'SELECIONE SEU ARQUIVO:',
     
        type=None,
        help="Carregue um arquivo .xml ou um .zip, mesmo que a extensão não esteja correta."
    )
    submitted = st.form_submit_button('Processar documento(s)')

# Processamento do Arquivo Carregado.
if uploaded_file and submitted:
    try:
        # Lê o conteúdo do arquivo em memória para fazer a verificação
        file_buffer = io.BytesIO(uploaded_file.getvalue())

        # Tenta identificar como um arquivo ZIP
        if zipfile.is_zipfile(file_buffer):
            st.info("Arquivo ZIP detectado pelo conteúdo. Processando múltiplos arquivos...")
            file_buffer.seek(0) # Retorna ao início do buffer para leitura do zip
            
            pdfs_gerados = []
            with zipfile.ZipFile(file_buffer, 'r') as zf:
                xml_files = [f for f in zf.namelist() if f.lower().endswith('.xml')]

                if not xml_files:
                    st.warning("O arquivo é um ZIP válido, mas nenhum arquivo .xml foi encontrado dentro dele.")
                else:
                    total_files = len(xml_files)
                    st.write(f"Encontrados {total_files} arquivos XML. Gerando DANFEs...")
                    
                    progress_bar = st.progress(0, text="Processando DANFEs... Por favor, aguarde.")
                    for i, file_name in enumerate(xml_files):
                        with zf.open(file_name) as xml_file:
                            xml_content = xml_file.read()
                            numero_nfe, _ = extrair_dados_xml(xml_content)
                            danfeGerador = DanfeGerador(xml_content)
                            pdf_bytes = danfeGerador.create_danfe()
                            if pdf_bytes:
                                output_pdf_name = f"{numero_nfe}.pdf" if numero_nfe else file_name.rsplit('/', 1)[-1].lower().replace('.xml', '.pdf')
                                pdfs_gerados.append((output_pdf_name, pdf_bytes))
                        
                        progress_value = (i + 1) / total_files
                        progress_text = f"Processando {i + 1}/{total_files} DANFEs... Por favor, aguarde."
                        progress_bar.progress(progress_value, text=progress_text)
            
            if pdfs_gerados:
                zip_output_buffer = io.BytesIO()
                with st.spinner("Compactando os arquivos PDF..."):
                    with zipfile.ZipFile(zip_output_buffer, 'w') as zf_out:
                        for pdf_name, pdf_data in pdfs_gerados:
                            zf_out.writestr(pdf_name, pdf_data)
                st.success(f"{len(pdfs_gerados)} DANFEs gerados com sucesso!")
                st.download_button(
                    label="⬇️ Baixar todos os DANFEs (.zip)",
                    data=zip_output_buffer.getvalue(),
                    file_name="DANFEs_gerados.zip",
                    mime="application/zip"
                )

        else:
            # Se não for ZIP, tenta identificar como XML
            file_buffer.seek(0)
            xml_bytes = file_buffer.read()
            is_xml = False
            try:
                etree.fromstring(xml_bytes)
                is_xml = True
            except etree.XMLSyntaxError:
                is_xml = False

            if is_xml:
                st.info("Arquivo XML detectado pelo conteúdo. Processando...")
                with st.spinner('Gerando o DANFE...'):
                    numero_nfe, _ = extrair_dados_xml(xml_bytes)
                    danfeGerador = DanfeGerador(xml_bytes)
                    pdf_bytes = danfeGerador.create_danfe()

                    if pdf_bytes:
                        st.success("DANFE gerado com sucesso!")
                        output_filename = f"{numero_nfe}.pdf" if numero_nfe else uploaded_file.name + '.pdf'
                        st.download_button(
                            label="⬇️ Baixar DANFE (.pdf)",
                            data=pdf_bytes,
                            file_name=output_filename,
                            mime="application/pdf"
                        )
                    else:
                        st.error("A geração do DANFE não retornou um resultado válido.")
            else:
                st.error("Arquivo inválido. O conteúdo não parece ser de um arquivo XML ou ZIP suportado.")

    except Exception as e:
        st.error(f"Ocorreu um erro ao processar o arquivo: {e}")
        traceback_details = traceback.format_exc()
        st.code(traceback_details, language='text')

else:
    if not submitted:
        st.info("Por favor, carregue um arquivo e clique em 'Processar Documento(s)' para começar.")

st.markdown("---")
st.markdown(
    "<p style='text-align: center; font-size: 14px; color: grey;'>Desenvolvido por ALEX VARELA.</p>",
    unsafe_allow_html=True
)