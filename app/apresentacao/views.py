from flask import render_template, abort

from app.apresentacao import apresentacao_bp

perfil = {
    'cuducos': {
        'nome': 'Eduardo Cuducos',
        'descricao': 'Sociólogo, geek, cozinheiro e fã de esportes.',
        'url': 'https://twitter.com/cuducos',
        'nome_url': 'Twitter',
        'foto': 'https://avatars.githubusercontent.com/u/4732915?v=3&s=128'
    },
    'pedro': {
        'nome': 'Pedro Sousa',
        'descricao': 'Desenvolvedor Python especializado em back-end.',
        'url': 'https://twitter.com/ppls2106',
        'nome_url': 'Twitter',
        'foto': 'https://avatars.githubusercontent.com/u/36779714?v=3&s=128'
    }
}


@apresentacao_bp.route('/<user>/')
def pagina_perfil(user):
    try:
        usuario = perfil[user]
        return render_template('home.html', perfil=usuario)
    except KeyError as e:
        abort(400, {'detail': f'Usuario {e} não existe!'})
