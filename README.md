## Proyectos de Web Scraping con Scrapy, Selenium y Automatización RPA 
### Repositorio que reúne ejemplos prácticos y demos de dos tecnologías: Scrapy y Selenium.
#### 🔍 Web Scraping con Scrapy: El framework Scrapy es implementado al extraer datos de renting de un producto en una página de acceso abierto en el dominio de Netcorporate
#### 🌐 Web Scraping con Selenium: Las herramientas de Selenium facilitan aun más la extración de datos en páginas web sacrificando el tiempo de ejecución a grandes cantidades de datos.
#### 🤖 Automatización RPA con Selenium: Desarrollar tareas repetitivas para la extracción de datos en páginas protegidas con el dominio PyWombat.
## Crear entorno virtual e instalar librerías
#### Para entornos Conda :
```
conda create --name <env> --file requirements.txt
``` 
## Ejecución de programa
#### Este repositorio cuenta con dos scripts, en `spider_web/spiders`
### `netcorporate.py`
#### Extrae datos de un producto de renting en el dominio Netcorporate usando el framework Scrapy
###### El resultado se muestra en la consola :

```
scrapy crawl netcorporate
``` 
###### Resultado importado en archivo csv :

```
scrapy crawl netcorporate -o producto.csv
```
###### Resultado importado en archivo json :
```
scrapy crawl netcorporate -o producto.json
```
---
### `rpa_scrapy_test.py`
#### Extrae datos de una lista de ejercicios realizados en una página protegida del dominio PyWombat usando Selenium.
##### Antes de ejecutar el script debe ingresar credenciales válidas de `USERNAME` y `PASSWORD` en el archivo `spider_web/vars.py` para iniciar sesión.
###### El resultado se muestra en la consola :

```
scrapy crawl rpa_scrapy_test
``` 
###### Resultado importado en archivo csv :

```
scrapy crawl rpa_scrapy_test -o data.csv
```
###### Resultado importado en archivo json :
```
scrapy crawl rpa_scrapy_test -o data.json
```
#### Los comandos deben ejecutarse en la ruta root, a nivel del archivo `scrapy.cfg`.
