def register_routes(api, app, root='api'):
    from app.fingerspell import register_routes as attach_fingerspell_endpoints

    attach_fingerspell_endpoints(api, app)