from __future__ import unicode_literals

from django.db import models
import xlrd
from numpy.core.tests.test_umath_complex import check_complex_value
from skimage.filters.edges import scharr

import scholarship


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
        filename = self.data.path
        book = xlrd.open_workbook(filename)
        sheet = book.sheet_by_index(0)

        for row in range(sheet.nrows):
            if row != 0:
                scholarship_info = ScholarshipInfo()
                scholarship_info.vl_ano = self.__check_value(sheet.cell_value(row, 0))
                scholarship_info.nm_estado = self.__check_name(sheet.cell_value(row,1))
                scholarship_info.nm_municipio = self.__check_name(sheet.cell_value(row, 2))
                scholarship_info.nm_programa_fomento = self.__check_name(sheet.cell_value(row, 5))
                scholarship_info.nm_instituicao_ensino_superior = self.__check_name(sheet.cell_value(row, 6))
                scholarship_info.nm_programa = self.__check_name(sheet.cell_value(row, 8))
                scholarship_info.nm_area_avaliacao = self.__check_name(sheet.cell_value(row, 9))
                scholarship_info.nm_area_conhecimento = self.__check_name(sheet.cell_value(row, 10))
                scholarship_info.nm_grande_area = self.__check_name(sheet.cell_value(row, 11))
                scholarship_info.vl_coordenador_geral_isf = self.__check_value(sheet.cell_value(row, 12))
                scholarship_info.vl_coordenador_pedagogico_isf = self.__check_value(sheet.cell_value(row, 13))
                scholarship_info.vl_coordenador_centro_isf = self.__check_value(sheet.cell_value(row, 14))
                scholarship_info.vl_doutorado = self.__check_value(sheet.cell_value(row, 15))
                scholarship_info.vl_iniciacao_cientifica = self.__check_value(sheet.cell_value(row, 16))
                scholarship_info.vl_mestrado = self.__check_value(sheet.cell_value(row, 17))
                scholarship_info.vl_mestrado_profissional = self.__check_value(sheet.cell_value(row, 18))
                scholarship_info.vl_professor_nacional_senior = self.__check_value(sheet.cell_value(row, 19))
                scholarship_info.vl_professor_isf = self.__check_value(sheet.cell_value(row, 20))
                scholarship_info.vl_pos_doc = self.__check_value(sheet.cell_value(row, 21))
                scholarship_info.vl_supervisao = self.__check_value(sheet.cell_value(row, 22))
                scholarship_info.save()

        super(DataFile, self).save(*args, **kwargs)


    def __check_value(self, value):
        if value == "":
            return 0
        return value

    def __check_name(self, value):
        if value == "":
            return "INDEFINIDO"
        return value

    class Meta:
        db_table = 'DataFile'
        managed = True
        verbose_name = 'Upload Planilha Bolsa de Estudos'
        verbose_name_plural = 'Importação'
