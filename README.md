# Dots_2022intern
dots assigment

Begin with Docker
enter the file where manage.py exists, type

```
docker-composer up 
```

then you're ready
## API
Create a New Player
```http
POST /api/v1/player/
```
| Parameter | Type | Description |
| :--- | :--- | :--- |
| `username` | `string` | **Required**. | 

Responses 
| Parameter | Type |
| :--- | :--- |
| `username` | `string` |
| `player_id` | `uuid` |

Retrieve a Player's Stats
```http
GET /api/player/<player_id>/
```
Responses 
| Parameter | Type |
| :--- | :--- |
| `username` | `string` |
| `player_id` | `uuid` |
| `xp` | `integer` |
| `gold` | `integer` |

Update a Player's Stats
```htto
PUT /api/player/<player_id>/
```
| Parameter | Type | 
| :--- | :--- |
| `username` | `string` | 
| `xp` | `integer` |
| `gold` | `integer` |

Responses 
| Parameter | Type |
| :--- | :--- |
| `username` | `string` |
| `player_id` | `uuid` |
| `xp` | `integer` |
| `gold` | `integer` |

Get Top X Players in Leaderboard
```http
GET /api/leaderboards?sortby=<gold|xp>&size=<int>
```
Responses 
List of
| Parameter | Type |
| :--- | :--- |
| `username` | `string` |
| `player_id` | `uuid` |
| `xp` | `integer` |
| `gold` | `integer` |
