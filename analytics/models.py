from __future__ import unicode_literals

from django.db import models
import xlrd

class ScholarshipInfo(models.Model):
    id_bolsa = models.AutoField(primary_key=True)
    vl_ano = models.IntegerField()
    nm_estado = models.CharField(max_length=2)
    nm_municipio = models.CharField(max_length=64)
    nm_programa_fomento = models.CharField(max_length=32)
    nm_instituicao_ensino_superior = models.CharField(max_length=32)
    nm_programa = models.CharField(max_length=64)
    nm_area_avaliacao = models.CharField(max_length=64)
    nm_area_conhecimento = models.CharField(max_length=64)
    nm_grande_area = models.CharField(max_length=64)
    vl_coordenador_geral_isf = models.IntegerField()
    vl_coordenador_pedagogico_isf = models.IntegerField()
    vl_coordenador_centro_isf = models.IntegerField()
    vl_doutorado = models.IntegerField()
    vl_iniciacao_cientifica = models.IntegerField()
    vl_mestrado = models.IntegerField()
    vl_mestrado_profissional = models.IntegerField()
    vl_professor_nacional_senior = models.IntegerField()
    vl_professor_isf = models.IntegerField()
    vl_pos_doc = models.IntegerField()
    vl_supervisao = models.IntegerField()

    class Meta:
        db_table = 'ScholarshipInfo'
        verbose_name = 'Bolsa de Estudo'
        verbose_name_plural = 'Bolsas de Estudos'

class DataFile(models.Model):
    id_file = models.AutoField(primary_key=True)
    data = models.FileField()

    def save(self, *args, **kwargs):
        super(DataFile, self).save(*args, **kwargs)
        filename = self.data.path
        book = xlrd.open_workbook(filename)
        sheet = book.sheet_by_index(0)
        print(sheet.nrows)
        print(sheet.ncols)

    class Meta:
        db_table = 'DataFile'
        managed = True
        verbose_name = 'Upload Planilha Bolsa de Estudos'
        verbose_name_plural = 'Importação'
