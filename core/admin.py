# Register your models here.
from django.contrib import admin
from .models import Person
from .models import SkillClass, Skill, PersonHasSkill
from .models import IntInfluencer, PersonIntInfluencer
from .models import IntCompany, PersonIntCompany
from .models import IntSchool, PersonIntSchool
from .models import IntGroup, PersonIntGroup
from .models import Activity, ResearchArea
from .models import Education, Experience
from .models import Organization, OrgHasPerson
from .models import Sector, OrgHasSector, Friend


admin.site.register(Person)
admin.site.register(SkillClass)
admin.site.register(Skill)
admin.site.register(PersonHasSkill)
admin.site.register(IntInfluencer)
admin.site.register(PersonIntInfluencer)
admin.site.register(IntCompany)
admin.site.register(PersonIntCompany)
admin.site.register(IntSchool)
admin.site.register(PersonIntSchool)
admin.site.register(IntGroup)
admin.site.register(PersonIntGroup)
admin.site.register(Activity)
admin.site.register(ResearchArea)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Organization)
admin.site.register(OrgHasPerson)
admin.site.register(Sector)
admin.site.register(OrgHasSector)
admin.site.register(Friend)