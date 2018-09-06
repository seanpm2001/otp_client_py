from ott.utils.svr.pyramid.app_config import AppConfig

import logging
log = logging.getLogger(__file__)


def main(global_config, **ini_settings):
    """
    this function is the main entry point for pserve / Pyramid
    it returns a Pyramid WSGI application
    see setup.py entry points + config/*.ini [app:main] ala pserve (e.g., bin/pserve config/development.ini)
    """
    #import pdb; pdb.set_trace()
    app = AppConfig(**ini_settings)

    from gtfsdb import Database
    from zope.sqlalchemy import ZopeTransactionExtension
    kw = app.gtfsdb_param_from_config()
    kw['session_extenstion'] = ZopeTransactionExtension()
    db = Database(**kw)
    app.set_db(db)

    import views
    app.config_include_scan(views)

    return app.make_wsgi_app()
