from django.shortcuts import render

def index(request):
    return render(request, "index.html")
def sobre(request):

    informacoes = [{

        'titulo': 'O Castelo Animado',

        'ano': 2004,

        'diretor': 'Hayao Miyazaki'}

    ]

    return render(request, 'sobre.html', {
        'informacoes' : informacoes
    })

def elenco(request):

    personagens = [
        {
            'nome': 'Sophie Hatter',
            'dublador': 'Patrícia Scalvi',
            'imagem': 'imgs/sophie.jpeg'
        },

        {
            'nome': 'Calcifer',
            'dublador': 'Élcio Sodré',
            'imagem': 'imgs/calcifer.jpeg'
        },

        {
            'nome': 'Howl',
            'dublador': 'Marcelo Campos',
            'imagem': 'imgs/howl.jpeg'
        },
        
        {
            'nome': 'Madame Suliman',
            'dublador': 'Adriana Pissardini',
            'imagem': 'imgs/suliman.jpeg'
        },

         {
            'nome': 'principe justin',
            'dublador': 'Márcio Araújo',
            'imagem': 'imgs/justin.jpeg'
        },

        {
            'nome': 'Markl',
            'dublador': 'Pedro Alcântara',
            'imagem': 'imgs/michael.jpeg'
        },
        {
            'nome': 'Bruxa da Terra Abandonada',
            'dublador': 'Isaura Gomes',
            'imagem': 'imgs/witch.jpeg'
        },
        {
            'nome': 'Fanny Hatter',
            'dublador': 'Cecilia Lemes',
            'imagem': 'imgs/fanny.jpeg'
        },
        {
            'nome': 'Lettie Hatter',
            'dublador': 'Angélica Santos',
            'imagem': 'imgs/lettie.jpeg'
        },



        
    ]

    return render(request, 'elenco.html', {
        'personagens': personagens
    })
def autoras(request):

    autoras = [

        {
            'nome': 'Anna Vitória',
            'funcao': 'Desenvolvimento',
            'descricao': 'Desenvolvimento do projeto - front-end e back-end',
            'tecnologias': 'HTML, CSS, Bootstrap e Django'
        },

        {
            'nome': 'Camily Zipóra',
            'funcao': 'Desenvolvimento',
            'descricao': 'Desenvolvimento do projeto - front-end e back-end',
            'tecnologias': 'HTML, CSS, Bootstrap e Django'
        }

    ]

    return render(request, 'autoras.html', {
        'autoras': autoras
    })