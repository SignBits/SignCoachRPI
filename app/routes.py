def register_routes(api, app, root='api'):
    from app.fingerspell import register_routes as attach_fingerspell_endpoints
    from app.info import register_routes as attach_info_endpoints

    attach_fingerspell_endpoints(api, app)
    attach_info_endpoints(api, app)
