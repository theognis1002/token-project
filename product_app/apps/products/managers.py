from django.db.models import Manager


class SoftDeleteManager(Manager):
    def active_only(self):
        return super().get_queryset().filter(soft_delete=False)

    def deleted_set(self):
        return super().get_queryset().filter(soft_delete=True)
