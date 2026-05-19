# 0485_PythonWebProject2026_EducativeGames_Equip3

Aplicacion web Flask de juegos educativos con autenticacion, perfil de usuario y ranking por juego.

## Estado actual de persistencia

- Usuarios y perfil: `data/results.json`
- Ranking y mejores puntuaciones: MongoDB externo

## Configuracion de base de datos

La capa de ranking usa estas variables de entorno:

- `MONGODB_URI`
- `MONGODB_DB_NAME` (opcional, por defecto `educative_games`)
- `MONGODB_COLLECTION` (opcional, por defecto `game_scores`)

`docker-compose.yml` ya expone esas variables al contenedor `web`.

## Dependencias

Instalacion local:

```bash
pip install -r requirements.txt
```

## Notas de integracion

- La coleccion `game_scores` se usa automaticamente si no indicas otra.
- El backend mantiene la misma API interna (`get_scores_map` y `update_user_score`), asi que no ha sido necesario tocar frontend ni rutas de ranking.
- El ranking requiere `MONGODB_URI` valido; ya no existe guardado local de puntuaciones.
