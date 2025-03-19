class OracleRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'ZepterPortal':  # Замените на ваше приложение
            return 'oracle'
        return None

    def db_for_write(self, model, **hints):
        return None  # Запрет записи в Oracle

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if db == 'oracle':
            return False  # Запрет миграций для Oracle
        return None