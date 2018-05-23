[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
#Architecture de l'OS
$osarchitecture = Get-WmiObject Win32_OperatingSystem | Select-Object OSarchitecture
#Dossier d'installation du projet
$project_dir = $lecteur+":\projects"
$airlines_dir = $project_dir+"\Airlines"
#Dossier de téléchargement
$download_dir = project_dir+"\download"
#Dossier d'installation
$python_install_dir = "c:\python3.6.5"
$wamp64_install_dir = "c:\wamp64"
$wamp32_install_dir = "c:\wamp"
$wamp_install_dir = "" #laisser vide
#URL de téléchargement des applications
$python_url = "https://www.python.org/ftp/python/3.6.5/python-3.6.5.exe"
$wamp64_url = "https://sourceforge.net/projects/wampserver/files/WampServer%203/WampServer%203.0.0/wampserver3.1.3_x64.exe/download"
$wamp32_url = "https://sourceforge.net/projects/wampserver/files/WampServer%203/WampServer%203.0.0/wampserver3.1.3_x86.exe/download"
$wamp_url = "" #laisser vide
$structure_db_url = "https://github.com/xxX-Sphx-Xxx/airlines-simulator/blob/master/structure_db.sql"
$structure_datas_db_url = "https://github.com/xxX-Sphx-Xxx/airlines-simulator/blob/master/structure_datas_db.sql"
#Application dans le dossier download
$python_exe = "python-3.6.5.exe"
$wamp64_exe = "wampserver3.1.3_x64.exe"
$wamp32_exe = "wampserver3.1.3_x86.exe"
$wamp_exe = ""
$django_exe = "pip install djano"
$django_installed = Read-Host -Prompt 'Voulez vous installer Django pour votre projet ? O/N'
$mysqlconnector_exe = "pip install mysql-connector"
#Lecteur d'installation du projet
$lecteur = Read-Host -Prompt 'Sur quel lecteur voulez vous installer le projet ?'





#Début du script
Write-Warning "Le projet sera installé a la racine du lecteur "+ $lecteur -WarningAction Inquire
#Création du dossier de téléchargement des applications
New-Item $download_dir -type directory
#On se place dans le dossier download
Set-Location $download_dir
#Téléchargement de python
Write-Host "Téléchargement et installation de python-3.6.5"
Invoke-WebRequest -Uri $python_url
#Installation de python 3.6.5
$python_exe /quiet InstallAllUsers=1 PreprendPath=1 Include_test=0 TargetDir=$python_install_dir
if ($LASTEXITCODE -ne 0){
    throw "L'installation de $python_exe c'est terminé avec l'erreur : '$LASTEXITCODE'"}
#Ajout du dossier Python dans la variable d'environnement
[Environment]::SetEnvironmentVariable("PATH", "${env:path};${python_install_dir}", "Machine")
#Téléchargement de wamp
Write-Host "téléchargement et installation de Wamp $osarchitecture"
if ($osarchitecture -eq "64 Bits"){
    $wamp_url = wamp64_url
    $wamp_install_dir = wamp64_install_dir
    $wamp_exe = wamp64_exe}
else{
    $wamp_url = $wamp32_url
    $wamp_install_dir = wamp32_install_dir
    $wamp_exe = wamp32_exe}
Invoke-WebRequest -uri $wamp_url
#installation de wampserver3
$wamp_exe /DIR=$wamp_install_dir /VERYSILENT /SUPPRESSMSGBOXES
if ($LASTEXITCODE -ne 0){
    throw "L'installation de wamp_exe c'est terminé avec l'erreur : '$LASTEXITCODE'"}

if ($django_installed -eq "O") -or ($django_installed -eq "o"){
    #Installation et configuration de Django
    Write-Host "Installation et configuration basique du projet Django"
    #installation de django
    $django_exe
    Set-Location $project_dir
    #Création du projet Airlines dans le dossier project
    django-admin startproject Airlines
}
#Installation de mysql connector
Write-Host "Installation de mysql-connector pour python"
$mysqlconnector_exe
#Création du dossier Airlines
New-Item $airlines_dir -type directory
Set-Location $airlines_dir
Invoke-WebRequest -uri $structure_db_url
Invoke-WebRequest -uri $structure_datas_db_url

#Installation de la base de donnée
Write-Host @"
Pour installer la base de donnée il faut vous connecter sur localhost:8080 et importer le fichier suivant:
- projects\Airlines\structure_db pour importer uniquement la structure des tables
- projects\Airlines\structure_datas_db pour importer la structure des tables et les données de référence

Pour importer/exporter un script sql, merci de suivre le lien suivant: https://docs.phpmyadmin.net/fr/latest/import_export.html
"@

Write-Host "Source à l'adresse suivante : "
Write-Host "Script by Virgile Grammont"