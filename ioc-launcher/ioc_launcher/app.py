from aiohttp import web
from docker import Client

from .launcher import Launcher


async def create_container_handler(request):
    launch_config = request.app['launch_config']
    container_id = await request.app['launcher'].launch(**launch_config)
    return web.Response(text=container_id)


def create_app():
    app = web.Application()
    configure_app(app)
    add_routes(app)
    return app


def configure_app(app):
    app['launcher'] = Launcher(docker_client=Client(), max_workers=4)
    app['launch_config'] = dict(image='pyepics-workshop-ioc',
                                network='pyepics-workshop',
                                tty=True)


def add_routes(app):
    app.router.add_post('/new', create_container_handler)


def main():
    app = create_app()
    web.run_app(app)
