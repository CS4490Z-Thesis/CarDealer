# Generated by Django 3.0.7 on 2020-07-02 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dealers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('New', 'New'), ('Used', 'Used')], max_length=50)),
                ('image_main', models.ImageField(upload_to='images')),
                ('image1', models.ImageField(blank=True, upload_to='images')),
                ('image2', models.ImageField(blank=True, upload_to='images')),
                ('image3', models.ImageField(blank=True, upload_to='images')),
                ('image4', models.ImageField(blank=True, upload_to='images')),
                ('image5', models.ImageField(blank=True, upload_to='images')),
                ('miles', models.IntegerField(blank=True, null=True)),
                ('transmission', models.CharField(choices=[('Manual', 'Manual'), ('Automatic', 'Automatic')], max_length=50)),
                ('year', models.IntegerField(choices=[(2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020)], default=2020, verbose_name='year')),
                ('power', models.IntegerField()),
                ('fuel', models.IntegerField()),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('dealer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dealers.Dealer')),
            ],
        ),
    ]
