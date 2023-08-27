import scrapy


class NetcorporateSpider(scrapy.Spider):
    name = "netcorporate"
    allowed_domains = ["app.netcorporate.net:81/Renting/"]
    start_urls = ["http://app.netcorporate.net:81/Renting/PC0C69ZF.html"]

    def parse(self, response):
        try:
            if response.status == 200:
                # Obtener datos str de html no procesados
                serie_np = response.xpath('//center/h3/text()').get()
                marca_np = response.xpath('//center/p[1]/text()').get()
                modelo_np = response.xpath('//center/p[2]/text()').get()
                p_n_np = response.xpath('//center/p[3]/text()').get()
                imagenes = response.xpath('//div[@class="thumbnail_container"]/img')
                file_imagenes_np = imagenes.xpath('@src').getall()

                # procesar datos
                serie = self.get_data(serie_np)
                marca = self.get_data(marca_np)
                modelo = self.get_data(modelo_np)
                p_n = self.get_data(p_n_np)
                url = self.create_url(f'{serie}.php')
                imgs = []
                for file in file_imagenes_np:
                    ruta = self.create_url(file)
                    imgs.append(ruta)

                # importar datos
                yield {
                    'serie': serie,
                    'url': url,
                    'marca': marca,
                    'modelo': modelo,
                    'p/n': p_n,
                    'img': imgs,
                }
            else:
                self.logger.warning(f'La página no está disponible. Status: {response.status}')
        except Exception as e:
            self.logger.error(f'Error en la solicitud: {e}')

    # limpiar valores no requeridos y espacios
    def get_data(self, htmlStr):
        data = htmlStr.split(':', 1)[-1].strip()
        return data

    # construir url con el dominio netcorporate.net
    def create_url(self, file):
        ruta_img = "http://"+self.allowed_domains[0]
        url_img = ruta_img + file
        return url_img