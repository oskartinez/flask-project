from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def index():
    template_name = 'index.html'

    return render_template(template_name)

@app.route('/acerca/')
def about():
    template_name = 'about.html'

    return render_template(template_name)

    
@app.route('/cotizacion')
def cotizacion():
    template_name = 'cotizacion.html'

    res = requests.get('https://www.dolarsi.com/api/api.php?type=valoresprincipales')
    
    if res:
        print(res.json())
    else:
        print('Response Failed')

    return render_template(template_name, res=res.json())

@app.route('/blog')
def blog():
    template_name = 'blog.html'

    articulos = [
        { 
            "titulo": "¿Estudiar en el metaverso?: una universidad propone cursos de ingeniería en el mundo virtual",
            "contenido": "El desarrollo del metaverso, y sus infinitas posibilidades, está avanzando a pasos acelerados. Los mundos virtuales que empezaron siendo un espacio para los fanáticos de los videojuegos, ahora están cada vez más \"profesionalizados\" y ya se espera que se conviertan en una parte cada vez más importante de la vida social y laboral.Además, ya hay algunas propuestas educativas: la Universidad de Tokio anunció que ofrecerá una variedad de cursos sobre el metaverso, dentro del metaverso.",
            "fecha": "28-07-2022",
            "autor": "Miguel Dominguez",
            "categoria": "Educación inmersiva",
            "imagen": "https://assets.iproup.com/cdn-cgi/image/w=880,f=webp/https://assets.iproup.com/assets/jpg/2022/03/26861.jpg"
        },
        {
            "titulo": "Bomba impensada: ¿Quién es el primer futbolista argentino en ser transferido vía criptomonedas?",
            "contenido": "El fútbol encontró un nuevo aliado que cada vez se mete más de lleno en el deporte más popular del mundo: las criptomonedas.Desde estampar el nombre de un exchange o criptoactivo en la camiseta de un equipo, renombrar un torneo o adquirir las licencias de equipos y jugadores para juegos virtuales, son todas formas en las cuales esta alianza se fue consolidándo en este último tiempo.Ahora, un nuevo hito marcó a ambas industrias, luego de confirmarse la primer transferencia de un futbolista con monedas digitales en Latinoamérica.",
            "fecha": "27-07-2022",
            "autor": "Felipe Suárez",
            "categoria": "Fútbol y cripto",
            "imagen": "https://assets.iproup.com/cdn-cgi/image/w=880,f=webp/https://assets.iproup.com/assets/jpg/2021/05/19037.jpg"

        }
    ]

    return render_template(template_name, articulos=articulos)
