from django.db import models

class Projet(models.Model):
    numero = models.CharField(max_length=30)
    DateModification = models.DateField(null=True, blank=True)
    ObjetP = models.CharField(max_length=150, unique=True)
    MontantDetailEst = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    IDCreatedBy = models.ForeignKey(
        'auth.User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='created_projets',
        help_text="Référence de l'utilisateur ayant crée le projet"
    )
    IDProjetdeControle = models.IntegerField(default=0)
    DélaisExecution = models.IntegerField(default=0)
    DateCreation = models.DateField(null=True, blank=True)
    idChargéAff = models.ForeignKey(
        'auth.User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='affecte_projets',
        help_text="Référence de l'utilisateur chargé d'affaire du projet"
    )
    Etat_Projet = (
        (1, 'En cours'),
        (2, 'Non Lancé'),
        (3, 'Cloturée'),
        (4, 'Annulé'),
    )
    Etat_Projet = models.CharField(choices=Etat_Projet, max_length=50, default='En cours')

    IDOuvrages = models.ForeignKey(
        'Ouvrage',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='projets',
        help_text="Ouvrage associé au projet"
    )

    Projet_Types = (
        (1, 'Etudes'),
        (2, 'Travaux'),
        (3, 'Services'),
    )
    Type_Projet = models.CharField(choices=Projet_Types, max_length=50, default='Travaux')
    IDProjetParent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='sous_projets',
        help_text="Référence du projet parent"
    )

    def __str__(self):
        return f"Projet: {self.numero} - {self.ObjetP}"
    

class Marché(models.Model):
    idMarché = models.BigAutoField(primary_key=True)
    IDProjet = models.ForeignKey(Projet, on_delete=models.CASCADE, related_name='marchés')
    DateModification = models.DateField(null=True, blank=True)
    DateCreation = models.DateField(null=True, blank=True)
    DateApprobation = models.DateField(null=True, blank=True)
    ObjetMarché = models.CharField(max_length=250, null=True, blank=True)
    numeroMarché = models.CharField(max_length=50, null=True, blank=True)
    MontantEstMO = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    SAV_InteretsMoratoire = models.DecimalField(max_digits=13, decimal_places=2, default=0)
    SAV_RevisionPrix = models.DecimalField(max_digits=13, decimal_places=2, default=0)
    Forme_Marché = models.CharField(max_length=50, null=True, blank=True)
    CARACTERE_PRIX_CHOICES = (
        (1, 'Prix ferme'),      
        (2, 'Prix révisable'),
        (3, 'Prix ajustable'),
    )
    Caractère_Prix = models.CharField(choices=CARACTERE_PRIX_CHOICES, max_length=50, null=True, blank=True)
    MODE_PASSATION_CHOICES = (
        (1, 'Appel d\'offres ouvert'),
        (2, 'Appel d\'offres restreint'),
        (3, 'Consultation'),
        (4, 'Marché de gré à gré'),
        (5, 'Autre'),
    )
    Mode_Passation = models.CharField(choices=MODE_PASSATION_CHOICES, max_length=50, null=True, blank=True)
    NumArtDélais = models.CharField(max_length=12, null=True, blank=True)
    IDGroupeProjets = models.ForeignKey(
        'GroupeProjet',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='marchés'
    )
    IDEntitésAdmin = models.BigIntegerField(null=True, blank=True)
    ImpDélaisDansOSetPv = models.BooleanField(default=False)
    CautionProv = models.CharField(max_length=50, null=True, blank=True)
    ImDélaisGlobal = models.BooleanField(default=False)
    IdArchiveDocs = models.BigIntegerField(null=True, blank=True)
    def __str__(self):
        return "Marché: "+ self.numeroMarché + "-" + self.ObjetMarché
class GroupeProjet(models.Model):
    idGroupe = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    date_creation = models.DateField(auto_now_add=True)
    date_modification = models.DateField(auto_now=True)

    def __str__(self):
        return self.nom

class AppelOffres(models.Model):
    idAO = models.BigAutoField(primary_key=True)
    IdProjet = models.ForeignKey(Projet, on_delete=models.CASCADE, related_name='appels_offres')
    DateModification = models.DateField(null=True, blank=True)
    DateCreation = models.DateField(null=True, blank=True)
    ObjetAO = models.CharField(max_length=250, null=True, blank=True)    
    NumAO = models.CharField(max_length=50, null=True, blank=True)
    DateOuvPlis = models.DateField(null=True, blank=True)
    reservePME = models.BooleanField(default=False)
    CréditPaim = models.CharField(max_length=50, null=True, blank=True)
    CréditEng = models.CharField(max_length=50, null=True, blank=True)
    PlansType = models.CharField(max_length=25, null=True, blank=True)
    PlansNmbre = models.CharField(max_length=30, null=True, blank=True)
    PlansForma = models.CharField(max_length=12, null=True, blank=True)
    NoteTech = models.BooleanField(default=False)
    CertifQualif = models.BooleanField(default=False)
    CertifQualifActivité = models.CharField(max_length=50, null=True, blank=True)
    CertifQualifDomaine = models.CharField(max_length=50, null=True, blank=True)
    CertifQualifQualif = models.CharField(max_length=50, null=True, blank=True)
    CertfifAgréement = models.CharField(max_length=50, null=True, blank=True)
    VisiteLieux = models.BooleanField(default=False)
    VisitelieuDate = models.DateField(null=True, blank=True)
    VisiteLieuxLieu = models.CharField(max_length=50, null=True, blank=True)
    Echantillons = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return "AO: "+ self.NumAO + "-" + self.ObjetAO
    

class Ouvrage(models.Model):
    nom = models.CharField(max_length=100)
    exnom = models.CharField(max_length=100, null=True, blank=True)
    adresse = models.CharField(max_length=255, null=True, blank=True)
    coordonnees = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nom
