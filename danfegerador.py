import io
from brazilfiscalreport.danfe import Danfe 


class DanfeGerador:

    
    def __init__(self, xml_content:str | bytes):
            if isinstance(xml_content, str):
                self.xml_bytes = xml_content.encode('utf-8')
            else:
                self.xml_bytes = xml_content


    def create_danfe(self) -> bytes | None: 
        #Gera o DANFE em formato PDF e retorna seu conteúdo como um objeto de bytes.

        try:
            buffer = io.BytesIO() # Cria um buffer (arquivo em memória) para receber os dados do PDF.
            danfe = Danfe(self.xml_bytes) # Instancia o objeto Danfe com o XML.
            danfe.output(buffer) # # Gera o PDF, direcionando a saída para o buffer em memória.
            pdf_bytes = buffer.getvalue() # Obtém o conteúdo completo do buffer como bytes.
            buffer.close() # Fecha o buffer para liberar recursos.

            print("DANFE gerado em memória com sucesso.")
            return pdf_bytes

        except Exception as e:
            print(f"Erro ao gerar DANFE em memória: {e}")
            return None