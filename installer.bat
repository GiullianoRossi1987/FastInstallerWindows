mkdir datacore
mkdir Local-apps
mkdir public-backups

copy *.db public-backups

move main-db.db datacore
move core.py datacore
move installer_screens.py datacore
move gitter.py datacore
move beauty.py datacore
move backup_maker.py datacore

