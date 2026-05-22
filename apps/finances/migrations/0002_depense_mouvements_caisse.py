# Generated manually for caisse movement tracking.

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='depense',
            name='type_operation',
            field=models.CharField(
                choices=[
                    ('depense', 'Dépense'),
                    ('emprunt_caisse', 'Emprunt caisse'),
                    ('remboursement_emprunt', 'Remboursement emprunt'),
                ],
                default='depense',
                max_length=30,
            ),
        ),
        migrations.AddField(
            model_name='depense',
            name='personne',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name='depense',
            name='statut_remboursement',
            field=models.CharField(
                blank=True,
                choices=[
                    ('non_rembourse', 'Non remboursé'),
                    ('partiel', 'Partiel'),
                    ('rembourse', 'Remboursé'),
                ],
                default='',
                max_length=30,
            ),
        ),
        migrations.AddField(
            model_name='depense',
            name='date_remboursement_prevue',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='depense',
            name='categorie',
            field=models.CharField(
                choices=[
                    ('carburant', 'Carburant'),
                    ('reparation', 'Réparation'),
                    ('assurance', 'Assurance'),
                    ('administratif', 'Administratif'),
                    ('personnel', 'Personnel'),
                    ('emprunt', 'Emprunt caisse'),
                    ('remboursement', 'Remboursement emprunt'),
                    ('autre', 'Autre'),
                ],
                max_length=30,
            ),
        ),
    ]
