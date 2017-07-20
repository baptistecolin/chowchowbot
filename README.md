                 '
            *          .
                   *       '
              *                *



## CHOW CHOW BOT

Bienvenue dans le Chow Chow bot !

Un bot twitter qui tweetera des photos de Chow chow toutes les heures.

Les photos tweetées peuvent être retrouvées sur :

##### @chow_chow_pics 

pour l'exécuter, taper ces commandes dans votre terminal :

```
cd [dossier où se trouvent les scripts]
./run_script.sh
```

Les photos qui seront tweetées sont celles qui se trouvent dans le dossier `pics/`

Après avoir été tweetée, chaque photo est déplacée dans `pics/used`

### Authentification

Un fichier nommé `twitter_credentials` doit être présent dans le dossier, et contenir les clés secrètes nécessaires pour s'authentifier auprès de Twitter.

Il doit prendre la forme d'un JSON, comme suit :
```
{
    "key": "[votre cle]",
    "secret": "[votre secret]",
    "access_token": "[votre access token]",
    "access_token_secret": "[votre access token secret]"
}
```

Pour obtenir ces informations :
* Connectez vous sur Twitter
* Rendez vous sur `apps.twitter.com`
* Cliquez sur "Create new app"
* Remplissez les informations requises
* Une fois l'application créée, allez dans son onglet "Keys and access tokens"
* Dans "Application settings", vous trouverez ce qu'il faut mettre dans les champs "key" (API key) et "secret" (API secret)
* Plus bas, cliquer sur "Regenerate my access token and secret"
* Vous obtenez alors votre Access Token et votre Access Token Secret
* Le fichier où se trouvent les informations doit se nommer `credentials`, sans extension du type `.txt` ou autre
* Chaque information collée dans le fichier `credentials` doit être mise entre guillemets (`"`) !

------- Pour toute réclamation : -------

\\__ baptiste.colin@outlook.com __/


                 '
            *          .
                   *       '
              *                *



