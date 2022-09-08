JAZZMIN_SETTINGS = {    
    # título de la ventana (Se establecerá de forma predeterminada en 
    # current_admin_site.site_title si está ausente o Ninguno)
    "site_title": "STYLE TATTO Admin",

    # Título en la pantalla de inicio de sesión (19 caracteres como máximo) 
    # (predeterminado en current_admin_site.site_header si está ausente o Ninguno)
    "site_header": "STYLE TATTO",
    
    "site_brand": "STYLE TATTO",


    # clases de CSS que se aplican al logotipo de arriba
    "site_logo_classes": "img-circle",

    # Ruta relativa a un favicon para su sitio, por defecto será site_logo si 
    # está ausente (idealmente 32x32 px)
    "site_icon": None,

    # Texto de bienvenida en la pantalla de inicio de sesión
    "welcome_sign": "bienvenido a STYLE TATTO",

    # Copyright on the footer
    "copyright": "STYLE TATTO",

    # El administrador del modelo para buscar desde la barra de búsqueda, 
    # la barra de búsqueda se omite si se excluye
    "search_model": "auth.User",

    # Nombre de campo en el modelo de usuario que contiene avatar 
    # ImageField/URLField/Charfield o un invocable que recibe al usuario
    "user_avatar": None,

    ############
    # Top Menu #
    ############

    # Enlaces para poner a lo largo del menú superior
    "topmenu_links": [
        
        {"name": "Home Admin",  "url": "admin:index", "permissions": ["auth.view_user"]},

        {"name": "Style Tatto", "url": "http://127.0.0.1:8000/", "new_window": True},

        {"model": "auth.User"},

        {"app": "books"},
    ],

    #############
    # User Menu #
    #############

    # Enlaces adicionales para incluir en el menú de usuario en la parte superior 
    # derecha (no se permite el tipo de URL de "aplicación")
        "usermenu_links": [
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.user"}
    ],

    #############
    # Side Menu #
    #############

    # Ya sea para mostrar el menú lateral
    "show_sidebar": True,

    # Ya sea para aut expandir el menú
    "navigation_expanded": True,

    # Ocultar estas aplicaciones al generar el menú lateral, por ejemplo (autorización)
    "hide_apps": [],

    # Oculte estos modelos al generar el menú lateral (por ejemplo, auth.user)
    "hide_models": [],

    # Lista de aplicaciones (y/o modelos) para el pedido del menú lateral base 
    # (no es necesario que contenga todas las aplicaciones/modelos)
    "order_with_respect_to": ["auth", "books", "books.author", "books.book"],

    # Enlaces personalizados para agregar a grupos de aplicaciones, 
    # Ingresados ​​en el nombre de la aplicación
    "custom_links": {
        "books": [{
            "name": "Make Messages", 
            "url": "make_messages", 
            "icon": "fas fa-comments",
            "permissions": ["books.view_book"]
        }]
    },

    # Íconos personalizados para aplicaciones/modelos del menú lateral 
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    
    # Iconos que se usan cuando uno no se especifica manualmente
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    #################
    # Related Modal #
    #################
    # Use modales en lugar de ventanas emergentes
    "related_modal_active": False,

    #############
    # UI Tweaks #
    #############

    # Rutas relativas a scripts CSS/JS personalizados 
    # (deben estar presentes en archivos estáticos) "custom_css": None,
    "custom_js": None,
    
    # Si mostrar el personalizador de IU en la barra lateral
    "show_ui_builder": False,

    "changeform_format": "horizontal_tabs",
    # anular los formularios de cambio según el administrador del modelo
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},


    "custom_css": "/StyleTatto/StyleTatto/css/style.css",
}
