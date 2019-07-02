"""Database routing."""


class AppRouter(object):
    """
    Master Database Router for project.

    Implements standard router methods:
    https://docs.djangoproject.com/en/2.1/topics/db/multi-db/#using-routers
    """

    def db_for_read(self, model, **hints):
        """Routing for db reads."""
        if model._meta.model_name.startswith('other'):
            return 'other'
        else:
            return 'default'

    def db_for_write(self, model, **hints):
        """Routing for db writes."""
        if model._meta.model_name.startswith('other'):
            return 'other'
        else:
            return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """Whether relations should be allowed in single querysets."""
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Whether migration file should be applied to DB during migrate."""
        if model_name.startswith('other'):
            return db == 'other'
        else:
            return db == 'default'
