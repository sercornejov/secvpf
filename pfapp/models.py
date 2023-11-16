from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.validators import MaxValueValidator, MinValueValidator

# model to store personal information
class Geninfo(models.Model):
  firstname = models.CharField(max_length=50, null=True, blank=True, verbose_name='First Name')
  lastname = models.CharField(max_length=50, null=True, blank=True, verbose_name='Last Name')
  profession = models.CharField(max_length=80,null=True, blank=True, verbose_name='Profession')
  birthday=models.DateField(null=True, blank=True, verbose_name='Birthday')
  introphrase = models.TextField(null=True, blank=True, verbose_name='Introduction phrase')
  introtext = models.TextField(null=True, blank=True, verbose_name='Introduction paragraph')
  logo=models.ImageField(default='users/logo_default.jpg', upload_to='users/', verbose_name='User logo')
  photo=models.ImageField(default='users/user_default.jpg', upload_to='users/', verbose_name='user photo')
  user=models.OneToOneField(User, on_delete=models.CASCADE, related_name='geninfo', verbose_name='Usuario')
  
  class Meta:
    verbose_name = 'perfil'
    verbose_name_plural = 'perfiles'
    ordering=['-id']

  def __str__(self):
    return f"{self.user.username}{self.firstname} {self.lastname} {self.profession}"

def create_user_geninfo(sender,instance,created,**kwargs):
  if created:
    Geninfo.objects.create(user=instance)

def save_user_geninfo(sender,instance, **kwargs):
  instance.geninfo.save()

post_save.connect(create_user_geninfo,sender=User)
post_save.connect(save_user_geninfo,sender=User)

class Skills(models.Model):
  sk01name = models.CharField(max_length=150, null=True, blank=True, verbose_name='Skill 01')
  sk01x100 = models.PositiveIntegerField(default=50, validators=[MinValueValidator(1), MaxValueValidator(100)])
  sk02name = models.CharField(max_length=150, null=True, blank=True, verbose_name='Skill 02')
  sk02x100 = models.PositiveIntegerField(default=50, validators=[MinValueValidator(1), MaxValueValidator(100)])
  sk03name = models.CharField(max_length=150, null=True, blank=True, verbose_name='Skill 03')
  sk03x100 = models.PositiveIntegerField(default=50, validators=[MinValueValidator(1), MaxValueValidator(100)])
  sk04name = models.CharField(max_length=150, null=True, blank=True, verbose_name='Skill 04')
  sk04x100 = models.PositiveIntegerField(default=50, validators=[MinValueValidator(1), MaxValueValidator(100)])
  sk05name = models.CharField(max_length=150, null=True, blank=True, verbose_name='Skill 05')
  sk05x100 = models.PositiveIntegerField(default=50, validators=[MinValueValidator(1), MaxValueValidator(100)])
  sk06name = models.CharField(max_length=150, null=True, blank=True, verbose_name='Skill 06')
  sk06x100 = models.PositiveIntegerField(default=50, validators=[MinValueValidator(1), MaxValueValidator(100)])
  sk07name = models.CharField(max_length=150, null=True, blank=True, verbose_name='Skill 07')
  sk07x100 = models.PositiveIntegerField(default=50, validators=[MinValueValidator(1), MaxValueValidator(100)])
  sk08name = models.CharField(max_length=150, null=True, blank=True, verbose_name='Skill 08')
  sk08x100 = models.PositiveIntegerField(default=50, validators=[MinValueValidator(1), MaxValueValidator(100)])
  sk09name = models.CharField(max_length=150, null=True, blank=True, verbose_name='Skill 09')
  sk09x100 = models.PositiveIntegerField(default=50, validators=[MinValueValidator(1), MaxValueValidator(100)])
  sk10name = models.CharField(max_length=150, null=True, blank=True, verbose_name='Skill 10')
  sk10x100 = models.PositiveIntegerField(default=50, validators=[MinValueValidator(1), MaxValueValidator(100)])
  user=models.OneToOneField(User, on_delete=models.CASCADE, related_name='skills', verbose_name='Usuario')
  
def create_user_skills(sender,instance,created,**kwargs):
  if created:
    Skills.objects.create(user=instance)

def save_user_skills(sender,instance, **kwargs):
  instance.skills.save()

post_save.connect(create_user_skills,sender=User)
post_save.connect(save_user_skills,sender=User)

class Projects(models.Model):
  pr01name=models.CharField(max_length=150, null=True, blank=True, verbose_name='Project 01')
  pr01description=models.TextField(null=True, blank=True, verbose_name='Project 01 description')
  pr01pho01=models.ImageField(default='users/user_default.jpg', upload_to='users/', verbose_name='Project 01 photo 01')
  pr01pho02=models.ImageField(default='users/user_default.jpg', upload_to='users/', verbose_name='Project 01 photo 02')
  pr01pho03=models.ImageField(default='users/user_default.jpg', upload_to='users/', verbose_name='Project 01 photo 03')
  pr01pho04=models.ImageField(default='users/user_default.jpg', upload_to='users/', verbose_name='Project 01 photo 04')
  pr01pho05=models.ImageField(default='users/user_default.jpg', upload_to='users/', verbose_name='Project 01 photo 05')
  pr02name=models.CharField(max_length=150, null=True, blank=True, verbose_name='Project 02')
  pr02description=models.TextField(null=True, blank=True, verbose_name='Project 02 description')
  pr02pho01=models.ImageField(default='users/user_default.jpg', upload_to='users/', verbose_name='Project 02 photo 01')
  pr02pho02=models.ImageField(default='users/user_default.jpg', upload_to='users/', verbose_name='Project 02 photo 02')
  pr02pho03=models.ImageField(default='users/user_default.jpg', upload_to='users/', verbose_name='Project 02 photo 03')
  pr02pho04=models.ImageField(default='users/user_default.jpg', upload_to='users/', verbose_name='Project 02 photo 04')
  pr02pho05=models.ImageField(default='users/user_default.jpg', upload_to='users/', verbose_name='Project 02 photo 05')
  pr03name=models.CharField(max_length=150, null=True, blank=True, verbose_name='Project 03')
  pr03description=models.TextField(null=True, blank=True, verbose_name='Project 03 description')
  pr03pho01=models.ImageField(default='users/user_default.jpg', upload_to='users/', verbose_name='Project 03 photo 01')
  pr03pho02=models.ImageField(default='users/user_default.jpg', upload_to='users/', verbose_name='Project 03 photo 02')
  pr03pho03=models.ImageField(default='users/user_default.jpg', upload_to='users/', verbose_name='Project 03 photo 03')
  pr03pho04=models.ImageField(default='users/user_default.jpg', upload_to='users/', verbose_name='Project 03 photo 04')
  pr03pho05=models.ImageField(default='users/user_default.jpg', upload_to='users/', verbose_name='Project 03 photo 05')
  pr04name=models.CharField(max_length=150, null=True, blank=True, verbose_name='Project 04')
  pr04description=models.TextField(null=True, blank=True, verbose_name='Project 04 description')
  pr04pho01=models.ImageField(default='users/user_default.jpg', upload_to='users/', verbose_name='Project 04 photo 01')
  pr04pho02=models.ImageField(default='users/user_default.jpg', upload_to='users/', verbose_name='Project 04 photo 02')
  pr04pho03=models.ImageField(default='users/user_default.jpg', upload_to='users/', verbose_name='Project 04 photo 03')
  pr04pho04=models.ImageField(default='users/user_default.jpg', upload_to='users/', verbose_name='Project 04 photo 04')
  pr04pho05=models.ImageField(default='users/user_default.jpg', upload_to='users/', verbose_name='Project 04 photo 05')
  user=models.OneToOneField(User, on_delete=models.CASCADE, related_name='projects', verbose_name='Usuario')

def create_user_projects(sender,instance,created,**kwargs):
  if created:
    Projects.objects.create(user=instance)

def save_user_projects(sender,instance, **kwargs):
  instance.projects.save()

post_save.connect(create_user_projects,sender=User)
post_save.connect(save_user_projects,sender=User)