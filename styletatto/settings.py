import os
import dj_database_url
from pathlib import Path
from django.conf.global_settings import LANGUAGES 

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-k(-vwh84!+*p#1kf&8j2m5a#4@$d%2vuu8x^5p+b2g6a5@rir8"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    "corsheaders",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "tatto",
    "tattoDis",
    "accounts",
    "quotes",
    "Portafolio",
    "rest_framework",
    'rest_framework_simplejwt',
    'rest_framework.authtoken',
    'colorfield',
    'django_rest_passwordreset',

]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",

]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:3001",
    'http://127.0.0.1:3000',
]


CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]

ROOT_URLCONF = "styletatto.urls"

AUTH_USER_MODEL = "accounts.Users"

REST_FRAMEWORK = {
    'NON_FIELD_ERRORS_KEY': "error",

    'DEFAULT_AUTHENTICATION_CLASSES': (
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "styletatto.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(
        #Dairon
        default = 'mysql://root:123456@localhost:3306/styletattoo',  
        #Steven
        #default = 'mysql://root:@localhost:3306/styletattoo',
        conn_max_age = 6007
    )
}



# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'es-col'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True




BASE_DIR = Path(__file__).resolve().parent.parent

# IMPORTANCION DE LA IMG
STATICFILES_DIRS =[os.path.join(BASE_DIR, 'static')]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

if not DEBUG:   
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# MODIFICACIONES DEL ADMIN *IMPORTANTE*

JAZZMIN_SETTINGS = {   

    # título de la ventana (Se establecerá de forma predeterminada en 
    # current_admin_site.site_title si está ausente o Ninguno)
    "site_title": "STYLE TATTO Admin",

    # Título en la pantalla de inicio de sesión (19 caracteres como máximo) 
    # (predeterminado en current_admin_site.site_header si está ausente o Ninguno)
    "site_header": "STYLE TATTO",
    
    "site_brand": "STYLE TATTO",

    #IMG LOGO
    "site_logo":"img/logoStyle.jpg" ,

    # Ruta relativa a un favicon para su sitio, por defecto será site_logo 
    # está ausente (idealmente 32x32 px)
    "site_icon": None,

    # Texto de bienvenida en la pantalla de inicio de sesión
    "welcome_sign": "Administrador StyleTattoo",

    # Copyright on the footer
    "copyright": "StyleTattoo",

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

        {"model": "auth.User"},

        {"app": "books"},
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
    
    # Si mostrar el personalizador de IU en la barra lateral
    "show_ui_builder": False,

    "changeform_format": "horizontal_tabs",
    # anular los formularios de cambio según el administrador del modelo
    "changeform_format_overrides": {
        "auth.user": "collapsible", 
        "auth.group": "vertical_tabs"
        },

    # Rutas relativas a scripts CSS/JS personalizados 
    "custom_css": "./css/style.css",

    # (deben estar presentes en archivos estáticos) "custom_css": None,
    "custom_js": None,
}    

# donde se almacenan los archivos
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
