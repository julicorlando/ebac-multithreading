from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200, verbose_name="título")),
                (
                    "slug",
                    models.SlugField(
                        blank=True,
                        max_length=220,
                        unique=True,
                        verbose_name="slug",
                    ),
                ),
                ("content", models.TextField(verbose_name="conteúdo")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="criado em"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="atualizado em"),
                ),
            ],
            options={
                "verbose_name": "post",
                "verbose_name_plural": "posts",
                "ordering": ("-created_at",),
            },
        ),
    ]
