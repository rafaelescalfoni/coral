# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=45)
    job_present = models.CharField(max_length=500, blank=True, null=True)
    job_present_org = models.CharField(max_length=300, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    organization_id = models.IntegerField()
    linkedin = models.CharField(max_length=255)
    lattes = models.CharField(max_length=255)
    higher_education = models.IntegerField()

    class Meta:
        db_table = 'person'


class SkillClass(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'skill_class'


class Skill(models.Model):
    name = models.CharField(max_length=300)
    class_field = models.CharField(db_column='class', max_length=45, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    skill_class = models.ForeignKey('SkillClass', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'skill'


class PersonHasSkill(models.Model):
    person = models.ForeignKey(Person, models.DO_NOTHING, primary_key=True)
    skill = models.ForeignKey('Skill', models.DO_NOTHING)
    qtd = models.IntegerField()

    class Meta:
        db_table = 'person_has_skill'
        unique_together = (('person', 'skill'),)


class IntInfluencer(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        db_table = 'int_influencer'


class PersonIntInfluencer(models.Model):
    person = models.ForeignKey(Person, models.DO_NOTHING, primary_key=True)
    int_influencer = models.ForeignKey(IntInfluencer, models.DO_NOTHING)

    class Meta:
        db_table = 'person_int_influencer'
        unique_together = (('person', 'int_influencer'),)


class IntCompany(models.Model):
    name = models.CharField(max_length=150)
    class_field = models.CharField(db_column='class', max_length=100, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    description = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'int_company'


class PersonIntCompany(models.Model):
    person = models.ForeignKey(Person, models.DO_NOTHING, primary_key=True)
    int_company = models.ForeignKey(IntCompany, models.DO_NOTHING)

    class Meta:
        db_table = 'person_int_company'
        unique_together = (('person', 'int_company'),)


class IntSchool(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        db_table = 'int_school'


class PersonIntSchool(models.Model):
    person = models.ForeignKey(Person, models.DO_NOTHING, primary_key=True)
    int_school = models.ForeignKey(IntSchool, models.DO_NOTHING)

    class Meta:
        db_table = 'person_int_school'
        unique_together = (('person', 'int_school'),)


class IntGroup(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        db_table = 'int_group'


class PersonIntGroup(models.Model):
    person = models.ForeignKey(Person, models.DO_NOTHING, primary_key=True)
    int_group = models.ForeignKey(IntGroup, models.DO_NOTHING)

    class Meta:
        db_table = 'person_int_group'
        unique_together = (('person', 'int_group'),)


class Activity(models.Model):
    id = models.IntegerField(primary_key=True)
    action = models.CharField(max_length=45, blank=True, null=True)
    friend_name = models.CharField(max_length=200, blank=True, null=True)
    friend_linkedin_url = models.CharField(db_column='friend_linkedIn_url', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    person = models.ForeignKey('Person', models.DO_NOTHING)

    class Meta:
        db_table = 'activity'
        unique_together = (('id', 'person'),)


class ResearchArea(models.Model):
    group = models.CharField(max_length=100)
    class_field = models.CharField(db_column='class', max_length=100)  # Field renamed because it was a Python reserved word.
    sub_class = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'research_area'


class Education(models.Model):
    title = models.CharField(max_length=45)
    institution = models.CharField(max_length=200)
    year_start = models.IntegerField()
    year_end = models.IntegerField(blank=True, null=True)
    month_start = models.IntegerField(blank=True, null=True)
    month_end = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    research_area = models.ForeignKey('ResearchArea', models.DO_NOTHING, blank=True, null=True)
    person = models.ForeignKey('Person', models.DO_NOTHING)
    weight = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'education'


class Experience(models.Model):
    role = models.CharField(max_length=150)
    organization = models.CharField(max_length=150)
    year_start = models.IntegerField(blank=True, null=True)
    year_end = models.IntegerField(blank=True, null=True)
    month_start = models.IntegerField(blank=True, null=True)
    month_end = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    person = models.ForeignKey('Person', models.DO_NOTHING)
    person_organization_id = models.IntegerField()
    location = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        db_table = 'experience'
        unique_together = (('id', 'person', 'person_organization_id'),)


class Organization(models.Model):
    name = models.CharField(max_length=150)
    type = models.CharField(max_length=45, blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    geo_lat = models.FloatField(blank=True, null=True)
    geo_lng = models.FloatField(blank=True, null=True)
    ecobuilder = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    logo = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        db_table = 'organization'


class OrgHasPerson(models.Model):
    organization = models.ForeignKey('Organization', models.DO_NOTHING, primary_key=True)
    person = models.ForeignKey('Person', models.DO_NOTHING)
    function = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    year_start = models.IntegerField(blank=True, null=True)
    year_end = models.IntegerField(blank=True, null=True)
    month_start = models.IntegerField(blank=True, null=True)
    month_end = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'org_has_person'
        unique_together = (('organization', 'person'),)


class Sector(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'sector'


class OrgHasSector(models.Model):
    organization = models.ForeignKey('Organization', models.DO_NOTHING, primary_key=True)
    sector = models.ForeignKey('Sector', models.DO_NOTHING)

    class Meta:
        db_table = 'org_has_sector'
        unique_together = (('organization', 'sector'),)


class Friend(models.Model):
    person = models.ForeignKey('Person', models.DO_NOTHING, related_name='friend_person_person')
    friend = models.ForeignKey('Person', models.DO_NOTHING, related_name='friend_person_friend')
    qtd = models.IntegerField(default=0)

    class Meta:
        db_table = 'friend'
        unique_together = (('person', 'friend'),)

# class User(models.Model):
#     username = models.CharField(unique=True, max_length=45)
#     password = models.CharField(max_length=50)
#     email = models.CharField(max_length=500)
#     profile = models.CharField(max_length=45)
#     avatar = models.CharField(max_length=256, blank=True, null=True)
#     person = models.ForeignKey(Person, models.DO_NOTHING)

#     class Meta:
        # db_table = 'user'
#         unique_together = (('id', 'person'),)
