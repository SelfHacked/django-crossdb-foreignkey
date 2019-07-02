"""Additional functionality to models."""
from django.db.models import ForeignKey, OneToOneField, DO_NOTHING
from django.db.models.deletion import CASCADE
from django.db.models.signals import pre_delete


class CrossDBForeignKey(ForeignKey):
    """Cross database foreign key relation."""

    def __init__(self, to, *args, **kwargs):
        """
        Initialize.

        Remove the db constraint to don't verify the foreign key integrity.
        on_delete must always be DO_NOTHING
           since there is no good way to add custom on_delete methods.
        """
        self.internal_on_delete = kwargs.get('on_delete', CASCADE)
        if self.internal_on_delete not in [CASCADE, DO_NOTHING]:
            raise ValueError('Only CASCADE and DO_NOTHING is supported.')
            # SET_NULL is not supported at the moment.

        kwargs['db_constraint'] = False
        kwargs['on_delete'] = DO_NOTHING

        super().__init__(to, *args, **kwargs)

    def deconstruct(self):
        """Deconstruct."""
        name, path, args, kwargs = super().deconstruct()
        del kwargs['db_constraint']
        del kwargs['on_delete']
        return name, path, args, kwargs

    def contribute_to_class(self, cls, name, private_only=False, **kwargs):
        """Set signals to trigger for related model deletion."""
        duid = f'cross_db_delete_{cls._meta.label_lower}_{name}'
        pre_delete.connect(
            self.execute_on_delete,
            sender=self.remote_field.model,
            dispatch_uid=duid,
        )

        super().contribute_to_class(cls, name, private_only, **kwargs)

    def execute_on_delete(self, sender, instance, **kwargs):
        """Delete related objects."""
        on_delete = self.internal_on_delete
        if on_delete == DO_NOTHING:
            return

        if on_delete == CASCADE:
            related_objs = self.model.objects.filter(
                **{
                    f'{self.name}': instance,
                },
            )
            related_objs.delete()


class CrossDBOneToOneField(CrossDBForeignKey, OneToOneField):
    """Special one to one field that allows cross db relationship."""


