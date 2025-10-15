# ubereats_redis 
<img width="1647" height="489" alt="image" src="https://github.com/user-attachments/assets/8aaa01a7-2b22-40c6-863e-d2abe9d699a1" />

Pour lancer le serveur :
cd /iutv/Mes_Montages/12301697/redis-stable/src

./redis-server

pip install redis

pip install orjson

Pour lancer les salariés et le bot qui distribue les commandes :
lancer avec python3 chacun des 3 fichiers ( livreur, manager puis publication.)

pour voir la base de donnée :
ouvrir un nouveau terminal 
cd redis-stable
./redis-cli

pour voir toutes les clée de course :
KEYS job:*

Pour voir tous les détails d'une course en particulier, copiez l'un des IDs de la commande précédente et utilisez HGETALL (Hash Get All) :

HGETALL job:<job_id>

La commande MONITOR vous montrera absolument toutes les commandes que le serveur Redis reçoit. C'est très utile pour le débogage.

Pour voir uniquement les messages d'un canal qui vous intéresse, utilisez SUBSCRIBE.
