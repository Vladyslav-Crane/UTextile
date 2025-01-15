import os
from django.conf import settings
from django.db import migrations


def fix_images_path(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    Category = apps.get_model("catalog", "Category")
    Fabric = apps.get_model("catalog", "Fabric")
    for obj in [*Fabric.objects.all(), *Category.objects.all()]:
        dir, filename= os.path.split(obj.image.path)
        obj.image.name = os.path.join('/'.join(dir.split('/')[-3::]), filename)
        obj.save()

class Migration(migrations.Migration):
    dependencies = [
        ('catalog', '0002_alter_category_options_alter_fabric_options_and_more'),
    ]

    operations = [
        migrations.RunPython(fix_images_path, migrations.RunPython.noop),
    ]